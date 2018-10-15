#!/usr/bin/env python3
# Author: David Scott David.Scott18@imperial.ac.uk
# Script: 
# Desc: 
# Arguments:
# Date: Oct 2018

#### To be modified to make it a "module"

"""Some functions exemplifying the use of..... """ 

__appname__ = '[                  ]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

#### imports ####
import sys

#### constants ####

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
    """   """
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo_5(x): # a recursive function
    """uses recusrion to obtain the factorial of x"""
    if x == 1:
        return 1
    return x * foo_5(x - 1) #!x factorial of x 
    #return "By process of recurions, %d is the factorial of %d" % (x * foo_5(x - 1), x)

def foo_6(x): #calculate the factorial of x in a different way
    """calculates factorial of x"""
    facto = 1
    while x >= 1:
        facto = facto * x 
        x = x -1 
    return "The factorial is %d" % facto 

def main(argv):
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
