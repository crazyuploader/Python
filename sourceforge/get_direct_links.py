#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: get_direct_links.py
"""Get direct links from SourceForge download URL"""

__author__ = "Jugal Kishore <me@devjugal.com>"


import sys
import re
import time
import requests
from get_mirrors import get_sourceforge_mirrors


def get_links(url):
    """
    Get list of direct links from SourceForge for a specific URL
    """
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url
    mirror_list, _ = get_sourceforge_mirrors()
    try:
        final = requests.get(url, allow_redirects=True, stream=True, timeout=10)
    except Exception as error:
        print(error)
        return None
    if final.status_code != 200:
        return None
    direct_links = []
    for mirror in mirror_list:
        hostname_prefix = mirror["name"].lower()
        regex_replace_pattern = rf"{hostname_prefix}.dl"
        mirror_url = re.sub(r"\w+\.dl", regex_replace_pattern, final.url)
        try:
            response = requests.head(mirror_url, allow_redirects=True, timeout=2)
            size = response.headers.get("Content-Length")
            if response.status_code == 200 and int(size) > 0:
                direct_links.append(response.url)
        except Exception:
            continue
    return [*set(direct_links)]


if __name__ == "__main__":
    start_time = time.time()
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
    execution_time = round(time.time() - start_time, 2)
    print(f"Execution time: {execution_time} seconds")
