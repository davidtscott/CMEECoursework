#!/bin/bash 
# Author: David Scott david.scott18@imperial.ac.uk
# Script: csvtospace.sh
# Desc: substitute a comma for a space
# Arguments: 
# Date: Oct 2018

echo "Creating a space delimited version of $1 ..."
cat $1 | tr "," " " >> $1.txt 
echo "Done!"
exit 