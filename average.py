#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

print("///Program to Display Average of Entered n Number(s)///")
number, total = [], 0
print("\nEnter Number of Numbers you want to get Average of: ")
num = int(input())
print("\nEnter ", num, " Number(s): ")
for x in range(num):
    number.append(int(input()))
total = sum(number)
average = total / num
print(
    "\nAverage of Entered Number(s) is = ", round(average, 3)
)  # Limiting Decimal Precision to 3 Digits
print("\nCreated by Jugal Kishore -- 2020")
