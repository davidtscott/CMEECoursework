#!/usr/bin/env python3
# Date: October 2018

"""Shows use of inputting and outputting data in files to scripts"""

__appname__ = '[basic_io.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import pickle 

######################
# FILE INPUT
######################
# Open a file for reading ('r')
f = open('../Sandbox/test.txt', 'r')
# Use "implicit" for loop:
# if the object is a file, python will cycle over 
for line in f: 
    print(line) 

# Close the file 
f.close() 

# Same example, skip blank lines 
f = open('../Sandbox/test.txt', 'r')
for line in f: 
    if len(line.strip()) > 0:
        print(line) 

f.close() 

########################
# FILE OUTPUT 
########################
# Save the elements of a list to a file 
list_to_save = range(100) 

#open a file for writing ('w')
f = open('../Sandbox/testout.txt', 'w')
for i in list_to_save: 
    f.write(str(i) + '\n') ##Add a new line at the end 

f.close() 

######################
# STORING OBJECTS 
######################
# To save an object (even complex) for later use 
my_dictionary = {"a key": 10, "another key": 11} 

f = open('../Sandbox/testp.p', 'wb') 
## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again 
f = open('../Sandbox/testp.p', 'rb') 
another_dictionary = pickle.load(f) 
f.close() 

print(another_dictionary)
 