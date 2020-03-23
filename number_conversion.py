#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

print("///Program to convert Decimal to Binary Number///")
print("\nEnter a Number: ")
number = int(input())
array = []
while number > 0:
    array.append(int(number % 2))
    number = int(number / 2)
array.reverse()  # Reversing the list, since the remainders are required to be written from bottom to top
print("\nBinary Equivalent: ")
for x in array:
    print(x, end="")
print("\n\nCreated by Jugal Kishore -- 2020")
