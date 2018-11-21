#!/usr/bin/env python3
# Date: Nov 2018

"""
Use of subprocess to run Rscript. Prints 'Succesful' if succesful
"""

__appname__ = '[subprocess in python]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

# packages
import subprocess 
import re


p = subprocess.Popen(["Rscript --verbose fmr.R"], stdout=subprocess.PIPE, \
stderr=subprocess.PIPE, shell=True)
stdout, stderr = p.communicate()
q = stdout.decode()
print()

if len(re.findall(r"Finishsed", q)) == 1: # if word "Finished" appears once, 
    print("Succesful") # print succesful
else:
    print("Not Succesful") # if not print not succesful to screen
