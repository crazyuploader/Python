#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: get-as-info.py
"""Get AS Info for a given ASN"""

__author__ = "Jugal Kishore <me@devjugal.com>"


import requests
import sys
import time


def get_param() -> list[str]:
    if len(sys.argv) < 2:
        print("Usage: %s <ASN> ..." % sys.argv[0])
        print("Example: %s 9498" % sys.argv[0])
        sys.exit(1)
    return sys.argv[1:]


def get_as_info(AS_NUMBER: str):
    if AS_NUMBER.__contains__("AS"):
        AS_NUMBER = AS_NUMBER.replace("AS", "")
    url = "https://stat.ripe.net//data/as-overview/data.json?resource=AS" + AS_NUMBER
    r = requests.get(url)
    if r.status_code != 200:
        print("Invalid AS Number: %s" % AS_NUMBER)
        print("API URL: %s" % url)
        sys.exit(1)
    return r.json()


if __name__ == "__main__":
    start_time = time.time()
    print("AS Info for ->", get_param())
    print("")
    for AS_NUMBER in get_param():
        as_info = get_as_info(AS_NUMBER)
        print("  ASN Info: AS%s" % as_info['data']['resource'])
        print("ASN Holder: %s" % as_info['data']['holder'])
        print("")
    print("--- Took %s seconds ---" % round(time.time() - start_time, 2))
