# README Document for CMEECourseWork Week2
## Author: David Scott- _david.scott18@imperial.ac.uk_
## Date: _Oct - 2018_

### Description: [Enter description for project here]

### Tree map
```
.
├── Code
│   ├── align_seqs_better.py : DNA sequence alignment, improved version so that the output  includes each best alignment   Takes sequences as input from a single external file. see '../Data/align_seqs_better.txt'  Saves best alignment and best score to a csv file. see '../Results/align_seqs_better.txt'  All code is annotated within the script.  Author: David Scott (david.scott18@imperial.ac.uk)
│   ├── align_seqs_fasta.py : Aligns any two .fasta sequences from seperate files.  Script takes inputs from user in command line,  otherwise has two default input .fasta files.    for default files see:     fasta_input('../Data/fasta/407228326.fasta')     fasta_input('../Data/fasta/407228412.fasta')  All code is annotated within the script.  Author: David Scott (david.scott18@imperial.ac.uk)
│   ├── align_seqs.py : DNA sequence alignment.  Takes sequences as input from a single external file. see '../Data/align_seqs.csv'  Saves best alignment and best score to a csv file. see '../Results/align_seqs.csv'  All code is annotated within the script.  Author: David Scott (david.scott18@imperial.ac.uk)
│   ├── basic_csv.py : script to show the use of csv module in python.
│   ├── basic_io.py : Shows use of inputting and outputting data in files to scripts
│   ├── boilerplate.py : basic boiler plate example, using sys module 
│   ├── cfexercises1.py : Control flow examples 
│   ├── cfexercises2.py : Six functions to show the use of modules for  manipulation and calculation of variables.   Main arguemnt prints results of each function using a default input value, to test functionality.   Uses loops for factorial calculations.   Take input from command line.  All code is annotated within the script.  Author: David Scott (david.scott18@imperial.ac.uk)
│   ├── control_flow.py : Some functions exemplifying the use of control statements 
│   ├── debugme.py : simple debug example fucntion.
│   ├── dictionary.py : Populates a dictionary from a list of tuples (Species name, Order). Uses order as key and species names as values.   Dictionary named taxa_dic  Some tuples share order thus, multiple species are assigned to each order in dic.   To use, run script, write taxa_dic['Carnivora'] into command line.   Includes orders Chiroptera, Rodentia, Afrosoricida, Carnivora.  All code is annotated within script.  Author: David Scott (david.scott18@imperial.ac.uk)
│   ├── lc1.py : Three list comprehensions and three loops on a tuple of tuples.  Object birds contains a tuple of tuples. Each tuple has the latin name, common name and body mass of a bird species.   Code in the script takes components of each tuple and assigns them to new list.  Each task is twice repeated, using both list comprehension and loops.     The first one takes the latin name frome each tuple using index [0] and assigns  it to a new list object. Thhe second takes common name, index [1]  and the third takes the body mass index [2].   All code is annotated within script.   Author: David Scott (david.scott18@imperial.ac.uk)
│   ├── lc2.py : Extracts tuples from a tuple of tuples of rainfal data.   Completes two tasks (below), twice by using both list comprehension and loops     1- creates a list of month, rainfall tuples where the rainfall      was above 100.0 mm      2- creates list of month names where the rainfall was below 50.0 mm  All code is annotated within script.  Author: David Scott (david.scott18@imperial.ac.uk)
│   ├── loops.py : basic boilerplate to demonstrate the use of loops in python 
│   ├── oaks_debugme.py : Functions to detect and print oaks of genus 'Quercus'.  Dispays "FOUND AN OAK!" when oak species is detected.  Bug fixed of previous version (spelling)  Added doctests to test functionality of functions.   All code is annotated within the script.  Author: David Scott (david.scott18@imperial.ac.uk) : simple debug example fucntion.
│   ├── oaks.py : Using loops in python to manipulate data.
│   ├── scope.py : example to show global variables 
│   ├── sysargv.py : basic boiler plate example, using sys module 
│   ├── test_control_flow.py : Some functions exemplifying the use of control statements  : Some functions exemplifying the use of control statements
│   ├── tuple.py : Extracts tuples from within a tuple and outputs as seperate lines,  seperated by a blank line.   All code is annotated within the script.  Author: David Scott (david.scott18@imperial.ac.uk)
│   └── using_name.py : shows use of main 
├── Data
│   ├── align_seqs.csv
│   ├── bodymass.csv
│   ├── fasta
│   │   ├── 407228326.fasta
│   │   ├── 407228412.fasta
│   │   └── E.coli.fasta
│   ├── JustOaksData.csv
│   ├── testcsv.csv
│   └── TestOaksData.csv
├── README.md
├── README.txt
└── Sandbox
    ├── testout.txt
    ├── testp.p
    └── test.txt

4 directories, 34 files

```
