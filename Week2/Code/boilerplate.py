#!/usr/bin/env python3
# Author: David Scott David.Scott18@imperial.ac.uk
# Date: Oct 2018

"""basic boiler plate example, using sys module """ 

__appname__ = '[python boilet plate example]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

## imports ##
import sys # module to interface our program with the operating system 

## Constants ##

## functions ## 
def main(argv):
    """ Main entry point of the program """
    print ('This is a boilerplate') # four space indent 
    return 0             #used for debugging. 0 for success or failure

if __name__ == "__main__": 
    """Makes sure the "main" function is called from command line"""
    status = main(sys.argv)    
    sys.exit(status) 
