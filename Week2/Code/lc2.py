#!/usr/bin/env python3

"""Extracts tuples from a tuple of tuples of rainfal data."""

__appname__ = '[]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

"""
Completes two tasks (below), twice by using both list comprehension and loops
    1- creates a list of month, rainfall tuples where the rainfall 
    was above 100.0 mm

    2- creates list of month names where the rainfall was below 50.0 mm

""" 


# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.

rainfall_big = [item for item in rainfall if item[1] > 100.0]
# creates an object called rainfall_big.
# assigns every item (month, rain tuple) to rainfall_big with a rainfall (index[1]) 
#   above 100.0 
print(rainfall_big)
# prints object (list of tuples)

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm.

rainfall_small = [item[0] for item in rainfall if item[1] < 50.0]
# creates a list object called rainfall_small.
# assigns every item[0] (month name) to rainfall_small with a rainfall (index[1]) 
#   below 50mm
print(rainfall_small)
# print object (list of months name)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

#same as above but with loops
# here used 'rain' instead of 'item' as above. same principle
# both rain and item represent each tuple in rainfall. can use anyterm.

rainfall_b = set()
# created a set called rainfall_b to be fed from the loop
for rain in rainfall:
# for each rain (tuple) in ranfall
    if rain[1] > 100.0:
        #if index 1 (rainfall) of tuple measures over 100.0
        rainfall_b.add(rain)
        #add the tuple (rain) to new set rainfall_.b
print(rainfall_b)
# prints contetn of rainfall_b only containing tuples with a rainfall > 100.0

# here same again but with slight change 
rainfall_s = set()
for rain in rainfall:
    if rain[1] < 50.0:
        # selected tuples with rainfall (index 1) below 50.0 
        rainfall_s.add(rain[0])
        # only added the month name to new object rainfall_s
print(rainfall_s)
#prints content

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
