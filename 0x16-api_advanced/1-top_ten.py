#!/usr/bin/python3
"""
This is a script to  prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    This function  prints the titles of the first 10 hot posts listed
    for a given subreddit.
    """
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 10}
    r = requests.get('https://www.reddit.com/r/{}/hot.json'.
                     format(subreddit), headers=headers,
                     params=params, allow_redirects=False)
    if (r.ok):
        for item in r.json()['data']['children'][:10]:
            print(item['data']['title'])
    else:
        print(None)
