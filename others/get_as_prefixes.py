#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: get_as_prefixes.py
"""Get IP Prefixes for AS Number from https://bgp.he.net/"""

__author__ = "Jugal Kishore <me@devjugal.com>"

# Import Libraries
from bs4 import BeautifulSoup
import requests

def get_as_prefixes(as_number: str) -> list[str]:
    """
    Get IP Prefixes for AS Number from https://bgp.he.net/
    :param as_number: AS Number
    :return: List of IP Prefixes
    """
    url = f"https://bgp.he.net/{as_number}"
    response = requests.get(url, timeout=30)
    if response.status_code != 200:
        print("HTTP response:", response.status_code)
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    prefixes = []
    table = soup.find("table", {"id": "table_prefixes4"})
    if table:
        for row in table.find_all("tr"):
            details = row.find("td")
            if details:
                prefix = details.text.strip()
                prefixes.append(prefix)
        return prefixes

if __name__ == "__main__":
    as_number = input("Enter AS Number (e.g., AS15169): ")
    if not as_number.startswith("AS"):
        print("Invalid AS Number. Please enter a valid AS Number (e.g., AS15169).")
        exit(1)
    prefixes = get_as_prefixes(as_number)
    if prefixes:
        print(f"IP Prefixes for {as_number}:")
        for prefix in prefixes:
            print(prefix)
    else:
        print("No prefixes found.")
