#!/usr/bin/python3
"""0. How many subs?"""


import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/<subreddit>/about.json'.format(subreddit)

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
