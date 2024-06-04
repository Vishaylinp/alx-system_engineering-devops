#!/usr/bin/python3
"""query the Reddit API and return num of subs"""
import requests


def number_of_subscribers(subreddit):
    """Number of sub"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 \
    Safari/537.36 Edg/125.0.0.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.RequestException:
        return 0
    except ValueError:
        return 0
