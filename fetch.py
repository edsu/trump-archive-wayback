#!/usr/bin/env python3

"""
Use the [Trump Archive] CSV export to look for snapshots in the Internet
Archive's Wayback Machine. A separate JSON file for each tweet id is
generated with the snapshots.
"""

import re
import csv
import json
import wayback

from tqdm import tqdm
from urllib.parse import urlparse
from collections import defaultdict

wb = wayback.WaybackClient()

ids = []
for tweet in csv.DictReader(open('trump-archive.csv')):
    if tweet['isRetweet'] == 'f':
      ids.append(tweet['id'])
    
tweets = defaultdict(list)
for tweet_id in tqdm(ids):
    url = 'https://twitter.com/realDonaldTrump/status/{}'.format(tweet_id)

    snaps = []
    for result in wb.search(url, matchType='prefix'):
        uri = urlparse(result.url)
        if re.match(r'^/realDonaldTrump/status/(\d{4,})/?$', uri.path,
                re.IGNORECASE):
            snaps.append(result._asdict())

    snaps = sorted(snaps, key=lambda s: s['timestamp'])
    json.dump(
        snaps, 
        open('snapshots/{}.json'.format(tweet_id), 'w'),
        default=str,
        indent=2
    )
