#!/bin/bash

SITE=site

if [ -d $SITE ]; then
    rm -r $SITE/*
fi

mkdir -p $SITE/css

cp css/common.css $SITE/css/

python3 to_html.py


