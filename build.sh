#!/usr/bin/env bash

clear
echo "Available Files -"
for f in *.py; do echo "$f"; done
echo ""
echo "Enter File Name without -- Extension"
read -r fname
if [[ -f ${fname}.py ]]; then
    clear
    echo "Running $fname.py with Python3"
    sleep 2
    clear
    python3 "$fname.py"
else
    echo "File Does not Exist"
    echo "Exiting!!"
    sleep 1
    clear
    exit
fi
echo ""
echo "Show Source Code?"
echo ""
echo "'y' for yes and anything else for no"
read -r temp
if [[ $temp = "y" ]]; then
    clear
    cat "${fname}.py"
    sleep 5
    echo ""
    echo "Press 'y' to Exit"
    read -r temp
    if [[ $temp = "y" ]]; then
        clear
        echo "K Thanks, Bye!"
        sleep 3
        exit
    fi
else
    clear
    echo "K Thanks, Bye!"
    sleep 2
    exit
fi