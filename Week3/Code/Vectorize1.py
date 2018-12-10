#!/usr/bin/env python3
# Date: October 2018

""" Compares speed of two functions with and without vectorization""" 

__appname__ = '[Vectorize1.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import numpy as np 
import time

# creates random array of dimension 1000 * 10000
#   with uniform distribution
M = np.random.rand(1000, 1000)

# define function to count each element of array M
def SumAllElements(M):
    """Counts sum of elements of an array """
    tot = 0
    for i in np.nditer(M): 
        tot += i
    return tot

## Call SumAllElements function with input and timeit 
start1 = time.time()  # starts timer
SumAllElements(M) #calls function with input
end1 = time.time()  # ends timer

## Call sum function with input and timeit 
# sum function does that same as above but without loops
start2 = time.time() # starts timer
np.sum(M)
end2 = time.time() # ends timer

# print speed of functiosn to compare
print("Speed of SumAllElements function using loops: {}".format(end1 - start1)) 
print("Speed of sum function without loops: {}".format(end2 - start2)) 
