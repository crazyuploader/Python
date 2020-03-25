#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

print("///Program to Display Sum of its Digit(s)///")
number = int(input("\nEnter a Number: "))
grand = 0
temp = number
while number > 0:
    b = number % 10
    grand = grand + b
    number = int(number / 10)
print("\nSum of Entered Number ", temp, " is = ", grand)
print("\nCreated By Jugal Kishore -- 2020")
