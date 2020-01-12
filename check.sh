#!/usr/bin/env bash

echo ""
echo "Checking all the files with Pyflakes"
for f in $(ls *.py); do echo; echo "Checking $f"; pyflakes $f; done
