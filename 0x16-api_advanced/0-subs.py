#!/usr/bin/python3
"""query the Reddit API and return num of subs"""
import requests


def number_of_subscribers(subreddit):
    """Number of sub"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "MyUniqueRedditApp/0.0.1"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
