"""Refresh Scholar data; publish only after a complete, validated fetch."""

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path


def normalize_author(author, scholar_id):
    if author.get('scholar_id') != scholar_id:
        raise ValueError('Google Scholar returned an unexpected profile')
    if not author.get('name'):
        raise ValueError('Google Scholar returned an empty profile')
    citedby = author.get('citedby')
    if type(citedby) is not int or citedby < 0:
        raise ValueError('Google Scholar did not return a valid citation count')
    publications = author.get('publications')
    if not isinstance(publications, list):
        raise ValueError('Google Scholar did not return the publication list')
    result = dict(author)
    result['publications'] = {p['author_pub_id']: p for p in publications}
    result['updated'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    return result


def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    from scholarly import scholarly

    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip() or 'AMUlDdEAAAAJ'
    scholarly.set_timeout(20)
    scholarly.set_retries(2)
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    author = normalize_author(author, scholar_id)
    results = Path(__file__).resolve().parent / 'results'
    results.mkdir(exist_ok=True)
    payloads = {
        'gs_data.json': author,
        'gs_data_shieldsio.json': {
            'schemaVersion': 1,
            'label': 'citations',
            'message': str(author['citedby']),
        },
    }
    for filename, data in payloads.items():
        temporary = results / (filename + '.tmp')
        temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        temporary.replace(results / filename)
    print(f"Updated {author['name']}: {author['citedby']} citations, "
          f"{len(author['publications'])} publications ({author['updated']})")


if __name__ == '__main__':
    main()
