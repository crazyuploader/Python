#!/usr/bin/env bash

clear
echo "Available Files -"
for f in *.py; do echo "$f"; done
echo
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
echo "K Thanks, Bye!"
