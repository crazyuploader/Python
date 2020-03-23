#!/usr/bin/env python3

__author__ = "Jugal Kishore & Akash Shiva"
__version__ = "1.0"


import random


print("///Hangman Game///")
print("")
print(" ~ You have 5 attempts to guess it right")
attempt = 5
win = 0
total = [
    [
        "Flower",
        "rose",
        "jasmine",
        "lilly",
        "tulip",
        "snowdrops",
        "lotus",
        "cherry",
        "sunflower",
    ],
    ["Animal", "dog", "cat", "elephant", "horse", "lion", "tiger", "cheetah", "bear",],
    [
        "Computer Part",
        "mouse",
        "keyoard",
        "monitor",
        "speaker",
        "processor",
        "motherboard",
        "pendrive",
    ],
    [
        "Body Part",
        "fingers",
        "toe",
        "leg",
        "hairs",
        "eyes",
        "nose",
        "ears",
        "lips",
        "hips",
        "mouth",
    ],
]
random_list = total[random.randint(0, len(total) - 1)]
random_word = random.choice(random_list[1::])
print("Hint: It's", random_list[0])
print("Picking Random word... Done!")
while attempt >= 1:
    print("")
    if attempt == 4:
        print("Hint 1: First letter is --->", random_word[0])
    elif attempt == 3:
        print("Hint 2: Second letter is --->", random_word[1])
    print("Enter {0} Name:".format(random_list[0]))
    input_word = input().lower().replace(" ", "")
    if input_word == random_word:
        win += 1
        break
    else:
        attempt -= 1
        print("")
        if attempt != 0:
            print("Wrong Guess! Attempts Remaining:", attempt)
if win > 0:
    print("")
    print("Indeed the Correct Answer is:", input_word)
else:
    print("All attempts are over, You are a looser :(")
print("\nCreated by Jugal Kishore & Akash Shiva -- 2020")
