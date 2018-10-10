#!/bin/bash
# Author: David Scott David.Scott18@imperial.ac.uk
# Script: MyExampleScript.sh
# Desc: Example script printing using variables
# Arguments: 1 $USER for username 
# Date: Oct 2018

msg1="Hello" #creates variable and assigns string "Hello" to variable 
msg2=$USER #creates variable and assigns variable $USER which displays username
echo "$msg1 $msg2" #prints variables created
echo "Hello $USER" #prints "Hello" and $USER from variable input. thus same thing printed twice 
			# using different techniques   
echo
