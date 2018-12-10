#!/usr/bin/env python3
# Date: October 2018

""" Calculates tree height using trigonometric function in python""" 

__appname__ = '[get_TreeHeight.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import sys
import csv
import math
import os

## functions ##

def command_line_data(argv):
    """ creates an array from input file given in command line. 
    If none given, exits script and prints execution failure message. 
    retunrs array without headers
    """
    # if no file given exit script
    if (len(sys.argv) == 1):
        sys.exit("SCRIPT EXECUTION STOPPED: One input file must be supplied")
    # if there is make array but skip header row
    with open(sys.argv[1], 'r') as f:
        treedata = csv.reader(f)
        next(treedata)
        TreeArray = [row for row in treedata]
        return TreeArray

#create function to calculate height
def tree_height(degrees, distance): 
    """Calculates heights of trees given distance of each tree 
    from its base and angle to its top, using  the trigonometric formula """
    radians = degrees * math.pi / 180 # degrees
    height = distance * math.tan(radians) # distace 
    #print("Calculated heights in meters are:")
    return(height)

def main(argv):
    """ Call tree_height and command_line_data functions and outputs results 
    to csv file in results directory, using input file name. 
    """
    # call command_line_data function 
    AllData = command_line_data(sys.argv)
    # apply tree_height function to each row in array and append results to new column
    for row in range(len(AllData)):
        AllData[row].append(tree_height(float(AllData[row][2]), float(AllData[row][1])))

    # take elements from command line input file and add to output filename
    name = str(os.path.basename(os.path.splitext(sys.argv[1])[0]))
    outputfilename = "../Results/" + name + "_treeheights.csv"

    #write to a csv file and add headers
    with open("outputfilename", "w") as g:
        writer = csv.writer(g)
        writer.writerow(("Species", "Distance.m", "Angel.degrees", "Tree.Height.m"))
        for row in AllData:
            writer.writerow(row)
        print("Saved output to csv file: {}" .format(outputfilename))
        # prints output file name and path to file

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)


###
### alternative method below. decided to change it to make more use of functions etc 
###

# read distance, degrees and species names data into lists
#distance = []
#degrees = []
#names = []

#with open(sys.argv[1], 'r') as f:
    #next(f)             # skips header
    #for row in treedata:
        #names.append(row[0])
        #distance.append(float(row[1])) # import items to lst as floats
        #degrees.append(float(row[2]))

#create function to calculate height
#def tree_height(degrees, distance): #(treedata): 
    #"""Calculates heights of trees given distance of each tree 
    #from its base and angle to its top, using  the trigonometric formula """
    #heights = []
    #for i, j in zip(degrees, distance):
        #radians = i * math.pi / 180 # degrees (i) 
        #heights.append(j * math.tan(radians)) # distance (j)
    #print("Calculated heights in meters are:")
    #return(heights)

# call tree_height function with input parameters 
#   and joins lists of parameters with output tree heights 
#rows = zip(names, distance, degrees, tree_height(degrees, distance))

# take elements from command line input file and add to output filename
#name = str(os.path.basename(os.path.splitext(sys.argv[1])[0]))
#outputfilename = "../Results/" + name + "_treeheights.csv"

#write to a csv file and add headers
#with open("outputfilename", "w") as g:
    #writer = csv.writer(g)
    #writer.writerow(("Species", "Distance.m", "Angel.degrees", "Tree.Height.m"))
    #for row in rows:
        #writer.writerow(row)
    #print("Saved output to csv file: {}" .format(outputfilename))
    # prints output file name and path to file
    