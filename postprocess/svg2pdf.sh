#!/bin/bash

cd  ../docs/figures
svgs=$(ls *.svg)
for i in $svgs; do
    inkscape $i --export-pdf=../../doc/figures_pdf/${i%.svg}".pdf"
done
