#!/usr/bin/env python3
# Date: Nov 2018

"""Example of profiling functions in python""" 

__appname__ = '[profiling functions in python]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

def my_squares(iters):
    out = []
    for i in range(iters):
        out.append(i ** 2)
    return out 

# range in python3 iterates efficieantly. 
# append grows memory of lis defined. thsi si slow  

def my_join(iters, string):
    out = '' # creates a string
    for i in range(iters):
        out += string.join(", ") #.join for strings 
    return out 

def run_my_funcs(x,y):
    print(x,y)
    my_squares(x)
    my_join(x,y)
    return 0 

run_my_funcs(10000000,"My string")
