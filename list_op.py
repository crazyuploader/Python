#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"


def getAverage(total, numbers):
    average = total / numbers
    return round(average, 3)


print("///List Average, Sum Program///")
print("\nEnter Number of elements you want to have: ")
elements = int(input())
array, Sum = [], 0
average = 0.0
for i in range(elements):
    print("\nEnter", i, "element:")
    array.append(int(input()))

print("\nEntered Array: ", array)
for i in range(elements):
    Sum = array[i] + Sum

print("\nSum of all the elements =", Sum)
print("Average of all the elements =", getAverage(Sum, elements))
print("\nCreated by Jugal Kishore -- 2020")

# Run it online at https://python.jugalkishore.repl.run/
