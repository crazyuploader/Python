#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: get_latest_speedtest.py
"""Get latest binaries for Ookla Speedtest CLI"""

__author__ = "Jugal Kishore <me@devjugal.com>"


# Import Libraries
import json
import sys
from bs4 import BeautifulSoup
import requests


# Get HTML from speedtest.net website
print("Getting HTML from speedtest.net website...")
data = requests.get("https://www.speedtest.net/apps/cli", timeout=30)
print(f"HTTP Status Code: {data.status_code}")
if data.status_code != 200:
    print("Fatal: Error getting HTML file from: https://www.speedtest.net/apps/cli")
    print("Exiting!")
    sys.exit(1)
else:
    print("200 HTTP Status Code, continuing...")

# Souping
soup = BeautifulSoup(data.text, "html.parser")
links = soup.find(id="linux-flyout")
dicts = {}
for link in links:
    tag = link.find("a")
    dicts[tag.string] = tag.get("href")

print(json.dumps(dicts, indent=4))
