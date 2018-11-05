#!/usr/bin/python

""" Compares speed of two functions with and without loops""" 

__appname__ = '[Vectorize1]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

# packages
import numpy as np 
import time

# creates random array of dimension 1000 * 10000
#   with uniform distribution
M = np.random.rand(1000, 1000)

# define function to count each element or array M
start1 = time.time()  # starts timer
def SumAllElements(M):
"""Counts sum of elements of an array """
    tot = 0
    for i in np.nditer(M): 
        tot += i
    return tot
end1 = time.time()  # ends timer

SumAllElements(M) #calls function with input

# sum function does that same as above but without loops
start2 = time.time() # starts timer
SumFuntion = sum(M)
end2 = time.time() # ends timer

# print speed of functiosn to compare
print("Speed of function defined using loops:", end1 - start1) 
print("Speed of sum function without loops:", end2 - start2) 
