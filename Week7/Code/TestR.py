#!/usr/bin/env python3
# Date: Nov 2018

"""
Example script to run an Rscript from python using subprocess module
""" 

__appname__ = '[subprocess Rscript in python]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

##packages 
import subprocess


subprocess.Popen("/usr/lib/R/bin/Rscript --verbose TestR.R > \
../Results/TestR.Rout 2> ../Results/TestR_errFile.Rout",\
 shell=True).wait()

# backlash allow python to read multiline script as single line
