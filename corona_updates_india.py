#!/usr/bin/env python3

__author__ = "Jugal Kishore & Akash Shiva"
__version__ = "1.0"

import requests
import os
from bs4 import BeautifulSoup


URL = "https://www.mohfw.gov.in/"
get = requests.get(URL)
soup = BeautifulSoup(get.text, "html.parser")

state = []
cases = []
recovered = []
deaths = []

for i in range(1, 36):
    state.append((soup.find("table").find_all("tr")[i].find_all("td")[1].contents[0]))
    cases.append((soup.find("table").find_all("tr")[i].find_all("td")[2].contents[0]))
    recovered.append(
        (soup.find("table").find_all("tr")[i].find_all("td")[3].contents[0])
    )
    deaths.append((soup.find("table").find_all("tr")[i].find_all("td")[4].contents[0]))

output = "State, Cases, Recovered, Deaths\n"
file = open("data.csv", "w")
for i in range(0, 35):
    output = (output + "\n" + "{0}, {1}, {2}, {3}".format(state[i], cases[i], recovered[i], deaths[i]))
file.write(output)
file.close()
os.system("csvtomd data.csv")
os.system("rm data.csv")
print("")
print("Website Scrapped:", URL)
print("\nCreated by Jugal Kishore & Akash Shiva -- 2020")

# Run it online at https://python.jugalkishore.repl.run/
