#!/bin/bash
# Author: David Scott David.Scott18@imperial.ac.uk
# Script: ConcatenateTwoFiles.sh
# Desc: Takes two files (as variables $1, $2) and merges them together as a new
#       file ($3). File names are written in the command line after 
#	bash ConcatenateTwoFiles.sh respectively. 
# Arguments: Two files $1 $2 to be merged together.
# Date: Oct 2018

cat $1 > $3     #Takes content of first variable (file) and duplicates it in variable 3 (creates new file).
cat $2 >> $3	#Appends the content of variable 2 (second file) to the end of variable 3 (file created). 
echo "Merged File is"
cat $3
