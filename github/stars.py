#!/usr/bin/env python3
"""Displays GitHub Starred Repo(s) for a given user."""

from os import name
import subprocess
import requests

__author__ = "Jugal Kishore"


def clear():
    """
    Function to clear the console.
    """
    if name == "posix":
        subprocess.call("clear")


USER = str(input("Enter GitHub Username: "))
if not USER:
    print("Enter something!")
    exit(1)
clear()
URL = f"https://api.github.com/users/{USER}/starred"
got = requests.get(URL, timeout=30)
JSON = got.json()
print(f"Fetching Details for {USER}...")
if got.status_code == 200:
    clear()
    total_requests = got.headers["X-RateLimit-Limit"]
    remaining_requests = got.headers["X-RateLimit-Remaining"]
    print(f"GitHub API Used: {remaining_requests}/{total_requests}")
    print("")
    if len(JSON) == 0:
        print(f"GitHub User '{USER}' doesn't have any Starred Repo(s)")
        exit(0)
    print(f"Details for GitHub User '{USER}'")
    print(f"Last {len(JSON)} Starred Repo(s)")
    for repo in JSON:
        print("")
        print(f"         Name: {repo['name']}")
        print(f"    Full Name: {repo['full_name']}")
        print(f"  Description: {repo['description']}")
        print(f"     Language: {repo['language']}")
        print(f"        Stars: {repo['stargazers_count']}")
        print(f"    Clone URL: {repo['clone_url']}")
else:
    print("ERROR: Check username")
