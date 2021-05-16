#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"


def create_dict(integer):
    dictionary = {}
    temp = 1
    while temp <= integer:
        dictionary[temp] = temp * temp
        temp += 1
    return dictionary


print("Enter an Integer")
integer = int(input())
if integer > 0:
    print(create_dict(integer))
else:
    print("Integer should be greater than 1!")
