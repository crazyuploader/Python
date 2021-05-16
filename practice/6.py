#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

import math
def Calculate(data):
    list = []
    C = 50
    H = 30
    for number in data:
        list.append(str(round(math.sqrt((2*C*int(number)/H)))))
    print(",".join(list))

string = input("Input Number(s): ")
Calculate(string.split(","))
