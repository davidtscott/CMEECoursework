#!/usr/bin/env python3
# Date: Nov 2018

"""
""" 

__appname__ = '[ in python]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 


# imports QMEE CDT link and node data
# colour nodes by node type 
#   (organization type "University", "Hosting Partner", "Non-hosting Partner")
## write to a .svg file 

with open(../Data/QMEE_Net_Mat_edges.csv) as f
    links = f.read() 

with open(../Data/QMEE_Net_Mat_nodes.csv) as g
    nodes = g.read()

