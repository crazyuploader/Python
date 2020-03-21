#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

import string
import random


def newline():
    print("")


print("///Random Password Generator///")
newline()
letters = string.ascii_letters + string.digits + string.punctuation
length = len(letters) - 1
print(" ~ A secure password should always be of at least 8 characters")
newline()
print("Enter Length of Password:")
required_password = int(input())
newline()
for i in range(0,3):
    generated_password = ""
    required = required_password
    while required > 0:
        random_number = random.randint(0, length)
        generated_password = generated_password + letters[random_number]
        required -= 1
    print("Generated Password:", generated_password)
newline()
print("Created by Jugal Kishore -- 2020")
