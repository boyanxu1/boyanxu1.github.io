const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.resolve(__dirname, '../../_includes/fetch_google_scholar_stats.html'), 'utf8')
  .replace(/^<script>\s*/, '').replace(/\s*<\/script>\s*$/, '');
const now = Date.parse('2026-09-30T12:00:00Z');
const fresh = {citedby: 1234, updated: '2026-09-30T08:00:00+00:00', publications: {'test:paper': {num_citations: 12}}};
async function display(responses, data = fresh) {
  const elements = {
    total_cit: {textContent: ''},
    'citation-summary': {hidden: true},
    'citation-updated': {textContent: ''}
  };
  const paper = {textContent: '', getAttribute: () => 'test:paper'};
  const requests = [];
  const timers = new Set();
  const context = {
    document: {getElementById: id => elements[id], querySelectorAll: () => [paper]},
    Date: class extends Date {static now() {return now;}},
    AbortController,
    setTimeout(fn, ms) {const id = setTimeout(fn, ms); timers.add(id); return id;},
    clearTimeout(id) {clearTimeout(id); timers.delete(id);},
    async fetch(url) {
      requests.push(url);
      const next = responses.shift();
      if (next instanceof Error) throw next;
      return {ok: next !== null, json: async () => next === 'DATA' ? data : next};
    }
  };
  vm.runInNewContext(source, context);
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(timers.size, 0, 'request timers must be cleared');
  return {elements, paper, requests};
}

test('fresh snapshot renders total, paper and original date', async () => {
  const {elements, paper} = await display(['DATA', {state: 'fresh', last_success: fresh.updated}]);
  assert.equal(elements.total_cit.textContent, '1,234');
  assert.equal(elements['citation-summary'].hidden, false);
  assert.equal(elements['citation-updated'].textContent, 'Updated 2026-09-30');
  assert.equal(paper.textContent, '| Citations: 12');
});

test('stale status keeps counts and last success date', async () => {
  const {elements} = await display(['DATA', {state: 'stale', last_success: fresh.updated}]);
  assert.equal(elements['citation-updated'].textContent, 'Cached · Last updated 2026-09-30');
  assert.match(elements['citation-updated'].title, /Latest refresh unavailable/);
  assert.equal(elements.total_cit.textContent, '1,234');
});

test('old snapshot is visibly cached without any status file', async () => {
  const {elements} = await display(['DATA', null], {...fresh, updated: '2026-09-16T13:30:41+00:00'});
  assert.equal(elements['citation-updated'].textContent, 'Cached · Last updated 2026-09-16');
});

test('status from a different CDN version is ignored', async () => {
  const {elements} = await display(['DATA', {state: 'stale', last_success: '2026-09-16T13:30:41+00:00'}]);
  assert.equal(elements['citation-updated'].textContent, 'Updated 2026-09-30');
});

test('falls back after first data source fails', async () => {
  const {elements, requests} = await display([new Error('offline'), 'DATA', null]);
  assert.equal(elements.total_cit.textContent, '1,234');
  assert.match(requests[1], /cdn.jsdelivr.net/);
});

test('invalid data falls back, unavailable sources keep summary hidden', async () => {
  const {elements} = await display([{citedby: -1}, new Error('offline')]);
  assert.equal(elements['citation-summary'].hidden, true);
  assert.equal(elements.total_cit.textContent, '');
});

test('unknown timestamp is never advertised as recently updated', async () => {
  const {elements} = await display(['DATA', null], {...fresh, updated: undefined});
  assert.equal(elements['citation-updated'].textContent, 'Last update unknown');
});

test('negative publication count is not rendered', async () => {
  const {paper} = await display(['DATA', null], {...fresh, publications: {'test:paper': {num_citations: -2}}});
  assert.equal(paper.textContent, '');
});
