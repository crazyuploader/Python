#!/usr/bin/env bash
#
# Add executable permission to '*.py' files in current directories
#
# Colors
NC="\033[0m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"

# Variables
DATE="$(date +%m/%d/%y)"

git remote remove origin
git remote add origin https://"${GH_REF}"
git fetch --all
echo ""
echo "Adding executable permission"
echo ""
chmod +x ./*.py
CHANGES=$(git status --porcelain)
if [[ -n ${CHANGES} ]]; then
    CHANGED_FILES=$(git status --porcelain | cut -d " " -f 3)
    echo -e "${YELLOW}Changed Files${NC}"
    echo ""
    for file in ${CHANGED_FILES}; do echo -e "${GREEN}${file}${NC}"; ((FILES = FILES + 1)); done
    echo ""
    echo "${GREEN}${FILES} changed.${NC}"
    echo ""
fi
if [[ -z ${CHANGES} ]]; then
    echo -e "${GREEN}Nothing to commit${NC}"
else
    git config user.email "49350241+crazyuploader@users.noreply.github.com"
    git config user.name "crazyuploader"
    git add .
    git commit -m "Travis CI"              \
               -m ""                        \
               -m "Date: ${DATE}"            \
               -m ""                          \
               -m "Add Executable Permission:" \
               -m "$(for changes in ${CHANGED_FILES}; do echo "${changes}"; done)"
    git push https://crazyuploader:"${GITHUB_TOKEN}"@"${GH_REF}" HEAD:"${TRAVIS_BRANCH}"
    echo ""
    echo -e "${YELLOW}Changes pushed to branch '${TRAVIS_BRANCH}' at https://${GH_REF}/tree/${TRAVIS_BRANCH}"
fi
