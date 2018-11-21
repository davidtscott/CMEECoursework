#!/bin/bash
# Author: David Scott
# Scrit: RunLV.sh
# Desc: Runs three scipts, LV1.py LV2.py and LV3.py and checks speed
# Arguements:  
# Date:

### LV1.py
python3 -m cProfile -s cumtime LV1.py #| head -20 
echo LV1.py complete
echo 
###  LV2.py 
python3 -m cProfile LV2.py 1. 0.1 1.5 0.75 -s cumtime #| head -20 
echo LV2.py complete
echo 
### LV3.py 
python3 -m cProfile LV3.py -s cumtime # | head -20 
echo LV3.py complete
echo 
