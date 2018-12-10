#!/usr/bin/env python3
# Date: October 2018

""" shows use of main """ 

__appname__ = '[using_name.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"


if __name__ == '__main__':
    #if being run by itself print this
    print('This program is being run by itself') 
else: 
    #if not, print this
    print('I am being imported from another module')  

### this can also be embedded into boilerplate.py
