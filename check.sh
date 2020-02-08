#!/usr/bin/env bash

# Colors
GREEN='\033[1;32m'
NC='\033[0m'
YELLOW='\033[1;33m'

echo ""
echo -e "${GREEN}" "Checking all the files with Pyflakes ${NC}"
for f in *.py; do echo ""; echo "Checking $f"; pyflakes "$f"; done
echo ""
echo -e "${GREEN}" "Checking all the files with Flake8 ${NC}"
for f in *.py; do echo ""; echo "Checking $f"; echo "$(flake8 "${f}" --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics) errors"; done
echo ""
echo -e "${YELLOW}" "Done! ${NC}"