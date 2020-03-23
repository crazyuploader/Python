#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

import re

run = True
print("///Advanced Calculator///\n")
while run:
    print("Type 'quit' to exit\n")
    equation = input("Kindly enter an equation\n")
    if equation == "quit":
        print("Uh-Oh, you decided to exit.")
        print("Exiting!")
        break
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', "", equation)
        equation = eval(equation)
        print(equation)
print("\nCreated by Jugal Kishore -- 2020")
