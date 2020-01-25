#!/usr/bin/env python3

print('///Program to Display Average of Entered n Number(s)///')
number ,total = [], 0
print('\nEnter Number of Numbers you want to get Average of: ')
num = int(input())
for x in range(num):
    number.append(int(input()))
total = sum(number)
print(total)
average = total / num
print('\nAverage of Entered Number(s) is = ', average)
print('\nCreated by Jugal Kishore -- 2020')
