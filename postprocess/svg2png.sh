#!/bin/bash

cd  ../doc/figures
svgs=$(ls *.svg)
for i in $svgs; do
    inkscape $i --export-png=${i%.svg}".png"
done
