#!/usr/bin/env python3

"""example to show global variables """ 

__appname__ = '[global variables]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

_a_global = 10

def a_function():
    """showing use of gloabl variables"""
    global _a_global 
    #without this the definition would not exist outside function
    _a_global = 5
    _a_local = 4
    print("Inside the function, the value is ", _a_global) 
    print("Inside the function, the value is ", _a_local)
    return None

a_function()
print("Outside the function, the value is ", _a_global) 
