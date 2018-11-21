#!/usr/bin/env python3
# Date: Nov 2018

"""
Use of subprocess to run Rscript. Prints 'Succesful' if succesful
"""

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
