#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: get_as_prefixes.py
"""Get IP Prefixes for AS Number from https://bgp.he.net/"""

__author__ = "Jugal Kishore <me@devjugal.com>"

# Import Libraries
from bs4 import BeautifulSoup
import requests


# Function to extract prefixes from the table
def extract_prefixes_from_table(table) -> list[str]:
    """
    Extract prefixes from the given table.
    :param table: BeautifulSoup table element
    :return: List of prefixes
    """
    prefixes = []
    for row in table.find_all("tr"):
        details = row.find("td")
        if details:
            prefix = details.text.strip()
            prefixes.append(prefix)
    return prefixes


# Function to get IP Prefixes for AS Number
def get_as_prefixes(as_number: str, ip_version: str | None = None) -> list[str]:
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
    if ip_version == "4":
        table = soup.find("table", {"id": "table_prefixes4"})
        prefixes = extract_prefixes_from_table(table)
        return prefixes
    elif ip_version == "6":
        table = soup.find("table", {"id": "table_prefixes6"})
        prefixes = extract_prefixes_from_table(table)
        return prefixes
    elif ip_version == "all":
        table_v4 = soup.find("table", {"id": "table_prefixes4"})
        table_v6 = soup.find("table", {"id": "table_prefixes6"})
        prefixes = extract_prefixes_from_table(table_v4)
        prefixes.extend(extract_prefixes_from_table(table_v6))
        return prefixes
    return []


# Main function to run the script
if __name__ == "__main__":
    as_number = input("Enter AS Number (e.g., AS15169): ")
    if not as_number.startswith("AS"):
        as_number = "AS" + as_number
    ip_version = input("Enter IP Version (4/6/all): ")
    if ip_version not in ["4", "6", "all"]:
        print("Invalid IP Version. Please enter 4, 6, or 'all'.")
        exit(1)
    prefixes = get_as_prefixes(as_number, ip_version)
    if prefixes:
        print(f"IP Prefixes for {as_number}:")
        for prefix in prefixes:
            print(prefix)
    else:
        print("No prefixes found.")
