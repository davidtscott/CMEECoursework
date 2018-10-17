#!/usr/bin/env python3

"""DNA sequence alignment.

Takes sequences as input from a single external file.
see '../Data/align_seqs.csv'

Saves best alignment and best score to a csv file.
see '../Results/align_seqs.csv'

All code is annotated within the script.

Author: David Scott (david.scott18@imperial.ac.uk)

""" 

__appname__ = '[sequence alignment]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"


# These are the two sequences to match
#seq2 = "ATCGCCGGATTACGGG"
#seq1 = "CAATTCGGAT"

import csv 

with open('../Data/align_seqs.csv', 'r') as csvfile:
    DNAseqs = csv.reader(csvfile)
    for row in DNAseqs:
        seq1 = row[0]
        seq2 = row[1]

# assign the longest sequence s1, and the shortest to s2
# l1 is the length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# function that computes a score
# by returning the number of matches 
# starting from arbitrary startpoint
def calculate_score(s1, s2, l1, l2, startpoint):
    # startpoint is the point at which we want to start
    matched = "" # contains string for alignement
    score = 0
    for i in range(l2):
        #pdb.set_trace()
        if (i + startpoint) < l1:
            # if its matching the character
            if s1[i + startpoint] == s2[i]:
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # build some formatted output
    print("." * startpoint + matched)        
    print("." * startpoint + s2) 
    print(s1)
    print(score) 
    print("")

    return score

calculate_score(s1, s2, l1, l2, 0)
calculate_score(s1, s2, l1, l2, 1)
calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score)
my_best_align = None
my_best_score = -1

for i in range(l1):
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2
        my_best_score = z

print(my_best_align)
print(s1)
print("Best score:", my_best_score)

with open('../Results/align_seqs.csv','w') as g:
    output = csv.writer(g)
    output.writerow([my_best_align])
    output.writerow([s1])
    output.writerow([my_best_score])
