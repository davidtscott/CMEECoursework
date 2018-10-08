#!/bin/bash
# Author: David Scott david.scott18@imperial.ac.uk
# Script: variables.sh
# Desc: 
# Arguments: 
# Date: Oct 2018

# Shows the use of variables 
MyVar='some string'
echo 'the current value of the variable is' $MyVar 
echo 'Please enter a new string'
read MyVar 
echo 'the current value of the variable is' $MyVar 

## Reading multiple values 
echo 'Enter two numbers sepearted by space(s)'
read a b 
echo 'you entered' $a 'and' $b '. Their sum is:'
mysum=`expr $a + $b`
echo $mysum 