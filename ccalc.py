#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.1"

import re

def find_sign():
    global equation
    var = 0
    signs = ["+", "-", "*", "/", "%"]
    number_of_signs = len(signs)
    for value in signs:
        if equation.find(value) == -1:
            var += 1
    if var != number_of_signs:
        return True
    else:
        return False


previous = 0
run = True
print("///Advanced Calculator///\n")
print("Type 'quit' to exit\n")
while run:
    if previous == 0:
        equation = input("Enter equation:\n")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Uh-Oh, you decided to exit.")
        print("Exiting!")
        break
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            if find_sign() == True:
                previous = eval(str(previous) + equation)
            else:
                print("Try Again! You forgot to include a mathematical sign")
print("\nCreated by Jugal Kishore -- 2020")
