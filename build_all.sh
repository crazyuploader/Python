#!/usr/bin/env bash

echo Checking all the files with Pyflakes
echo
for f in $(ls *.py); do echo "Checking $f"; echo; pyflakes $f; done
