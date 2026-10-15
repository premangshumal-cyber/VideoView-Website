#!/usr/bin/env python3
"""Offline release gate: crawl HTML links, metadata, schema and release URLs.

Run from any directory with Python 3; no dependencies or network needed.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://www.videoview.online/'

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        self.nodes.append((tag, dict(attrs)))
    def select(self, tag, **attrs):
        return [a for t, a in self.nodes if t == tag and all(a.get(k) == v for k, v in attrs.items())]

errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

pages = {p.name: (p.read_text(), Page(p.read_text())) for p in ROOT.glob('*.html')}
titles = []
descriptions = []
links = 0
for name, (source, page) in pages.items():
    check(len(page.select('h1')) == 1, f'{name}: needs exactly one h1')
    check(len(page.select('main')) == 1, f'{name}: needs one main landmark')
    check(bool(page.select('html', lang='en')), f'{name}: missing language')
    check(len(page.select('meta', name='viewport')) == 1, f'{name}: missing viewport')
    ids = [a['id'] for _, a in page.nodes if a.get('id')]
    check(len(ids) == len(set(ids)), f'{name}: duplicate IDs')
    for img in page.select('img'):
        check('alt' in img and 'width' in img and 'height' in img, f'{name}: image needs alt/dimensions: {img}')
    if name != '404.html':
        title = re.findall(r'<title>(.*?)</title>', source)
        desc = page.select('meta', name='description')
        check(len(title) == 1 and len(desc) == 1, f'{name}: title/description missing or duplicated')
        titles.extend(title)
        descriptions.extend(d.get('content') for d in desc)
        url = ORIGIN + ('' if name == 'index.html' else name)
        check(page.select('link', rel='canonical') == [{'rel': 'canonical', 'href': url}], f'{name}: wrong canonical')
        check(page.select('meta', property='og:url')[0]['content'] == url, f'{name}: wrong OG URL')
        check(bool(page.select('meta', property='og:image')), f'{name}: missing social image')
        check('noindex' not in source, f'{name}: unexpected noindex')
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S)
        check(len(blocks) == 1, f'{name}: missing or duplicate JSON-LD graph')
        for block in blocks:
            data = json.loads(block)
            check(data.get('@context') == 'https://schema.org', f'{name}: invalid schema context')
            check('aggregateRating' not in block and '"review"' not in block, f'{name}: unverified reviews present')
            for entity in data['@graph']:
                if entity.get('@type') == 'SoftwareApplication':
                    check(entity.get('softwareVersion') in ('1.1.0', '1.0.0'), f'{name}: release version changed')
                    check(entity.get('downloadUrl', '').startswith('https://github.com/premangshumal-cyber/VideoView-Website/releases/download/'), f'{name}: unexpected binary origin')
    else:
        check('noindex' in page.select('meta', name='robots')[0]['content'], '404 must not be indexed')
    for tag, attrs in page.nodes:
        attr = 'href' if tag in ('a', 'link') else 'src' if tag in ('img', 'script') else None
        if not attr or not attrs.get(attr):
            continue
        target = urlsplit(attrs[attr])
        if target.netloc or target.scheme:
            continue
        links += 1
        path = unquote(target.path).lstrip('/') or (name if target.fragment else 'index.html')
        check((ROOT/path).is_file(), f'{name}: broken local link {attrs[attr]}')
        if target.fragment and path in pages:
            check(any(a.get('id') == target.fragment for _, a in pages[path][1].nodes), f'{name}: broken anchor {attrs[attr]}')
check(len(titles) == len(set(titles)), 'Duplicate page titles')
check(len(descriptions) == len(set(descriptions)), 'Duplicate descriptions')
sitemap = ET.parse(ROOT/'sitemap.xml')
urls = [node.text for node in sitemap.findall('.//{*}loc')]
expected = {ORIGIN+('' if n == 'index.html' else n) for n in pages if n != '404.html'}
check(len(urls) == len(set(urls)) and set(urls) == expected, 'Sitemap must match all canonical public pages')
check('Sitemap: '+ORIGIN+'sitemap.xml' in (ROOT/'robots.txt').read_text(), 'Wrong robots sitemap')
releases = {
    'setup': 'v1.1.0/VideoView-Setup.exe',
    'portable': 'v1.1.0/VideoView-Portable.zip',
    'source': 'v1.1.0/VideoView-Source.zip',
    'thirdparty': 'v1.1.0/VideoView-ThirdPartySources.zip',
}
for key, path in releases.items():
    a = pages['downloads.html'][1].select('a', **{'data-download': key})
    check(len(a) == 1 and a[0]['href'] == 'https://github.com/premangshumal-cyber/VideoView-Website/releases/download/'+path, f'Broken no-JavaScript download for {key}')
config = json.loads((ROOT/'vercel.json').read_text())
check({'source': '/index.html', 'destination': '/', 'permanent': True} in config['redirects'], 'Missing duplicate-homepage redirect')
manifest = (ROOT/'downloads/SHA256SUMS.txt').read_text()
check('31f97cb3575388b4ab47dc1ee91a0ab6372353df06460a4ec074d8fa0439967f  VideoView-Android-1.0.0.apk' in manifest, 'APK hash missing')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(pages)} HTML files, {len(urls)} sitemap URLs, {links} local links/assets/anchors; metadata, JSON-LD and direct binary links valid.')
