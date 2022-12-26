#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: get_direct_links.py
"""Get direct links from SourceForge download URL"""

__author__ = "Jugal Kishore <me@devjugal.com>"


import sys
import re
import requests


def get_links(url):
    mirror_list = requests.get("https://api.devjugal.com/sourceforge_mirrors", timeout=10).json()["mirrors"]
    final_url = requests.get(url, allow_redirects=True, stream=True, timeout=10)
    if final_url.status_code != 200:
        return
    direct_links = []
    for mirror in mirror_list:
        regex = f"{mirror['short_name']}.dl"
        mirror_url = re.sub(r"\w+\.dl", regex, final_url.url)
        try:
            response = requests.get(mirror_url, allow_redirects=True, stream=True, timeout=30)
            if response.status_code == 200:
                direct_links.append(response.url)
        except Exception:
            continue
    return direct_links


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No download URL is provided!!")
        exit(1)
    url = sys.argv[1]
    links = get_links(url)
    if links:   
        for link in links:
            print(link)
    else:
        print("No links found, check download URL")
