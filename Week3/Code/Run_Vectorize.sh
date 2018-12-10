#!/bin/bash
# Author: David Scott David.Scott18@imperial.ac.uk
# Script: boilerplate.sh
# Desc: Compares speed of functions with and without vectorization(R & Python)
# Arguments: none
# Date: Oct 2018

divider===============================
divider=$divider$divider
width=60

printf "%$width.${width}s\n" "$divider"

echo -e "Running Vectorize1.R  in R .... \n"
time Rscript --vanilla Vectorize1.R 
echo -e "^^ Run time of Vectorize1.R script. \n"
echo -e "Vectorize1.R is complete. \n"

printf "%$width.${width}s\n" "$divider"

echo -e  "Running Vectorize1.py in python3 .... \n"
time python3 Vectorize1.py
echo -e "^^ Run time of Vectorize1.py script. \n"
echo -e  "Vectorize1.py is complete. \n"

printf "%$width.${width}s\n" "$divider"

echo -e "Running Vectorize2.R  in R .... \n"
time Rscript --vanilla Vectorize2.R
echo -e "^^ Run time of Vectorize2.R script. \n"
echo -e "Vectorize2.R is complete. \n"

printf "%$width.${width}s\n" "$divider"

echo -e "Running Vectorize2.py in python3 .... \n"
time python3 Vectorize2.py
echo -e "^^ Run time of Vectorize2.py script. \n"
echo -e "Vectorize2.py is complete.\n"

printf "%$width.${width}s\n" "$divider"
