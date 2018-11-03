#!/usr/bin/env python3

""" Calculates tree height using trigonometric function in python""" 

__appname__ = '[Tree Heights]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

# modules used
import sys
import csv
import math
import os

# read distance and degrees data into two lists
distance = []
degrees = []
names = []
with open(sys.argv[1], 'r') as f:
    next(f)
    treedata = csv.reader(f)
    for row in treedata:
            names.append(row[0])
            distance.append(row[1])
            degrees.append(row[2])

# converts items in list to floats
distance2 = [float(i) for i in distance]
degrees2 = [float(i) for i in degrees]

#create function to calculate height
def tree_height(degrees2, distance2): #(treedata): 
    """This function calculates heights of trees given distance of each tree 
    from its base and angle to its top, using  the trigonometric formula """
    heights = []
    for i, j in zip(distance2, degrees2):
        radians = i * math.pi / 180 #distance (i)
        heights.append(j * math.tan(radians)) #degrees (j)
    print("Calculated heights in meters are:")
    print(heights)

    # join lists 
    rows = zip(names, distance, degrees, heights)

    # take elements from command line input file and add to output filename
    a = os.path.splitext(sys.argv[1])[0]
    b = a.split("/")
    c = b[2]
    outputfilename = "../Results/" + c + "_treeheights.csv"

    #write to a csv file and add headers
    with open("outputfilename", "w") as g:
        writer = csv.writer(g)
        writer.writerow(("Species", "Distance.m", "Angel.degrees", "Tree.Height.m"))
        for row in rows:
            writer.writerow(row)
        print("Saved output to csv file: {}" .format(outputfilename))

tree_height(degrees2, distance2)
