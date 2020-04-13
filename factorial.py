#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

print("///Program to Display Factorial of an Entered Number///")
print("\nEnter a Number: ")
a = input()
factorial = 1
for i in range(1, int(a) + 1):
    factorial = factorial * i
print("\nFactorial of {0} is = {1}".format(a, factorial))
print("\nCreated by Jugal Kishore -- 2020")

# Run it online at https://python.jugalkishore.repl.run/
