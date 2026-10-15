#!/usr/bin/env python3
"""Notify IndexNow after a verified production update. No analytics or cookies.

Run without --submit to inspect the exact URL list. Use --submit only after
these changes are live. A 200/202 acknowledges notification, not indexing.
"""
from pathlib import Path
from urllib.request import Request, urlopen
import argparse
import json
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--submit', action='store_true')
args = parser.parse_args()
keyfiles = [p for p in root.glob('*.txt') if re.fullmatch(r'[a-f0-9]{32}\.txt', p.name)]
if len(keyfiles) != 1:
    raise SystemExit('Expected one root IndexNow verification file')
key = keyfiles[0].read_text().strip()
urls = [n.text for n in ET.parse(root/'sitemap.xml').findall('.//{*}loc')]
host = 'www.videoview.online'
if not all(u.startswith('https://'+host+'/') for u in urls):
    raise SystemExit('Unexpected sitemap host')
payload = {'host':host,'key':key,'keyLocation':'https://'+host+'/'+keyfiles[0].name,'urlList':urls}
print(json.dumps({'host':host,'urlList':urls}, indent=2))
if args.submit:
    with urlopen(payload['keyLocation'], timeout=30) as response:
        if response.status != 200 or response.read().decode().strip() != key:
            raise SystemExit('Live IndexNow verification file does not match')
    request = Request('https://api.indexnow.org/indexnow', data=json.dumps(payload).encode(), headers={'Content-Type':'application/json; charset=utf-8'}, method='POST')
    with urlopen(request, timeout=30) as response:
        print('IndexNow HTTP',response.status,'— submission received; indexing is not confirmed.')
