#!/usr/bin/env python3

__author__ = "Jugal Kishore & Akash Shiva"
__version__ = "1.0"


import random


print("///Rock Paper Scissor Game///")
while True:
    print("")
    print("1. for Rock")
    print("2. for Paper")
    print("3. for Scissor")
    print("4. to exit")
    print("")
    print("Enter your choice:")
    total = ["Rock", "Paper", "Scissor"]
    try:
        human_put = int(input()) - 1
    except ValueError:
        print("Not an integer")
        break
    comp_put = random.randint(0, 2)
    if human_put == 0:
        choice = "Rock"
    elif human_put == 1:
        choice = "Paper"
    elif human_put == 2:
        choice = "Scissor"
    elif human_put == 3:
        print("Bye Bye")
        break
    print("")
    print("Your Choice: ", choice)
    print("")
    print("Computer Choice: ", total[comp_put])
    print("")
    if human_put == comp_put:
        print("It's a Tie")
    elif (human_put==0 and comp_put==1) or (human_put==1 and comp_put==2) or (human_put==2 and comp_put==0):
        print("You Lost!")
    elif (comp_put==0 and human_put==1) or (comp_put==1 and human_put==1) or (comp_put==2 and comp_put==0):
        print("You Won!")
print("\nCreated by Jugal Kishore & Akash Shiva -- 2020")