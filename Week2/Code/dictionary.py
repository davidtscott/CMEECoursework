#!/usr/bin/env python3
# Date: October 2018

"""Populates a dictionary from a list of tuples (Species name, Order)
"""

__appname__ = '[taxa_dic]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

"""
Uses order as key and species names as values. 

Dictionary named taxa_dic

Some tuples share order thus, multiple species are assigned to 
each order in dictionary.

To use, run script, write taxa_dic['Carnivora'] into command line. 

Includes orders Chiroptera, Rodentia, Afrosoricida, Carnivora.

""" 


taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

# Write your script here:

### created a dictionary whihc is a set of values indexed by keys. 
# in this case the keys are the order names
# the values are species names 
        
#taxa_dic = {k: v for v, k in taxa}

# create empty dictionary
taxa_dic={}

# v = value (species name)
# k = key (order)
for v, k in taxa:
    if k in taxa_dic:
        # append the new species to the order
        taxa_dic[k].append(v)
    else:
        # add new order to dic and assign its species name
        taxa_dic[k] = [v]

print(taxa_dic)

# to draw information from dictionary use:
### taxa_dic['Carnivora']

#### old solution ##

# first defined name of dictionary - taxa_dic
# then curly brackets start the dictionary construction
# then define first keys e.g 'Carnivora'
#       this is an order 
#now to give that key (order) its list of values (species names) do:
# 'Carnivora' : set(['x', 'y', 'z'])
# in this case 'x', 'y', 'z'  values will be species names of order carivora. 
# this creates a tuple of names indexed by an order 
# can be repeated for as many key : value pairs
# essentially a dictionary is a group indexed tuples 

# taxa_dic = {'Chiroptera' : set(['Myotis lucifugus']), 
#         'Rodentia' : set(['Gerbillus henleyi', 'Peromyscus crinitus', 
#         'Mus domesticus', 'Cleithrionomys rutilus']), 
#         'Afrosoricida' : set(['Microgale dobsoni', 'Microgale talazaci']),
#         'Carnivora' : set(['Lyacon pictus', 'Arctocephalus gazella', 
#         'Canis lupus'])}
