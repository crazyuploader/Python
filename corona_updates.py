#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

import requests


def newline():
    print("")


def get_data(URL):
    response = requests.get(URL)
    json_data = response.json()
    if response.status_code != 200:
        return "Not Found!"
    return json_data


API_GITHUB = "https://github.com/NovelCOVID/API"
BASE_URL = "https://corona.lmao.ninja/v2/"
ALL_URL = BASE_URL + "all"
fetched = get_data(ALL_URL)

print("///Corona Virus Update///")
newline()
print("Total No. of Cases:", "\n", fetched["cases"])
newline()
print("Critical Cases:", "\n", fetched["critical"])
newline()
print("No. of Cases Today:", "\n", fetched["todayCases"])
newline()
print("Total Deaths:", "\n", fetched["deaths"])
run = True
while run:
    newline()
    print("Want Country Data?")
    temp = input("Enter 'yes' for continue or anything else to exit\n")
    newline()
    if temp == "yes":
        country = input("Enter Country Name:\n")
        country_URL = BASE_URL + "countries/" + country
        got = get_data(country_URL)
        if got != "Not Found!":
            newline()
            print("Stats for", country)
            newline()
            print("Total cases:    ", got["cases"])
            print("Cases Today:    ", got["todayCases"])
            print("Total Deaths:   ", got["deaths"])
            print("Deaths Today:   ", got["todayDeaths"])
            print("Total Recovered:", got["recovered"])
            print("Critical Cases: ", got["critical"])
        else:
            newline()
            print("Country not found!")
    else:
        run = False
print("API Used:", API_GITHUB)
print("\nCreated by Jugal Kishore -- 2020")

# Run it online at https://python.jugalkishore.repl.run/
