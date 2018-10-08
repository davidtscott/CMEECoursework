#!/bin/bash
# Author: David Scott david.scott18@imperial.ac.uk
# Script: CountLines.sh
# Desc: Counts the number of lines in a file 
# Arguments: <
# Date: Oct 2018
NumLines=`wc -l < $1`
echo "The file $1 has $NumLines lines"
echo