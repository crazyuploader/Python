#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

def Add_2(x, y):
    return x + y


print("///Program to Add two Number(s)///")
print("\nEnter First Number: ")
a = input()
print("\nEnter Second Number: ")
b = input()
Sum = Add_2(int(a), int(b))
print("\nAddition of Entered Number(s) {0} and {1} is = {2}".format(a, b, Sum))
print("\nCreated by Jugal Kishore -- 2020")

# Run it online at https://python.jugalkishore.repl.run/
