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


def print_it(string) -> None:
    """Function to print to stdout"""

    # If --silent argument is provided, skip printing most of the stuff
    if "--silent" not in sys.argv[1:]:
        print(string)


# Get HTML from speedtest.net website
print_it("Getting HTML from speedtest.net website...")
data = requests.get("https://www.speedtest.net/apps/cli", timeout=30)
print_it(f"HTTP Status Code: {data.status_code}")
if data.status_code != 200:
    print_it("Fatal: Error getting HTML file from: https://www.speedtest.net/apps/cli")
    print_it("Exiting!")
    sys.exit(1)
else:
    print_it("200 HTTP Status Code, continuing...")

# Souping
soup = BeautifulSoup(data.text, "html.parser")
links = soup.find(id="linux-flyout")
dicts = {}
for link in links:
    tag = link.find("a")
    dicts[tag.string] = tag.get("href")

print(json.dumps(dicts, indent=4))
print_it(sys.argv[1:])
