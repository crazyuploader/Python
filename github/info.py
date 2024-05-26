#!/usr/bin/env python3
"""Displays information about a GitHub user."""

import requests

__author__ = "Jugal Kishore <me@devjugal.com>"


GITHUB_API_URL = "https://api.github.com/users/"

print("Enter GitHub Username: ")
USER = input()
if not USER:
    print("Enter something!")
    exit(1)

print(f"Fetching Details for {USER}...")
req = requests.get(GITHUB_API_URL + USER, timeout=30)
json = req.json()
if req.status_code != 200:
    print("ERROR: Check username")
    print("Debug Message:", req.text)
    exit(1)
else:
    print("")
    print("Username: " + json["login"])
    print("Name: " + json["name"])
    print("Location: " + json["location"])
    print("Followers: " + str(json["followers"]))
    print("Following: " + str(json["following"]))
    print("Public Repos: " + str(json["public_repos"]))
    print("Bio: " + json["bio"])
    print("URL: " + json["html_url"])
    print("Last Repo: " + json["repos_url"])
    print("User Created: " + json["created_at"])
