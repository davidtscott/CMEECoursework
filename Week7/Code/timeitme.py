#!/usr/bin/env python3
# Date: Nov 2018

"""
Example of timeit module in python. 
Imports modules from profileme and profileme2.
""" 

__appname__ = '[timeitme.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

##### Modules ## 
import time
import timeit
from profileme import my_squares as my_squares_loops
from profileme2 import my_squares as my_squares_lc
from profileme import my_join as my_join_join
from profileme2 import my_join as my_join

#nmber of iterations 
iters = 1000000

### Loops versus list comprehension 

# %timeit my_squares_loops(iters)
# %timeit my_squares_lc(iters)

start = time.time()
my_squares_loops(iters)
print("my_squares_loops takes %f s to run." % (time.time() - start))

start = time.time()
my_squares_lc(iters)
print("my_squares_lc takes %f s to run." % (time.time() - start))


### loops versus join method for strings

mystring = "my string"

# %timeit(my_join_join(iters, mystring))
# %timeit(my_join(iters, mystring))

start = time.time()
my_join_join(iters, mystring)
print("my_join_join takes %f s to run." % (time.time() - start))

start = time.time()
my_join(iters, mystring)
print("my_join takes %f s to run." % (time.time() - start))
