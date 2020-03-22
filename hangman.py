#!/usr/bin/env python3

__author__ = "Jugal Kishore & Akash Shiva"
__version__ = "1.0"

import random


print("///Hangman Game///")
print("")
print(" ~ You have 5 attempts to guess it right")
attempt = 5
win = 0
flower = ["rose", "jasmine", "lilly", "tulip", "snowdrops", "lotus", "cherry", "sunflower"]
animal = ["dog", "cat", "elephant", "horse", "lion", "tiger", "cheetah", "bear"]

random_list = random.randint(1, 2)
if random_list == 1:
    chosen = "flower"
    temp = flower
elif random_list == 2:
    chosen = "animal"
    temp = animal
print("Hint: It's", chosen)
print("Picking Random {0}... Done!".format(chosen))
random_list = random.choice(temp)
while attempt >= 1:
    print("")
    if attempt == 4:
        print("Hint 1: First letter is --->", random_list[0])
    if attempt == 3:
        print("Hint 2: Second letter is --->", random_list[1])
    print("Enter {0} Name:".format(chosen))
    input_flower = input().lower()
    if input_flower == random_list:
        win += 1
        break
    else:
        attempt -= 1
        print("")
        if attempt != 0:
            print("Wrong Guess! Attempts Remaining:", attempt)
if win > 0:
    print("")
    print("Indeed the Correct Answer is:", input_flower)
else:
    print("All attempts are over, You are a looser :(")
print("\nCreated by Jugal Kishore & Akash Shiva -- 2020")
