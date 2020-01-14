#!/usr/bin/env python3

print('///Program to Display Greater Number among three Number(s)///')
print('\nEnter First Number: ')
a = int(input())
print('\nEnter Second Number: ')
b = int(input())
print('\nEnter Third Number: ')
c = int(input())
if a > b:
    if a > c:
        print('\nGreatest Number = ',a)
    else:
        print('\nGreatest Number = ',c)
else:
    if b > c:
        print('\nGreatest Number = ',b)
    else:
        print('\nGreatest Number = ',c)