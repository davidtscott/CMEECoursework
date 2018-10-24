#!/usr/bin/env python3

""" Calculates tree height using trigonometric function in python""" 

__appname__ = '[Tree Heights]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"


import sys
import csv

distance = []
degrees = []
with open(sys.argv[1], 'r') as file:
    treedata = csv.reader(file)
    for row in treedata:
        distance.append(row[1])
        degrees.append(row[2])

print(distance)
print(degrees)

#create function to calculate height

def tree_height(degree, distance):
    """This function calculates heights of trees given distance of each tree 
from its base and angle to its top, using  the trigonometric formula """
    #convert into python script
    radians = degrees * pi / 180
    height = distance * tan(radians)
    print(height)

#paste("Tree height is:",
#do name and ou
tree_height(degrees, distance) 
