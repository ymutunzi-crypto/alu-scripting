#!/usr/bin/python3
"""Queries the Reddit API and prints the top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alx.task1:v1.0 (by /u/ymutunzi-crypto)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print("None")
