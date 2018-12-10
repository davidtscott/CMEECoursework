#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: Example boilerplate in R

rm(list=ls()) # clears workspace
graphics.off() # clears graphics

# A boilerplate R script 

MyFunction <- function(Arg1, Arg2){
    # Statements involving Arg1, Arg2:
    print(paste("Argument", as.character(Arg1), "is a", class(Arg1))) # print Arg1's type
    print(paste("Argument", as.character(Arg2), "is a", class(Arg2))) # print Arg2's type
    
    return (c(Arg1, Arg2)) #this is optional, but very useful 
}

MyFunction(1,2) #test the function
MyFunction("Riki", "Tiki") #A different test

# {} brackets tell R where specification of function start and end
# indentation not required like in python
#   but make code more readable
