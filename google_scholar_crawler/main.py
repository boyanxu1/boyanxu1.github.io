"""Refresh a public Scholar profile without retrying access-denied responses."""

import argparse
import json
import os
import re
import socket
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

from bs4 import BeautifulSoup

DEFAULT_SCHOLAR_ID = 'AMUlDdEAAAAJ'
MAX_RESPONSE_BYTES = 2_000_000


class RefreshError(Exception):
    """An unavailable or invalid upstream response; never publish its counts."""


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Do not follow sign-in, CAPTCHA, or alternate-host redirects.
        return None


def timestamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def fetch_profile(scholar_id, opener=None):
    if not re.fullmatch(r'[A-Za-z0-9_-]+', scholar_id):
        raise ValueError('Invalid Google Scholar profile ID')
    # Scholar permits public /citations?user= profiles, but not cstart pages.
    # Never retry a denial, rotate sessions, solve challenges, or use proxies.
    url = 'https://scholar.google.com/citations?' + urlencode(
        {'user': scholar_id, 'hl': 'en', 'pagesize': 100})
    request = Request(url, headers={'User-Agent': 'AcademicHomepageCitationUpdater/1.0'})
    opener = opener or build_opener(ProxyHandler({}), NoRedirects())
    try:
        with opener.open(request, timeout=20) as response:
            if response.status != 200:
                raise RefreshError(f'http_{response.status}')
            body = response.read(MAX_RESPONSE_BYTES + 1)
            if len(body) > MAX_RESPONSE_BYTES:
                raise RefreshError('response_too_large')
            return parse_profile(body.decode('utf-8'), scholar_id)
    except HTTPError as error:
        raise RefreshError(f'http_{error.code}') from error
    except (TimeoutError, socket.timeout) as error:
        raise RefreshError('timeout') from error
    except URLError as error:
        raise RefreshError('network_error') from error
    except UnicodeError as error:
        raise RefreshError('invalid_response') from error


def parse_count(text):
    value = text.strip().replace(',', '')
    if not re.fullmatch(r'[0-9]+', value):
        raise RefreshError('invalid_response')
    return int(value)


def parse_profile(html, scholar_id):
    soup = BeautifulSoup(html, 'html.parser')
    if soup.select_one('#gs_captcha_ccl, #recaptcha, #captcha-form, .rc-doscaptcha-body'):
        raise RefreshError('access_challenge')
    name = soup.select_one('#gsc_prf_in')
    total = soup.select_one('#gsc_rsb_st .gsc_rsb_std')
    papers = soup.select_one('#gsc_a_b')
    more = soup.select_one('#gsc_bpf_more')
    if name is None or total is None or papers is None or more is None:
        raise RefreshError('invalid_response')
    if not more.has_attr('disabled'):
        # Do not publish a first page as a complete bibliography or crawl cstart.
        raise RefreshError('incomplete_publications')
    publications = []
    for row in papers.select('.gsc_a_tr'):
        link = row.select_one('a.gsc_a_at')
        count = row.select_one('.gsc_a_ac')
        if link is None or count is None:
            raise RefreshError('invalid_response')
        ids = parse_qs(urlsplit(link.get('href', '')).query).get('citation_for_view', [])
        if len(ids) != 1:
            raise RefreshError('invalid_response')
        publications.append({
            'author_pub_id': ids[0],
            'bib': {'title': link.get_text(' ', strip=True)},
            # Scholar renders a blank citation link for a zero-citation paper.
            'num_citations': parse_count(count.get_text(strip=True) or '0'),
        })
    displayed_range = soup.select_one('#gsc_a_nn')
    if displayed_range is not None:
        match = re.fullmatch(r'1\s*[\u2013-]\s*([0-9,]+)', displayed_range.get_text(strip=True))
        if match is None or parse_count(match.group(1)) != len(publications):
            raise RefreshError('incomplete_publications')
    return normalize_author({
        'scholar_id': scholar_id,
        'name': name.get_text(' ', strip=True),
        'citedby': parse_count(total.get_text(strip=True)),
        'publications': publications,
    }, scholar_id)


def normalize_author(author, scholar_id):
    if author.get('scholar_id') != scholar_id or not author.get('name', '').strip():
        raise RefreshError('invalid_profile')
    citedby = author.get('citedby')
    if type(citedby) is not int or citedby < 0:
        raise RefreshError('invalid_citation_count')
    publications = author.get('publications')
    if not isinstance(publications, list) or not publications:
        # Fail closed rather than replacing this established profile with empty data.
        raise RefreshError('empty_publications')
    by_id = {}
    for paper in publications:
        if not isinstance(paper, dict):
            raise RefreshError('invalid_publication')
        paper_id = paper.get('author_pub_id', '')
        count = paper.get('num_citations')
        if (not isinstance(paper_id, str) or not paper_id.startswith(scholar_id + ':')
                or len(paper_id) <= len(scholar_id) + 1 or paper_id in by_id
                or type(count) is not int or not 0 <= count <= citedby
                or not paper.get('bib', {}).get('title')):
            raise RefreshError('invalid_publication')
        by_id[paper_id] = paper
    return {**author, 'publications': by_id, 'updated': timestamp()}


def read_previous(path, scholar_id):
    if path is None or not path.exists():
        return None
    data = json.loads(path.read_text(encoding='utf-8'))
    # Validate without changing the original successful fetch timestamp or bytes.
    normalize_author({**data, 'publications': list(data['publications'].values())}, scholar_id)
    updated = datetime.fromisoformat(data['updated'].replace('Z', '+00:00'))
    if updated.tzinfo is None:
        raise ValueError('Previous citation timestamp must have a timezone')
    return data


def write_payloads(output_dir, payloads):
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, data in payloads.items():
        temporary = output_dir / (filename + '.tmp')
        temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        temporary.replace(output_dir / filename)


def refresh(output_dir, previous_path, scholar_id, fetcher=fetch_profile, failed_attempt=False):
    if previous_path is not None and previous_path.resolve().parent == output_dir.resolve():
        raise ValueError('Previous citation data must be outside the output directory')
    previous = read_previous(previous_path, scholar_id)
    # Avoid accidentally reusing successful output from an earlier local run.
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename in ('gs_data.json', 'gs_data_shieldsio.json', 'gs_status.json'):
        (output_dir / filename).unlink(missing_ok=True)
    try:
        if failed_attempt:
            raise RefreshError('fetch_process_failed')
        author = fetcher(scholar_id)
    except RefreshError as error:
        status = {
            'state': 'stale' if previous else 'unavailable',
            'checked_at': timestamp(),
            'last_success': previous['updated'] if previous else None,
            'reason': str(error),
        }
        # Only status is written. The published data and badge stay byte-for-byte intact.
        write_payloads(output_dir, {'gs_status.json': status})
        print(f"Citation refresh unavailable ({error}); last success: {status['last_success'] or 'none'}")
        return 2
    status = {'state': 'fresh', 'checked_at': timestamp(), 'last_success': author['updated'], 'reason': None}
    write_payloads(output_dir, {
        'gs_data.json': author,
        'gs_data_shieldsio.json': {'schemaVersion': 1, 'label': 'citations', 'message': str(author['citedby'])},
        'gs_status.json': status,
    })
    print(f"Updated {author['name']}: {author['citedby']} citations ({author['updated']})")
    return 0


def report(output_dir):
    status = json.loads((output_dir / 'gs_status.json').read_text(encoding='utf-8'))
    if status['state'] == 'fresh':
        data = json.loads((output_dir / 'gs_data.json').read_text(encoding='utf-8'))
        message = f"Fetched **{data['citedby']} citations** at {data['updated']}; {len(data['publications'])} publications."
    else:
        message = (f"**No fresh citation data:** {status['reason']}. "
                   f"Last successful fetch: {status['last_success'] or 'none'}. "
                   'Previously published counts and their timestamp were not changed.')
        print('::warning::' + message)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as summary:
            summary.write(message + '\n')
    return 0 if status['state'] == 'fresh' else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent / 'results')
    parser.add_argument('--previous-data', type=Path)
    parser.add_argument('--failed-attempt', action='store_true')
    parser.add_argument('--report', action='store_true')
    args = parser.parse_args()
    if args.report:
        return report(args.output_dir)
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip() or DEFAULT_SCHOLAR_ID
    return refresh(args.output_dir, args.previous_data, scholar_id, failed_attempt=args.failed_attempt)


if __name__ == '__main__':
    raise SystemExit(main())
