#!/bin/bash 
# Author: David Scott david.scott18@imperial.ac.uk
# Script: csvtospace.sh
# Desc: substitute a comma for a space, creating a new .txt version of file. 
# Arguments: $1 csv file, of which a duplicate space delimited version is to be made
# Date: Oct 2018

echo "Creating a space delimited version of $1 ..." # Prints string stating which file ($1)
					 	#is to be converted from comma to space seperated. 
file="${1//.csv/}"                       #removes the .csv extension of variable 1. Replaces it with nothing. 
cat $1 | tr "," " " >> $file.txt 	# Reads content of variable 1 as an output, piped, then translates occurances 				# of commas to space and appends content to a new .txt version without the csv extension ($1).
echo "Done!" 					# Prints "Done!" when complete
exit 
