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
    print_it("")

# Souping
soup = BeautifulSoup(data.text, "html.parser")

# Get links for Linux
linux_links = soup.find(id="linux-flyout")
linux_url = {}
for link in linux_links:
    tag = link.find("a")
    linux_url[tag.string] = tag.get("href")

# Get links for macOS & Windows
other_links = soup.find_all("a", {"class": "btn btn-sm btn-outline btn-full-width"})
other_url = {}
for link in other_links:
    OS = link.text.split(" ")[-1]
    other_url[OS] = link.get("href")

all_links = {"linux": linux_url, "others": other_url}
print(json.dumps(all_links, indent=4))
