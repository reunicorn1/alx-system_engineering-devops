#!/usr/bin/python3
"""
This is a script to returns a list containing the titles of all hot
articles for a given subreddit and prints a sorted count of given
keywords
"""
import requests


def count_words(subreddit, word_list, instances={}, after="",
                count=0):
    """
    This function returns a list containing the titles of all hot
    articles for a given subreddit and prints a sorted count of given
    keywords
    """
    headers = {"User-Agent": "Custom-header"}
    params = {"after": after, "count": count, "limit": 100}
    try:
        r = requests.get("https://www.reddit.com/r/{}/hot/.json".
                         format(subreddit), headers=headers,
                         params=params, allow_redirects=False)
        results = r.json()
        if not r.ok:
            return
    except Exception:
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(),
                           key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k.lower(), v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
