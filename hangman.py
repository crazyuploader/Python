#!/usr/bin/env python3

__author__ = "Jugal Kishore & Akash Shiva"
__version__ = "1.0"

import random


print("///Hangman Game///")
print("")
print("Hint: It's a flower")
print(" ~ You have 5 attempts to guess it right")
attempt = 5
win = 0
flowers = ["rose", "jasmine", "lilly", "tulip", "snowdrops", "lotus", "cherry", "sunflower"]
print("Picking Random Flower... Done!")
random_flower = random.choice(flowers)
while attempt >= 0:
    print("")
    if attempt == 4:
        print("Hint 1: First letter is --->", random_flower[0])
    if attempt == 3:
        print("Hint 2: Second letter is --->", random_flower[1])
    print("Enter Flower Name:")
    input_flower = input()
    if input_flower == random_flower:
        win += 1
        break
    else:
        attempt -= 1
        print("")
        print("Wrong Guess! Attempts Remaining:", attempt)
if win > 0:
    print("")
    print("Indeed the Correct Answer is:", input_flower)
else:
    print("All attempts are over, You are a looser :(")
print("\nCreated by Jugal Kishore & Akash Shiva -- 2020")

