#!/bin/bash
# Author: David Scott david.scott18@imperial.ac.uk
# Script: CountLines.sh
# Desc: Counts the number of lines in a file, assigns cout to a variable 
#       and prints results as a text string. 
# Arguments: $1 file to have lines counted
# Date: Oct 2018

NumLines=`wc -l < $1`  # redirects content of $1 file to the standard input of command
			# command wc -l counts number of lines 
			# output value then stored as variable NumLines 
echo "The file $1 has $NumLines lines"  # prints string with input file name ($1) and output value ($NumLines)
echo

