#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

print("///Program to Display factor(s) of an Entered Number///")
print("\nEnter a Number: ")
number = int(input())
print("")
for x in range(1, int(number + 1)):
    if int(number) % x == 0:
        print("{0} is divisble by {1}".format(number, x))
print("\nCreated by Jugal Kishore -- 2020")

# Run it online at https://python.jugalkishore.repl.run/
