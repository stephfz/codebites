#!/bin/sh
# Auto-check for pep8 so I don't check in bad code
FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -e '\.jinja$' | grep -v '\/migrations\/')

if [ -n "$FILES" ]; then
    /usr/local/bin/flake8 $FILES
    python /Users/stephaniefrias/Projects/codebites/amp_spike/read_and_seek.py $FILES
fi
