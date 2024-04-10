#!/usr/bin/python3
"""
This is a script to returns a list containing the titles of all hot
articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    This function prints the titles of all hot posts listed
    for a given subreddit.
    """
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}
    try:
        r = requests.get('https://www.reddit.com/r/{}/hot.json'.
                         format(subreddit), headers=headers,
                         params=params, allow_redirects=False)
        if r.ok:
            data = r.json()['data']['children']
            if not data:
                return hot_list
            for item in data:
                hot_list.append(item['data']['title'])
            after = data[-1]['data']['name']
            return recurse(subreddit, hot_list, after)
        else:
            return None
    except Exception as e:
        return None
