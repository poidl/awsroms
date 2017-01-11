#!/bin/bash

cd  ../docs/figures
inkscape $1 --export-png=../../doc/figures_png/${1%.svg}".png"

