#!/usr/bin/env python3

__author__ = "Jugal Kishore & Akash Shiva"
__version__ = "1.0"


import os


def rename_function():
    current_folder = os.curdir
    filepaths = os.listdir(current_folder)
    num = 0
    for name in filepaths:
        os.rename(name, name.replace(" ", "_"))
        renamed = name.replace(" ", "_")
        if name != renamed:
            num += 1
            print(name + " ---> " + renamed)
    if num == 0:
        print("Nothing changed")


def rename_to_lower():
    current_dir = os.curdir
    file_name = os.listdir(current_dir)
    for name in file_name:
        os.rename(name, name.lower())
        renamed = name.lower()
        if name != renamed:
            print(name + " ---> " + renamed)


print("///File Renamer///\n")
print("1. Space Remover")
print("2. File Name Upper to Lower")
print("3. Space Remover + File Name Upper to Lower")
print("Anything to exit")
choice = input()
if choice == "1":
    rename_function()
elif choice == "2":
    rename_to_lower()
elif choice == "3":
    rename_function()
    rename_to_lower()
else:
    print("Exiting!")
print("\nCreated by Jugal Kishore & Akash Shiva -- 2020")

# Run it online at https://python.jugalkishore.repl.run/
