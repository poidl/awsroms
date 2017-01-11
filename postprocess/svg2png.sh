#!/bin/bash

cd  ../doc/figures
inkscape $1 --export-png=../figures_png/${1%.svg}".png"

