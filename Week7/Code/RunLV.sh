#!/bin/bash
# Author: David Scott
# Scrit: 
# Desc:
# Arguements:  
# Date:

### LV1.py
python3 -m cProfile -s cumtime LV1.py | head -20 

###  LV2.py 
python3 -m cProfile LV2.py 1. 0.1 1.5 0.75 -s cumtime | head -20 

### LV3.py 
python3 -m cProfile LV3.py -s cumtime | head -20 
