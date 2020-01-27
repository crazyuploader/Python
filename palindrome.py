#!/usr/bin/env python3

__author__ = 'Jugal Kishore'
__version__ = '1.0'

print("///Program to Check if Entered Number is Palindrome or not///")
print("\nEnter a Number: ")
a = int(input())
pal = int(a)
c, b = 0, 0
while int(a) > 0:
    c = int(a % 10)
    b = b * 10 + c
    a = int(a / 10)
if pal == b:
    print("\nEntered is a Palindrome Number.")
else:
    print("Entered Number is not a Palindrome Number.")
