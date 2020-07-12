#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"


import sys
import os
import subprocess
import time


def newline():
    print("")


def clear_screen():
    os.system("cls")


def my_exit():
    clear_screen()
    print("K Thanks Bye!")
    time.sleep(2)
    exit(0)

files = []
if os.name != "nt":
    subprocess.call(["bash", "./build.sh"])
    exit
else:
    clear_screen()
    print("Python version:", sys.version)
    newline()
    current_directory = os.curdir
    print(" Available Files -\n")
    number = 0
    for file in os.listdir(current_directory):
        if file.endswith(".py"):
            if number < 9:
                print("{0}  — {1}".format(number + 1, file))
            else:
                print("{0} — {1}".format(number + 1, file))
            files.append(file)
            number += 1
    print("\t\tTotal Files -", number)
    newline()
    print("Kindly enter file number: (Enter 0 to exit)")
    file_to_execute = int(input())
    fname = files[file_to_execute - 1]
    if file_to_execute == 0:
        newline()
        print("Off you go!")
        exit(0)
    else:
        clear_screen()
        print("Running {0} with default Python...".format(fname))
        time.sleep(2)
        clear_screen()
        subprocess.call(["python", fname])
        newline()
        print("Show Source Code?")
        print("\n'y' for yes and anything else for no")
        temp = str(input())
        if temp == "y":
            clear_screen()
            print("///Source Code for {0} ///\n".format(fname))
            file = open(fname, "r")
            print(file.read())
            file.close()
            time.sleep(5)
            print("\nEnter 'y' to exit")
            temp = input()
            if temp == "y":
                my_exit()
            else:
                clear_screen()
                print("Crashed...")
                i = 10
                while (i > 0):
                    print(i)
                    time.sleep(0.1)
                    i -= 1
                print("Bye!")
                exit(0)
        else:
            my_exit()
    