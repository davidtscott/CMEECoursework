#!/usr/bin/env python3
# Date: October 2018

"""
Extracts tuples from within a tuple and outputs as seperate lines

""" 

__appname__ = '[tuple.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"


birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )


# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line or output block by species 
# Hints: use the "print" command! You can use list comprehension!

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

# for every tuple in object birds, print
# for tuple in birds:
#   print(tuple)
#   print("")

birdlist = [print(i,"\n") for i in birds]

# this prints each tuple seperately, seperated by blank line as opposed to
# printing entire block as would happen just used 'birds' 

# OR

#for tuple in birds:
#  print(tuple[0])
#  print(tuple[1])
#  print(tuple[2])
#  print(" ")
