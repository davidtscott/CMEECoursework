#!/bin/bash
# Author: David Scott David.Scott18@imperial.ac.uk
# Script: boilerplate.sh
# Desc: runs rscript and python3 scripts (both cal. tree height)
# Arguments: none
# Date: Oct 2018

echo "Running get_TreeHeight.R in R"
Rscript --vanilla get_TreeHeight.R ../Data/trees.csv
echo -e "get_TreeHeight.R is complete. \n"


echo "Running get_TreeHeight.py in python3"
python3 get_TreeHeight.py ../Data/trees.csv
echo "get_TreeHeight.py is complete"
