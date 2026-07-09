#!/usr/bin/python3
"""Module to query the Reddit API and print titles of top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    params = {"limit": 10}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        try:
            children = response.json().get("data", {}).get("children", [])
            if not children:
                print("None")
                return
            for post in children:
                print(post.get("data", {}).get("title"))
        except Exception:
            print("None")
    else:
        print("None")
