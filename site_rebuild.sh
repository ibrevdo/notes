#!/bin/bash

SRC=/home/mago/git/notes
SITE=docs

cd $SRC

if [ -d $SITE ]; then
    rm -r $SITE/*
fi

mkdir -p $SITE/css

cp css/common.css $SITE/css/
touch $SITE/.nojekyll

python3 to_html.py


