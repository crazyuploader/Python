#!/usr/bin/env python3

__author__ = 'Jugal Kishore'
__version__ = '1.0'

print("///Program to Display Greater Number among three Number(s)///")
print("\nEnter First Number: ")
a = int(input())
print("\nEnter Second Number: ")
b = int(input())
print("\nEnter Third Number: ")
c = int(input())
if a > b:
    if a > c:
        print("\nGreatest Number among {0}, {1}, {2} is = {3}".format(a, b, c, a))
    else:
        print("\nGreatest Number among {0}, {1}, {2} is = {3}".format(a, b, c, c))
else:
    if b > c:
        print("\nGreatest Number among {0}, {1}, {2} is = {3}".format(a, b, c, b))
    else:
        print("\nGreatest Number among {0}, {1}, {2} is = {3}".format(a, b, c, c))
print("\nCreated by Jugal Kishore -- 2020")
