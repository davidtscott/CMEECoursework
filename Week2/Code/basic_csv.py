#!/usr/bin/env python3
# October 2018

""" Script to show the use of csv module in python. """

__appname__ = '[basic_csv]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## imports ##
import csv

## constants ##


## functions ## 

# Read a file containing: 
# 'Species','Intraorder','Family','Distribution', 'Body mass male (Kg)'
f = open('../Data/testcsv.csv','r')

# extract ad print desired data
csvread = csv.reader(f) 
temp = []
for row in csvread:
    temp.append(tuple(row))
    print(row)
    print("The species is", row[0]) 

f.close() # close file

# Write a file containing only species name and body mass
f = open('../Data/testcsv.csv','r') 
g = open('../Data/bodymass.csv','w') 

csvread = csv.reader(f) 
csvwrite = csv.writer(g) 
for row in csvread: 
    print(row) 
    csvwrite.writerow([row[0], row[4]]) 

f.close()
g.close() 
