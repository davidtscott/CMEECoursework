#!/bin/bash
# Author: David Scott David.Scott18@imperial.ac.uk
# Script: boilerplate.sh
# Desc: runs rscript and python3 scripts (both cal. tree height)
# Arguments: none
# Date: Oct 2018

Rscript --vanilla get_TreeHeight.R ../Data/trees.csv

python3 get_TreeHeight.py ../Data/trees.csv

