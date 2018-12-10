#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: sums all elements of a matrix 

rm(list=ls()) # clears workspace
graphics.off() # clears graphics

# creates matix of uniform distribution 
M <- matrix(runif(1000000),1000,1000)

SumAllElements <- function(M){
  Dimensions <- dim(M)
  Tot <- 0
  for (i in 1:Dimensions[1]){
    for (j in 1:Dimensions[2]){
      Tot <- Tot + M[i,j]
    }
  }
  return (Tot)
}

## This on my computer takes about 1 sec
print("Speed of SumAllElements function defined using loops:")
print(system.time(SumAllElements(M)))

## While this takes about 0.01 sec
print("Speed of sum function without loops:")
print(system.time(sum(M)))

#system.time function calculates time taken by code
#sum() function 100 times faster than SumAllElements()
# as it uses vectorisation, avoiding the amount of loops used by SumAllElements
