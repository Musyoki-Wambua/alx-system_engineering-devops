#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit,
    handling non-existent subreddits gracefully.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print(f"Subreddit '{subreddit}' does not exist.")
        return 0
    else:
        results = response.json().get("data")
        subscribers = results.get("subscribers")
        print(f"Subscribers:", subscribers)
        return
