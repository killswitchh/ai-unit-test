#!/bin/bash
add_comments_script=$1
echo $add_comments_script
for file in $(find . -name "add_unit_tests.py" -prune -o -name "*.py" -print)
do
    echo $file
    if [[ ($file == ./ai-tests* ) ||  ($file == ./tests* ) || ($file == ./.github/unit-test* )]] ;
    then
        echo "IGNORING" + $file
    else
        echo "EXECUTING" + $file
        python $add_comments_script $file
    fi
done