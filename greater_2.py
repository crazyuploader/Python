#!/usr/bin/env python3

print("///Program to Display Greater Number///")
print("\nEnter First Number: ")
a = int(input())
print("\nEnter Second Number: ")
b = int(input())
if a > b:
    print("\nGreater Number between {0} and {1} is = {2}.".format(a, b, a))
elif b > a:
    print("\nGreater Number between {0} and {1} is = {2}.".format(a, b, b))
else:
    print("\n{0} and {1} are Equal!".format(a, b))
print("\nCreated by Jugal Kishore -- 2020")
