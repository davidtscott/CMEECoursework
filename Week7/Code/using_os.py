#!/usr/bin/env python3
# Date: Nov 2018

"""
Use the subprocess.os module to get list of files and  directories 
in ubuntu home directory. 
"""

# Hint: look in subprocess.os and/or subprocess.os.path and/or 
# subprocess.os.walk for helpful functions

#Packages
import subprocess
import re

#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:


# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithC = []

# Use a for loop to walk through the home directory.
for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir + files:
        FilesDirsStartingWithC += re.findall(r"^C", i)
print("Number of subdirs and files beginning with 'C':")
print(len(FilesDirsStartingWithC))

#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'

FilesDirsStartingWithCorc = []

# Type your code here:

for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir + files:
        FilesDirsStartingWithCorc += re.findall(r"^[Cc]", i)
print("Number of subdirs and files beginning with 'C' or 'c':")
print(len(FilesDirsStartingWithCorc))
#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 

DirsStartingWithCorc = []

# Type your code here:
for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir:
        if re.search(r"^[Cc]", i) != None:
            DirsStartingWithCorc.append(i)
print("Number of subdirs beginning with 'C' or 'c':")
print(len(DirsStartingWithCorc))
