#!/usr/bin/env python3

__author__ = "Jugal Kishore & Akash Shiva"
__version__ = "1.0"


import os


def print_list(name, renamed_list):
    for f in renamed_list:
        print(name + " ---> " + f)


def rename_function():
    renamed_files = list()
    current_folder = os.curdir
    filepaths = os.listdir(current_folder)
    for name in filepaths:
        os.rename(name, name.replace(" ", "_"))
        renamed = name.replace(" ", "_")
        if name != renamed:
            renamed_files.append(renamed)
    print_list(name, renamed_files)
    if len(renamed_files) == 0:
        print("Nothing changed")


print("///File Renamer///\n")
print("Do you want to rename all the file/folders with spaces in them?")
print("'y' for yes, or anything to exit")
choice = input()
if choice == "y":
    rename_function()
else:
    print("Exiting!")
print("\nCreated by Jugal Kishore & Akash Shiva -- 2020")
