#!/usr/bin/env python3
# Date: October 2018

""" Aligns any two fasta sequences from seperate files """

__appname__ = '[align_seqs_fasta.py]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

"""Aligns any two .fasta sequences from seperate files. 
Script takes inputs from user in command line, 
otherwise has two default input .fasta files.  

for default files see:
    fasta_input('../Data/fasta/407228326.fasta')
    fasta_input('../Data/fasta/407228412.fasta')

""" 

## imports ##
import sys 
import csv 

## functions ##

def fasta_input(fastafile):
    """ Read DNA seq from .fasta file, skips header
    and returns the sequence as a string by removing end line character.
    module designed so not to have to replicate code for each file input.
     """
    with open(fastafile, 'r') as f1: #'with' closes the file automatically
        f1str = "" #creates blank string
        counter = 0 #counter, starts at 0 
        for line in f1: 
            if counter:  #if line 0 (header) skip it
                f1str += line.replace("\n", "") # if not, so this
            counter += 1
    return f1str  # closes off function


def calculate_score(s1, s2, l1, l2, startpoint):
    """ Computes score of two DNA sequences aligned.
    startes from arbiary startpoint. Returns number 
    of matches.
    """
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
    #print("." * startpoint + matched)        
    #print("." * startpoint + s2) 
    #print(s1)
    #print(score) 
    #print("")

    return score


def main(argv):
    """ takes input from command line or defaults to two fasta files mapped,
    assigns them to two variables. Checks length of sequences. 
    assigns the longer sequence to s1 variable and shorter to s2 variable."""
    # if three or more argv variables in command line (includes module)
    if len(argv) >= 3:  
        # assign the first file (variable [1]) to seq1
        seq1 = fasta_input(sys.argv[1])
        #assign the second file (variable [2]) to seq2
        seq2 = fasta_input(sys.argv[2])
    else:
        # or, if number of arguments less than three:
        seq1 = fasta_input('../Data/fasta/407228326.fasta')
        seq2 = fasta_input('../Data/fasta/407228412.fasta')
        # assign default files (with file path) to variable seq1 and seq2
    # assign the longest sequence to s1, and the shortest to s2
    # l1 is the length of the longest, l2 that of the shortest
    l1 = len(seq1) #finds lenth of seq and assgns to variable
    l2 = len(seq2)
    if l1 >= l2:    # if l1 (seq1) is longer than l2 (seq2)
        s1 = seq1   
        s2 = seq2   
    else:    # assigns the longest sequense as s1 and the shorter as s2
        s1 = seq2   
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths

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

    # save output to .txt file 
    with open('../Results/align_seqs_fasta.txt','w') as outfile:
        outfile.write("My Best Score: {}\n".format(my_best_score)) 
        outfile.write("My Best Alignment: \n{}".format(my_best_align)) 


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
