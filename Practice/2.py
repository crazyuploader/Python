#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

print("Program to computer factorial of a number")
print("\nEnter a number: ")
number = int(input())
print("\nFactorial of {0} is = {1}".format(number, fact(number)))
