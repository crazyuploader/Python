#!/usr/bin/env bash
#
# Add executable permission to '*.py' files in current directories
#
# Colors
NC="\033[0m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"

# Variables
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
DATE="$(date +%m/%d/%y)"

git add origin https://"${GH_REF}"
echo ""
echo "Adding executable permission"
echo ""
chmod +x ./*.py
CHANGES=$(git status --porcelain)
if [[ -n ${CHANGES} ]]; then
    CHANGED_FILES=$(git status --porcelain | cut -d " " -f 3)
fi
if [[ -z ${CHANGES} ]]; then
    echo -e "${GREEN}Nothing to commit${NC}"
else
    git config user.email "49350241+crazyuploader@users.noreply.github.com"
    git config user.name "crazyuploader"
    git add .
    git commit -m "Travis CI" \
               -m "" \
               -m "Date: ${DATE}" \
               -m "" \
               -m "Add Executable Permission:" \
               -m "$(for changes in ${CHANGED_FILES}; do echo "${changes}"; done)"
    git push https://crazyuploader:"${GITHUB_TOKEN}"@"${GH_REF}" HEAD:"${BRANCH}"
    echo -e "${YELLOW}Changes pushed to branch '${BRANCH}' at https://${GH_REF}/tree/${BRANCH}"
fi
