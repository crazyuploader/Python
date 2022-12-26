#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: get_sourceforge_mirrors.py
"""Get SourceForge mirror list"""

__author__ = "Jugal Kishore <me@devjugal.com>"


import json
import time
from bs4 import BeautifulSoup
import requests


def get_sourceforge_mirrors() -> list[dict]:
    URL = "https://sourceforge.net/p/forge/documentation/Mirrors/"
    response = requests.get(URL, timeout=10)
    if response.status_code != 200:
        print("HTTP response:", response.status_code)
        return
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.tbody
    mirror_list = []
    for row in table.find_all("tr"):
        details = row.find_all("td")
        mirror_list.append({"name": details[2].text,
                            "short_name": details[1].text,
                            "location": details[3].text})
    return mirror_list


if __name__ == "__main__":
    start_time = time.time()
    mirrors = get_sourceforge_mirrors()
    if mirrors:
        print(json.dumps(mirrors, indent=4))
    execution_time = round(time.time() - start_time, 2)
    print(f"Execution time: {execution_time} seconds")
