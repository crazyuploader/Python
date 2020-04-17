#!/usr/bin/env bash

# Colors
GREEN="\033[1;32m"
NC="\033[0m"
YELLOW="\033[1;33m"
RED="\033[0;31m"

echo ""
echo -e "${GREEN}" "Available files -${NC}"
LIST_FILES="$(find . -path ./.git -prune -o -name '*.py' -print | sed 's|^./||')"
FILES=0
for file in ${LIST_FILES}; do
    echo "$file"
    ((FILES = FILES + 1))
done
echo ""
echo -e "${GREEN}Python Linter ${NC}"
echo ""
echo -e "${YELLOW}Checking all the files with Pyflakes${NC}"
echo ""
for file in ${LIST_FILES}; do
    echo "Checking '${file}'"
    pyflakes "${file}">> /dev/null 2>&1
    ERROR_CODE="$?"
    if [[ ${ERROR_CODE} != "0" ]]; then
        echo ""
        echo -e "${RED}$(pyflakes "${file}")${NC}"
    fi
done
echo ""
echo -e "${YELLOW}Checking all the files with Flake8 ${NC}"
echo ""
for file in ${LIST_FILES}; do
    echo "Checking '${file}'"
    echo "$(flake8 "${file}" --count --ignore=C901 --exit-zero --max-complexity=10 --max-line-length=127 --statistics) errors"
done
echo ""
echo -e "Number of Python Files Checked: ${GREEN}${FILES}${NC}"
