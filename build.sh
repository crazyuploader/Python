#!/usr/bin/env bash

# Colors
GREEN='\033[1;32m'
NC='\033[0m'
YELLOW='\033[1;33m'
MAGENTA='\033[1;35m'
RED='\033[0;31m'

# Main Script
clear
echo -e "${GREEN}" "Available Files -${NC}"
for f in *.py; do echo "$f"; done
echo ""
echo -e "Enter File Name -- ${YELLOW}Without Extension${NC}"
read -r fname
if [[ -f ${fname}.py ]]; then
    clear
    echo "Running $fname.py with Python3"
    sleep 2
    clear
    python3 "$fname.py"
else
    echo -e "${RED}" "File Does not Exist!${NC}"
    echo "Exiting!!"
    echo -e "${MAGENTA}" "K Thanks, Bye!${NC}"
    sleep 1
    clear
    exit
fi
echo ""
echo -e "${YELLOW}" "Show Source Code?${NC}"
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
        echo -e "${MAGENTA}" "K Thanks, Bye!${NC}"
        sleep 3
        exit
    fi
else
    clear
    echo -e "${MAGENTA}" "K Thanks, Bye!${NC}"
    sleep 2
    exit
fi