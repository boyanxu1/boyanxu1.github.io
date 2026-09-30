# Citation updater

The homepage reads `gs_data.json` from the `google-scholar-stats` branch. Its
`updated` value is the last **successful, complete** fetch, never the latest
attempt. `gs_status.json` separately records the attempt's `checked_at`, `state`
(`fresh`, `stale`, or `unavailable`), `last_success`, and failure reason.

## Why the fetch changed

The old scholarly 1.5.1 transport repeatedly renewed sessions after HTTP 403.
That branch did not increment its retry counter, so `set_retries(2)` still ran
until the workflow's 150-second external timeout.

The replacement makes one public-profile request, with a 20-second network
timeout and a 60-second workflow ceiling. It does not follow redirects, retry
403/429, rotate sessions, use proxy services, or solve access challenges. It uses
`/citations?user=...`, the public-profile path allowed by Scholar's
[robots.txt](https://scholar.google.com/robots.txt). This is **not a guarantee of
access**; Google's server can still deny the request. See also Google's
[automated-access guidance](https://scholar.google.com/intl/en/scholar/help.html#questions).

The updater requests up to 100 publications and requires the page's “Show more”
button to be disabled. It will not crawl prohibited `cstart` pagination. An
incomplete list, missing fields, duplicate/wrong-profile IDs, challenge, timeout,
or HTTP error must not overwrite the published snapshot. If a profile outgrows
one page, the updater reports `incomplete_publications` rather than dropping
publications. When the page includes a displayed publication range, its count
must also match the parsed rows.

## Failure behavior

- A successful refresh writes the homepage-consumed fields (`citedby`, `updated`,
  name/profile ID, and keyed publication titles/counts), the badge, and fresh status.
  Other scholarly-only metadata (for example h-index and affiliation) is no longer
  included in newly fetched snapshots
- A blocked refresh writes **only status**; counts, per-paper data, and the old
  successful timestamp remain byte-for-byte unchanged on the data branch
- The workflow publishes this status, reports the reason and last success, and
  still fails. A green run must not imply that stale data was refreshed
- The homepage labels data older than 48 hours as cached, even before a status
  file exists. A matching stale status also labels a more recent snapshot cached
- Interrupted fetches get `fetch_process_failed`; programming/publishing failures
  are not silently treated as successful refreshes
- Malformed prior data stops the run before fetching or publishing, so its
  successful timestamp is never guessed

Continued 403 responses require permitted upstream access; changing a timeout
cannot create fresh counts. Keep the dated snapshot and link to the public
Scholar profile until access is available. A user-verified manual snapshot can
also be reviewed and committed with its **actual observation timestamp**. Do
not substitute another provider's count under the Google Scholar label or reset
an old snapshot's timestamp.

## Checks and operation

```sh
python -m pip install -r google_scholar_crawler/requirements.txt
python -m unittest discover -s google_scholar_crawler/tests -v
node --test google_scholar_crawler/tests/test_display.cjs
```

All tests are offline with synthetic fixtures. Pull requests run these tests
only; they neither contact Scholar nor update the published data branch.

The scheduled workflow runs on `main` daily at 08:17 UTC, or on an authorized
manual dispatch. `GOOGLE_SCHOLAR_ID` is read from the existing repository secret,
falling back to this site's public profile ID. No new account/key is required.

To run locally after obtaining the existing data-branch snapshot:

```sh
python google_scholar_crawler/main.py --previous-data citation-data/gs_data.json
python google_scholar_crawler/main.py --report
```

Exit 0 means fresh data; exit 2 means no fresh data. Keep the previous-data file
outside the output directory. Inspect the reason before trying again, and stop
on access-denied or challenge responses. Do not repeatedly rerun a blocked job.
