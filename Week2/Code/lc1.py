#!/usr/bin/env python3

"""Three list comprehensions and three loops on a tuple of tuples.

Object birds contains a tuple of tuples. Each tuple has the latin name,
common name and body mass of a bird species. 

Code in the script takes components of each tuple and assigns them to new list.

Each task is twice repeated, using both list comprehension and loops.   

The first one takes the latin name frome each tuple using index [0] and assigns 
it to a new list object. Thhe second takes common name, index [1] 
and the third takes the body mass index [2]. 

All code is annotated within script. 

Author: David Scott (david.scott18@imperial.ac.uk)

""" 

__appname__ = '[lc1.py - a tuple of tuples!]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"


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


##1## list comprehensions ##
birds_latinname = [item[0] for item in birds] 
#selects birds latinname (index 0) from within each tuple
#   of the birds object
#   assigns it to object new "birds_latinname"
print(birds_latinname)
# prints content of birds_latin name
#   the latin name of each speces of birds

birds_commonname = [item[1] for item in birds]
print (birds_commonname)
# same as above but for birds common name withn each tuple
#   index 1

birds_bodymass = [item[2] for item in birds]
print (birds_bodymass)
# same again but for birds body weight within each tuple
#   index 2

##2## loops ##

# latin name of species
# created the same 3 lists but used loop rather than list comprehension
birds_latin_loops = set()
# creates a set of unique elements called birds_latin_loops
for item in birds: # start of loop
# for each item in object birds (tuple of tuples)
    if item[0]: #if birds latin name (index 0)
        birds_latin_loops.add(item[0]) #add this item to set birds_latin_loops
print(birds_latin_loops) #then print this new set

# common names of species 
birds_common_loops = set()
for item in birds:
    if item[1]:
        birds_common_loops.add(item[1])
print(birds_common_loops)
# same as above but this time selected index 1 - common names

# body mass of birds
birds_mass_loops = set()
for item in birds:
    if item[2]:
        birds_mass_loops.add(item[2])
print(birds_mass_loops)
# selected item 2 - body mass
