#!/usr/bin/env python3
# Date: Nov 2018

"""
Using regex in python.
""" 
"""
Use of regex in python. Loads data and extracts data on kingdom,
phylum and species name of each species in the file. 

decode data to ASCII

Prints and formas output to the screen. 
"""

__appname__ = '[blackbirds.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

## imports ## 
import re

# Read the file
with open('../Data/blackbirds.txt', 'r') as f:
    text = f.read()

#encoding="ascii", errors="surrogateescape"

# remove \t\n and put a space in:
text = text.replace('\t',' ')
text = text.replace('\n',' ')

# note that there are "strange characters" (these are accents and
# non-ascii symbols) because we don't care for them, first transform
# to ASCII:
text = text.encode('ascii', 'ignore').decode() 
#print(text)
# Now extend this script so that it captures the Kingdom, 
# Phylum and Species name for each species and prints it out to screen neatly.

# Hint: you may want to use re.findall(my_reg, text)...
# Keep in mind that there are multiple ways to skin this cat! 
# Your solution may involve multiple regular expression calls 
# (easier!), or a single one (harder!)

reg_string = r"Kingdom\s(\w+).*?Phylum\s(\w+).*?Species\s(\w*\s\w+)" 

# carry out the cmmand on that string 

species = re.findall(reg_string, text)
#print(species)

# format and print output to screen
print('{A1:<15}{B1:<15}{C1:<15}'.format(A1='Kingdom', B1='Phylum', C1='Species'))
print('-'*50)
for i in species:
    print('{A2:<15}{B2:<15}{C2:<15}'.format(A2=i[0], B2=i[1], C2=i[2]))
