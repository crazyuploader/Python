#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

print("///Gapful Number Program///")
num = int(input("\nEnter a 3 Digit Number: "))
n = 0
temp = num
while temp > 0:  # Determining the Number of Digits using a while loop.
    temp = int(temp / 10)
    n += 1
if n == 3:  # Condition to see if the entered number is a 3 digit number or not.
    b = num % 10
    a = num / 100
    a = int(a % 10)
    c = int(str(a) + str(b))
    if num % c == 0:
        print("\nEntered Number", num, "is a Gapful Number.")
    else:
        print("\nEntered Number", num, "is not a Gapful Number.")
elif n > 3:
    print("\nEntered Number", num, "is more than 3 Digits.")
else:
    print("\nEntered Number", num, "is less than 3 Digits.")
print("\nCreated by Jugal Kishore -- 2020")
