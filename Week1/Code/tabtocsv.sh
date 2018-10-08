#!/bin/bash
# Author: David Scott david.scott18@imperial.ac.uk
# Script: tabtocsv.sh
# Desc: substitute the tabs in the files with commas
# Arguments: 1 -> tab delimited file
# Date: Oct 2018 

echo "Creating a comma delimited version of $1 ..."
cat $1 | tr -s "\t" "," >> $1.csv 
echo "Done!"
exit 
