#!/bin/bash
# Author: David Scott david.scott18@imperial.ac.uk
# Script: tiff2png.sh
# Desc: Converts a .tif file to a .png file
# Arguments: $*.tif 
# Date: Oct 2018

for f in $*.tif;   # sets .tif file as variable f
   do 
       echo "Converting $f";  # prints string with name of .tif file (f)
       convert "$f"  "$(basename "$f" .tif).png"; #converts variable f to png 
						  #  while maintaining basename f
    done  					  #    i.e basename.png
