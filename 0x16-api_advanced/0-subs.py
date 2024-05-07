import requests
"""0. How many subs?"""

def number_of_subscribers(subreddit):
    try:    
        headers = {'User-Agent': 'my-app/0.0.1'}
        url = f'https://www.reddit.com/r/<subreddit>/about.json'

        response = requests.get(url, headers=headers)
        response_json = response.json()  
    
        subscribers = response_json['data']['subscribers']
        return subscribers
    
    except Exception as e:
        return 0
