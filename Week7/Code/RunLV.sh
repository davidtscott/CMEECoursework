#!/bin/bash
# Author: David Scott
# Scrit: RunLV.sh
# Desc: Runs three scipts, LV1.py LV2.py and LV3.py and checks speed
# Arguements:  
# Date: Nov 2018

divider===============================
divider=$divider$divider
width=60

printf "%$width.${width}s\n" "$divider"

### LV1.py
python3 -m cProfile -s cumtime LV1.py 2>&1 | head -20 
echo
echo -e "LV1.py complete\n"
printf "%$width.${width}s\n" "$divider"

###  LV2.py 
python3 -m cProfile LV2.py 1. 0.1 1.5 0.75 -s cumtime 2>&1 | head -20 
echo
echo -e "LV2.py complete\n"
printf "%$width.${width}s\n" "$divider"

### LV3.py 
python3 -m cProfile LV3.py -s cumtime 2>&1 | head -20 
echo 
echo -e "LV3.py complete\n"
printf "%$width.${width}s\n" "$divider"

### LV4.py 
python3 -m cProfile LV4.py -s cumtime 2>&1 | head -20 
echo 
echo -e "LV4.py complete\n"
printf "%$width.${width}s\n" "$divider"
