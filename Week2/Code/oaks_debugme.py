#!/usr/bin/env python3
# Date: October 2018

"""Functions to detect and print oaks of genus 'Quercus'."""

__appname__ = '[oaks_debugme]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"


"""Dispays "FOUND AN OAK!" when oak species is detected.

Bug fixed of previous version (spelling)

Added doctests to test functionality of functions. 

All code is annotated within the script.

Author: David Scott (david.scott18@imperial.ac.uk)

""" 
## imports ##
import csv
import sys
import doctest
import pdb

#Define function
def is_an_oak(oakname):
    ## doctests within module
    """ Returns True if name starts with 'quercus', 
        otherwise returns False.
        
    >>> is_an_oak('Quercus robur')
    True
        
    >>> is_an_oak('Fraxinus excelsior')
    False

    >>> is_an_oak('Quercusstartswithaq fancythat')
    False

    """
    oakname = oakname.lower() #bug, quercus missing a u
    # Split string on space (" "), then take index [0] of the generated list.
    oakindex = oakname.split(" ")
    if len(oakindex[0]) != 7: #if length of first word not 7 characters
        return False # return it as false
    return oakname.startswith('quercus') # if
        

def main(argv): 
    """Takes data from input file, writes an output, 
    prints content and if it is a oak prints: 'FOUND AN OAK!'"""
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Results/JustOaksData.csv','w')
    taxa = csv.reader(f)
    next(taxa) ## EXCLUDES HEADER BEING PRINTED!! 
    csvwrite = csv.writer(g)
    csvwrite.writerow(['Genus', 'species']) ## ADDS HEADER!! 
    # oaks = set()  
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]):   #bug above interupted code here. 
        #did not recognise any oaks due to misspelling 
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])
    f.close()
    g.close()
    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod()
