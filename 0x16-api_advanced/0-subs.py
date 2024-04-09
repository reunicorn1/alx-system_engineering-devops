#!/usr/bin/python3
"""
This is a script to retrieve the number of subscribers in a certain
subreddit
"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers in a certain
    subreddit
    """
    headers = {'User-Agent': 'Custom User Agent'}
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit), headers=headers,
                     allow_redirects=False)
    if (r.ok):
        return (r.json()['data']['subscribers'])
    return 0
