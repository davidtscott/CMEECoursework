#!/usr/bin/env python3
# Date: Oct 2018

""" simple debug example fucntion."""

__appname__ = '[debugme.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## functions ##

def createabug(x):
    """simple function with a bug to fix"""
    y = x**4
    z = 2
    y = y/z
    return y 

# fixed the bug, set z to equal integer of 2
# can reset z to equal 0. for bug

createabug(25)
