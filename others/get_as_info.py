#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: get-as-info.py
"""Get AS Info for a given ASN"""

__author__ = "Jugal Kishore <me@devjugal.com>"


import sys
import time
try:
    import requests
except ImportError:
    print("Please install the required modules")
    sys.exit(1)


# Variable(s)
RIPE_STAT_API_ENDPOINT = "https://stat.ripe.net/data/as-overview/data.json?resource=AS"


def get_param() -> list[str]:
    """
    Get the ASN from the command line
    """
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <ASN> ...")
        print(f"Example: {sys.argv[0]} 9498")
        sys.exit(1)
    return sys.argv[1:]


def get_as_info(as_number: str):
    """
    Get AS info from RIPE Stat API
    """
    if "AS" in as_number:
        as_number = as_number.replace("AS", "")
    url = RIPE_STAT_API_ENDPOINT + as_number
    fetched_data = requests.get(url, timeout=30)
    if fetched_data.status_code != 200:
        print(f"Invalid AS Number: {as_number}")
        print(f"API URL: {url}")
        sys.exit(1)
    return fetched_data.json()


if __name__ == "__main__":
    start_time = time.time()
    print("AS Info for ->", get_param())
    print("")
    for AS_NUMBER in get_param():
        as_info = get_as_info(AS_NUMBER)
        asn = "AS" + as_info['data']['resource']
        as_holder = as_info['data']['holder']
        print(f"  ASN Info: AS{asn}")
        print(f"ASN Holder: {as_holder}")
        print("")
    print(f"--- Took {round(time.time() - start_time, 2)} seconds ---")
