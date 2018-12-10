#!/usr/bin/env python3
# Date: October 2018

""" 
Six functions to show the use of modules for 
manipulation and calculation of variables
""" 

__appname__ = '[cfexercises2.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

"""
Main argument prints results of each function 
using a default input value, to test functionality. 

Uses loops for factorial calculations. 

Takes input from command line.
""" 

#### Modified script and made it a module. 
#### All functions take arguements from the command line.
#### Added test arguements, to output from each function to show they work.


## imports ##
import sys

## constants ##


#### functions ####

def foo_1(x):
    """exponent, x to the power of 0.5"""
    #return x ** 0.5 #exponent, x to the power of 0.5 
    return "%d to the power of 0.5 is %f." % (x, x ** 0.5)

def foo_2(x, y):
    """returns the greater value of x and y"""
    if x > y:
        return "%d is greater than %d" % (x, y)
    return "%d is greater than %d" % (y, x)

def foo_3(x, y, z):
    """reassigns variables"""
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

def foo_4(x):
    """obtains factorial of x"""
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return "The factorial of %d is %d" % (x, result)

def foo_5(x): # a recursive function
    """uses recursion to obtain the factorial of x"""
    if x == 1:
        return 1
    return x * foo_5(x - 1) #!x factorial of x 

def foo_6(x): #calculate the factorial of x in a different way
    """calculates factorial of x"""
    facto = 1
    while x >= 1:
        facto = facto * x 
        x = x -1 
    return "The factorial is %d" % facto 

def main(argv):
    """Prints results of each function with a default numeric input,
    from foo_1() to foo_6() in numeric order. 
    Default value used: foo_1(8), 2(5, 15), 3(20, 10, 5), 4(5), 5(7), 6(8)."""
    print(foo_1(8))
    print(foo_2(5, 15))
    print(foo_3(20, 10, 5))
    print(foo_4(5))
    print(foo_5(7))
    print(foo_6(8))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)

####
# once script is run, these function can be called on  
# and the value of x can be changed within terminal e.g foo4(10)
