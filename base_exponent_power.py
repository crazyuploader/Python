#!/usr/bin/env python3

print('///Program to Calculate Power of a Number///')
print('Enter Base: ')
base = int(input())
print('Enter Exponent: ')
exponent = int(input())
result = 1
while exponent != 0:
    result *= base
    exponent -= 1
print('Answer: ', result)
print('\nCreated by Jugal Kishore -- 2020')
