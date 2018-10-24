#!/usr/bin/env python3
# Date: Oct 2018

"""basic boilerplate to demonstrate the use of loops in python """ 

__appname__ = '[python loop example]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

# For loops in Python
for i in range(5):
    print(i) 

my_list = [0, 2, "geronimo!", 3.0, True, False]
for k in my_list:
    print(k)

total = 0
summands = [0, 1, 11, 111, 1111] #creates a new total each time it loops
for s in summands:
    total = total + s 
    print(total)

# While loops in Python
z = 0 
while z < 100:
    z = z + 1
    print(z) 

b = True 
while b: 
    print("GERONIMO! infinite loop! ctrl+c to stop!")
# ctrl + c to stop
