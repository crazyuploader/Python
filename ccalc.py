#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.1"

import re

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
            previous = eval(str(previous) + equation)
print("\nCreated by Jugal Kishore -- 2020")
