#!/usr/bin/env python3

__author__ = 'Jugal Kishore'
__version__ = '1.0'

print("///Program to Check Prime Number///")
number = int(input("\nEnter a Number: "))
m = 0
for n in range(1, int(number + 1)):
    if number % n == 0:
        m += 1
if m == 2:
    print("\nEntered Number ", number, " is a Prime Number.")
else:
    print("\nEntered Number ", number, "is not a Prime Number.")
print("\nCreated by Jugal Kishore -- 2020")
