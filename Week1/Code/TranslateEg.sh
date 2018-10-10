# !/bin/bash
# Author: David Scott David.Scott18@imperial.ac.uk
# Script: TranslateEg.sh
# Desc: Three uses of the translate (tr) command: Remove spaces, letters, change case
# Arguments: none
# Date: Oct 2018

echo "remove    excess   spaces." | tr -s "\b" " " # Compresses a series of identical characters to single characters
							# in this case multiple spaces (blank characters) to a single

echo "remove all the as" | tr -d "a" # Deletes all occurances of a specified character from an input. In this case "a" 

echo "set to uppercase" | tr [:lower:] [:upper:] # Translates input from lower to upper. Can be done vice versa

echo "10.00 only numbers 1.33" | tr -d [:alpha:] | tr -s " " "," # Delete all letters (alpha), compress similar 
                                                                   #   characters and seperate with a comma. 
