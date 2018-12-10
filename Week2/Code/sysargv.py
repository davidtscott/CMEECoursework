#!/usr/bin/env python3
# Date: Oct 2018

"""basic boiler plate example, using sys module """ 

__appname__ = '[sys example]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

## imports ##
import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv)) 
