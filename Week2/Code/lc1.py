#!/usr/bin/env python3
# Date: October 2018

"""Three list comprehensions and three loops on a tuple of tuples."""

__appname__ = '[lc1.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

"""
Object birds contains a tuple of tuples. Each tuple has the latin name,
common name and body mass of a bird species. 

Code in the script takes components of each tuple and assigns them to new list.

Each task is twice repeated, using both list comprehension and loops.   

The first one takes the latin name frome each tuple using index [0] and assigns 
it to a new list object. The second takes common name, index [1] 
and the third takes the body mass index [2]. 

""" 


birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !). 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS.


## 1 ## list comprehensions ##

## latin name of species
birds_latinname = [item[0] for item in birds] 
print(birds_latinname)
#selects birds latinname (index 0) from within each tuple
#   of the birds object
#   assigns it to object new "birds_latinname"
# prints content of birds_latin name
#   the latin name of each speces of birds

## common names of species 
birds_commonname = [item[1] for item in birds]
print(birds_commonname)
# same as above but for birds common name withn each tuple
#   index 1

## body mass of birds
birds_bodymass = [item[2] for item in birds]
print(birds_bodymass)
# same again but for birds body weight within each tuple
#   index 2


## 2 ## loops ##

## latin name of species
birds_latin_loops = []
# creates a list called birds_latin_loops
for item in birds: # start of loop
# for each item in object birds (tuple of tuples)
    birds_latin_loops.append(item[0]) 
    # appends birds latin name to birds_latin_loops
print(birds_latin_loops) #then print this list

## common names of species 
birds_common_loops = []
for item in birds:
    birds_common_loops.append(item[1])
print(birds_common_loops)
# same as above but this time selected index 1 - common names

## body mass of birds
birds_mass_loops = []
for item in birds:
    birds_mass_loops.append(item[2])
print(birds_mass_loops)
# selected item 2 - body mass
