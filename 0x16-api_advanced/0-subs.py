#!/usr/bin/python3
"""0. How many subs?"""

import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    try:    
        headers = {'User-Agent': 'my-app/0.0.1'}
        url = f'https://www.reddit.com/r/<subreddit>/about.json'.format(subreddit)

        response = requests.get(url, headers=headers)
        response_json = response.json()  
    
        subscribers = response_json['data']['subscribers']
        return subscribers
    
    except Exception as e:
        return 0
