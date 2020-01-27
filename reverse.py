#!/usr/bin/env python3

__author__  = 'Jugal Kishore'
__version__ = '1.0'

print("///Program to Display Reverse Number of an Entered Number///")
print("\nEnter a Number: ")
a = int(input())
r = 0
t = 0
while int(a) > 0:
    r = int(a % 10)
    t = t * 10 + r
    a = int(a / 10)
print("\nReversed Number = ", t)
print("\nCreated by Jugal Kishore -- 2020")
