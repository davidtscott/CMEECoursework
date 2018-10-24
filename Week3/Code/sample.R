#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: run a simulation that involves sampling from a population

rm(list=ls()) # clears workspace


x <- rnorm(50) #Generate your population
doit <- function(x){
  x <- sample(x, replace = TRUE)
  if(length(unique(x)) > 30) { #only take mean if sample was sufficient
    print(paste("Mean of this sample was:", as.character(mean(x))))}
  }

## Run 100 iterations using vectorization:
result <- lapply(1:100, function(i) doit(x))

## Or using a for loop: 
result <- vector("list", 100) #Preallocate/Initialize
for(i in 1:100){
  results[[i]] <- doit(x)
}
