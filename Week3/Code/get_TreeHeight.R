#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: Calc. tree height: input file from command line, outputs to csv

rm(list=ls()) # clears workspace
graphics.off() # clears graphics

## packages ##
library(tools)

args = commandArgs(trailingOnly=TRUE)
# enables command line arguments

# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

# test if there is at least one argument given in command line: 
# if not, return an error
if (length(args)==0) {
  stop("At least one argument must be supplied (input file).", call.=FALSE)
} 

MyData <- read.csv(args[1], header = TRUE) # import with headers
#reads content of a csv file given in command line (argument one)
# assigns content to MyData variable

#functin using degrees to calculate radians 
#   and radian with distance to calculate height. 
TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  #print(paste("Tree height is:", height))
  return (height)
}

#creates a data frome (TreeDF) with data from MyData 
# and calls function TreeHeight defined above
# calls it with MyData column 3 (degrees) and MyData column 2 (distance)
# and thus appends output of function from two inputs with MyData
TreeDF <- data.frame(MyData, TreeHeight(MyData[3], MyData[2]))
colnames(TreeDF)[4] <- "Tree.Height.m"
# names column 4 containing output of function as "Tree.Height.m"


# strip extension and file path from file given as agrument one in command line
inputfile_name <- file_path_sans_ext(basename(args[1]))
# paste new file path , extension  together and assigns to variable
outputfile_name <- paste("../Results/", inputfile_name, "_treeheights.csv", sep = "")
# saves dataframe (TreeDF) to file named above.
write.csv(TreeDF, outputfile_name, row.names = FALSE)
#prints new name of output file
print(paste("Saved output to csv file:", outputfile_name))
