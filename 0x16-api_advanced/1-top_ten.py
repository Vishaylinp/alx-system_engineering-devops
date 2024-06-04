#!/usr/bin/python3
"""print Top ten"""
import requests


def top_ten(subreddit):
    """Top ten"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 \
    Safari/537.36 Edg/125.0.0.0"}

    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(count.get("data").get("title")) for count in results.get("children")]
