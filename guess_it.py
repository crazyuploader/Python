#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"

from random import randint


def newline():
    print("")


print("///Random Number Guessing Game///")
newline()
print("Rules: -")
newline()
print(" ~ This program will generate a random integer between 0 and 20")
print(" ~ You will get three attempts to guess it")
print(" ~ If you can't guess in three attempts, it will exit")
attempt = 3
newline()
while attempt > 0:
    if attempt == 3:
        random_number = randint(0, 20)
        print("Integer generated successfully")
    newline()
    print("Available Attempts: {0}".format(attempt))
    newline()
    print("Enter an integer:")
    try:
        number = int(input())
    except ValueError:
        newline()
        print("Not an integer")
        attempt -= 1
        continue
    if number == random_number:
        newline()
        print("You guessed it right!")
        newline()
        print("Random generated was indeed =", random_number)
        newline()
        print("Play Again?")
        print(" ~ 'y' for yes, anything else to exit")
        temp = input()
        if temp == "y":
            attempt = 3
            continue
        else:
            newline()
            print("Exiting!")
            break
    elif number > random_number:
        if number > 20 or number < 0:
            newline()
            print("The entered number should be in range [0,20]")
        else:
            newline()
            print(
                "Uh-huh, you guessed a little more than the generated number, try again"
            )
    else:
        if number > 20 or number < 0:
            newline()
            print("The entered number should be in range [0,20]")
        else:
            newline()
            print(
                "Uh-huh, you guessed a little less than the generated number, try again"
            )
    attempt -= 1
    if attempt == 0:
        newline()
        print("Ran out of attempts")
        print("Exiting!")
newline()
print("Created by Jugal Kishore -- 2020")
