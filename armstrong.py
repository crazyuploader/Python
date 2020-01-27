#!/usr/bin/env python3

__author__ = 'Jugal Kishore'
__version__ = '1.0'

print("///Program to Check Whether or not Entered Number is Armstrong.///")
number = int(input("\nEnter a Number: "))
temp = number
total = 0
while number > 0:
    a = number % 10
    total = total + int(a * a * a)
    number = int(number / 10)
if (temp == total):
    print("\nEntered Number ", temp, " is an Armstrong Number.")
else:
    print("\nEntered Number ", temp, " is not an Armstrong Number.")
print("\nCreated By Jugal Kishore -- 2020")
