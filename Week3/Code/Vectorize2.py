#!/usr/bin/env python3
# Date: October 2018

"""
Compares speed of two Stochastic Ricker models with and without
Vectorization.
""" 

__appname__ = '[Vectorize2.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import numpy as np 
import time

## Stochastic Ricker Equation
def stochrick(p0= np.random.uniform(.5, 1.5, (1000)), \
              r=1.2, K=1, sigma=0.2, numyears=100):
    """ Stochasitic Ricker model with Gausiann fluctiation """
    N = np.full([numyears, len(p0)], np.nan)
    N[0,] = p0 
    for pop in range(1, p0):
        for yr in range(2, p0):
            N[yr, pop] = N[yr - 1, pop] * np.exp(r * (1 - N[yr - 1, pop] / K) \
                        + np.random.normal(0, sigma, len(p0)))
    return N 

# call function and record time taken to execute
# records run time imediately prior and post execution
start1 = time.time()
stochrick
end1 = time.time()

time1 = end1 - start1

# format print output with time taken
print("Stochastic Ricker takes:{}".format(time1))

## Vectorized Stochastic Ricker Equation 
def stochrickvect(p0= np.random.uniform(.5, 1.5, (1000)),\
                  r=1.2, K=1, sigma=0.2, numyears=100):
    """ Vectorized Stochasitic Ricker model with Gausiann fluctiation. 
    Does not loop through pop and pop has been removed from the model."""
    N = np.full([numyears, len(p0)], np.nan)
    N[0,] = p0 
    # removed the pop loop
    for yr in range(2, p0):
        # removed pop from equation also
        N[yr,] = N[yr - 1,] * np.exp( r * (1 - N[yr - 1,] / K) \
                + np.random.normal(0,sigma, len(p0)))
    return N 

# call function and record time taken to execute 
# records run time imediately prior and post execution
start2 = time.time()
stochrickvect
end2 = time.time()

time2 = end2 - start2

# format print output with time taken
print("Vectorized Stochastic Ricker takes:{}".format(time2))
