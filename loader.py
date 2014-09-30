#!/usr/bin/env python
import json

from bs4 import BeautifulSoup
import requests

r = requests.get("http://cespedesfamilybarbecast.libsyn.com/rss")
soup = BeautifulSoup(r.content)
items = soup.select('item')

payload = []

for item in items:
  item_dict = {}
  item_dict['title'] = item.select('title')[0].text.strip()
  item_dict['audio_url'] = item.select('enclosure')[0]['url']
  item_dict['audio_length'] = item.select('enclosure')[0]['length']
  payload.append(item_dict)

with open('payload.json', 'w') as writefile:
  writefile.write(json.dumps(payload))