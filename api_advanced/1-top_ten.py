#!/usr/bin/python3
"""Queries the Reddit API and prints the top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alx.task:v1.0"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print("None")
