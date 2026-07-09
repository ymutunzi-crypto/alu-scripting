#!/usr/bin/python3
"""Module to query the Reddit API and print titles of top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-App/1.0"}
    params = {"limit": 10}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        children = response.json().get("data", {}).get("children", [])
        for post in children:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
