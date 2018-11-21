#!/bin/bash
# Author: David Scott David.Scott18@imperial.ac.uk
# Script: CompileLaTeX.sh
# Desc: Compile LaTeX with bibtex 
# Arguments: $1 
# Date: Oct 2018

pdflatex $1    #Did not add .tex so that code can freely read .tex file
pdflatex $1
texfile="${1//.tex/}"  #created a new variable texfile which removes the .tex from file assigned to $1 
bibtex $texfile   #Uses new variable textfile as bibtex cannot have file with .tex
pdflatex $1 
pdflatex $1 
mv $texfile.pdf ../Results       # moves output (pdf version of texfile) to Results
evince ../Results/$texfile.pdf & # displays pdf output on screen 

## Cleanup  # Removing all other files created other than .bib .pdf and .tex
rm *~
rm *.aux
rm *.bbl   # .bbl also added to script to remove 
rm *.blg   # .blg also added to script to remove as these files are not required
rm *.dvi
rm *.log
rm *.nav 
rm *.out
rm *.snm
rm *.toc
