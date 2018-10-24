#!/usr/bin/env python3
# Filename: using_name.py 

""" shows use of main """ 
__appname__ = '[main]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"


if __name__ == '__main__':
    print('This program is being run by itself') #if being run by itself print this
else: 
    print('I am being imported from another module') #if not, print this 

### this can also be embedded into boilerplate.py
