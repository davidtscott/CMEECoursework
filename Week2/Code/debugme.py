#!/usr/bin/env python3
# Author: David Scott David.Scott18@imperial.ac.uk
# Date: Oct 2018

""" simple debug example fucntion."""

__appname__ = '[debug example function]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"


def createabug(x):
    """simple function with a bug to fix"""
    y = x**4
    z = 0.
    y = y/z
    return y 

createabug(25)
