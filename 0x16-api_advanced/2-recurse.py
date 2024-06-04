#!/usr/bin/python3
"""All hot posts"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Return a list of titles."""
    url = "https://www.reddit.com/r/{}/hot/json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 \
    Safari/537.36 Edg/125.0.0.0"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allowed_redirections=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count = count + results.get("distribute")
    for i in results.get("children"):
        h_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, h_list, after, count)
    return h_list
