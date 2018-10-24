#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: use of break in functions

rm(list=ls()) # clears workspace

i <- 0 #initialize i
  while(i < Inf) {
    if (i == 20) {
      break
      } # Break out of the while loop!
    else {
      cat("i equals " , i , " \n")
      i <- i + 1 # Update i
    }
  }
