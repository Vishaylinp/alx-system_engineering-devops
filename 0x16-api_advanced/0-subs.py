#!/usr/bin/python3
"""query the Reddit API and return num of subs"""
import requests


def number_of_subscribers(subreddit):
    """Number of sub"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 \
    Safari/537.36 Edg/125.0.0.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
