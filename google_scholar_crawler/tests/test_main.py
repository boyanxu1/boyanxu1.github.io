import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock
from urllib.error import HTTPError, URLError

SPEC = importlib.util.spec_from_file_location('crawler', Path(__file__).parents[1] / 'main.py')
crawler = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(crawler)
ID = 'test_profile'
HTML = '''<div id="gsc_prf_in">Test Author</div>
<table id="gsc_rsb_st"><tr><td class="gsc_rsb_std">1,234</td></tr></table>
<table><tbody id="gsc_a_b">
<tr class="gsc_a_tr"><td><a class="gsc_a_at" href="/citations?view_op=view_citation&amp;citation_for_view=test_profile:paper1">A paper</a></td><td><a class="gsc_a_ac">12</a></td></tr>
<tr class="gsc_a_tr"><td><a class="gsc_a_at" href="/citations?view_op=view_citation&amp;citation_for_view=test_profile:paper2">Another paper</a></td><td><a class="gsc_a_ac"></a></td></tr>
</tbody></table><span id="gsc_a_nn">1–2</span><button id="gsc_bpf_more" disabled="">Show more</button>'''


class ParserTests(unittest.TestCase):
    def test_complete_profile_and_blank_zero_count(self):
        data = crawler.parse_profile(HTML, ID)
        self.assertEqual(data['citedby'], 1234)
        self.assertEqual(data['publications'][ID + ':paper2']['num_citations'], 0)
        self.assertEqual(len(data['publications']), 2)
        self.assertTrue(data['updated'].endswith('+00:00'))

    def test_rejects_partial_challenge_invalid_and_wrong_profile(self):
        cases = [
            (HTML.replace(' disabled=""', ''), 'incomplete_publications'),
            ('<form id="captcha-form"></form>', 'access_challenge'),
            ('<html>Access denied</html>', 'invalid_response'),
            (HTML.replace('test_profile:paper1', 'someone_else:paper1'), 'invalid_publication'),
            (HTML.replace('test_profile:paper2', 'test_profile:paper1'), 'invalid_publication'),
            (HTML.replace('1,234', 'unknown'), 'invalid_response'),
            (HTML.replace('class="gsc_a_ac"', 'class="missing"'), 'invalid_response'),
            (HTML.replace('id="gsc_bpf_more"', 'id="missing"'), 'invalid_response'),
            (HTML.replace('>12<', '>-1<'), 'invalid_response'),
            (HTML.replace('1–2', '1–49'), 'incomplete_publications'),
        ]
        for html, reason in cases:
            with self.subTest(reason=reason, html=html[:40]):
                with self.assertRaisesRegex(crawler.RefreshError, reason):
                    crawler.parse_profile(html, ID)

    def test_rejects_invalid_normalized_counts_and_empty_list(self):
        base = {'scholar_id': ID, 'name': 'Test', 'citedby': 12,
                'publications': [{'author_pub_id': ID + ':paper', 'num_citations': 12, 'bib': {'title': 'A'}}]}
        for value in [-1, True, '12', None]:
            data = {**base, 'citedby': value}
            with self.assertRaises(crawler.RefreshError):
                crawler.normalize_author(data, ID)
        with self.assertRaisesRegex(crawler.RefreshError, 'empty_publications'):
            crawler.normalize_author({**base, 'publications': []}, ID)
        data = copy.deepcopy(base)
        data['publications'][0]['num_citations'] = True
        with self.assertRaises(crawler.RefreshError):
            crawler.normalize_author(data, ID)


class TransportTests(unittest.TestCase):
    def test_one_request_with_timeout_and_public_profile_url(self):
        opener = MagicMock()
        response = opener.open.return_value.__enter__.return_value
        response.status = 200
        response.read.return_value = HTML.encode()
        crawler.fetch_profile(ID, opener)
        opener.open.assert_called_once()
        request = opener.open.call_args.args[0]
        self.assertEqual(request.full_url, 'https://scholar.google.com/citations?user=test_profile&hl=en&pagesize=100')
        self.assertEqual(opener.open.call_args.kwargs, {'timeout': 20})

    def test_403_429_redirect_and_timeouts_are_never_retried(self):
        for error, reason in [
            (HTTPError('https://scholar.google.com', 403, '', {}, None), 'http_403'),
            (HTTPError('https://scholar.google.com', 429, '', {}, None), 'http_429'),
            (HTTPError('https://scholar.google.com', 302, '', {}, None), 'http_302'),
            (TimeoutError(), 'timeout'),
            (URLError('offline'), 'network_error'),
        ]:
            with self.subTest(reason=reason):
                opener = MagicMock()
                opener.open.side_effect = error
                with self.assertRaisesRegex(crawler.RefreshError, reason):
                    crawler.fetch_profile(ID, opener)
                opener.open.assert_called_once()

    def test_redirect_handler_never_follows(self):
        self.assertIsNone(crawler.NoRedirects().redirect_request(None, None, 302, '', {}, 'https://example.com'))

    def test_rejects_oversized_response(self):
        opener = MagicMock()
        response = opener.open.return_value.__enter__.return_value
        response.status = 200
        response.read.return_value = b'x' * (crawler.MAX_RESPONSE_BYTES + 1)
        with self.assertRaisesRegex(crawler.RefreshError, 'response_too_large'):
            crawler.fetch_profile(ID, opener)


class RefreshTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.output = self.root / 'output'
        self.previous = self.root / 'gs_data.json'
        self.data = crawler.parse_profile(HTML, ID)
        self.data['updated'] = '2026-01-01T00:00:00+00:00'
        self.previous.write_text(json.dumps(self.data))
        self.original = self.previous.read_bytes()

    def test_failures_preserve_last_good_and_do_not_create_fresh_payload(self):
        for reason in ['http_403', 'http_429', 'timeout', 'incomplete_publications', 'invalid_response']:
            with self.subTest(reason=reason):
                self.output.mkdir(exist_ok=True)
                (self.output / 'gs_data.json').write_text('old local output')
                (self.output / 'gs_data_shieldsio.json').write_text('old local badge')
                fetcher = MagicMock(side_effect=crawler.RefreshError(reason))
                self.assertEqual(crawler.refresh(self.output, self.previous, ID, fetcher), 2)
                self.assertEqual(self.previous.read_bytes(), self.original)
                self.assertEqual(sorted(p.name for p in self.output.iterdir()), ['gs_status.json'])
                status = json.loads((self.output / 'gs_status.json').read_text())
                self.assertEqual(status['state'], 'stale')
                self.assertEqual(status['last_success'], self.data['updated'])
                self.assertEqual(status['reason'], reason)
                self.assertEqual(crawler.report(self.output), 2)

    def test_success_writes_compatible_data_badge_and_status(self):
        new_data = crawler.parse_profile(HTML, ID)
        self.assertEqual(crawler.refresh(self.output, self.previous, ID, lambda _: new_data), 0)
        self.assertEqual(self.previous.read_bytes(), self.original)
        status = json.loads((self.output / 'gs_status.json').read_text())
        self.assertEqual(status['state'], 'fresh')
        self.assertEqual(status['last_success'], new_data['updated'])
        self.assertEqual(json.loads((self.output / 'gs_data.json').read_text()), new_data)
        self.assertEqual(json.loads((self.output / 'gs_data_shieldsio.json').read_text())['message'], '1234')
        self.assertEqual(crawler.report(self.output), 0)

    def test_first_run_failure_is_unavailable_not_zero(self):
        fetcher = MagicMock(side_effect=crawler.RefreshError('http_403'))
        self.assertEqual(crawler.refresh(self.output, None, ID, fetcher), 2)
        status = json.loads((self.output / 'gs_status.json').read_text())
        self.assertEqual(status['state'], 'unavailable')
        self.assertIsNone(status['last_success'])
        self.assertFalse((self.output / 'gs_data.json').exists())

    def test_interrupted_process_status_never_fetches(self):
        fetcher = MagicMock()
        self.assertEqual(crawler.refresh(self.output, self.previous, ID, fetcher, failed_attempt=True), 2)
        fetcher.assert_not_called()
        self.assertEqual(self.previous.read_bytes(), self.original)

    def test_programming_errors_are_not_silenced_as_an_upstream_failure(self):
        with self.assertRaises(RuntimeError):
            crawler.refresh(self.output, self.previous, ID, MagicMock(side_effect=RuntimeError('bug')))

    def test_previous_file_cannot_be_deleted_by_output_cleanup(self):
        with self.assertRaisesRegex(ValueError, 'outside the output directory'):
            crawler.refresh(self.root, self.previous, ID, MagicMock())
        self.assertEqual(self.previous.read_bytes(), self.original)

    def test_malformed_history_fails_closed_without_fetching_or_overwriting(self):
        self.previous.write_text('{broken')
        fetcher = MagicMock()
        with self.assertRaises(ValueError):
            crawler.refresh(self.output, self.previous, ID, fetcher)
        fetcher.assert_not_called()
        self.assertEqual(self.previous.read_text(), '{broken')


if __name__ == '__main__':
    unittest.main()
