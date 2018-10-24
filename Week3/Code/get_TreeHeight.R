#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: calculates tree heght using trigonmenric function. take input file from command line. outputs results to csv

rm(list=ls()) # clears workspace

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

# test if there is at least one argument given in command line: if not, return an error
if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
} 

MyData <- read.csv(args[1], header = TRUE) # import with headers
#reads content of a csv file given in command line (argument one)
# assigns content to MyData variable

#functin using degrees to calculate radians 
#   and radian with distance to calculate height. 
TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  print(paste("Tree height is:", height))
  return (height)
}

#creates a data frome (TreeDF) with data from MyData (imported at beginning from trees.csv)
# and calls function TreeHeight defined above
# calls it with MyData column 3 (degrees) and MyData column 2 (distance)
# and thus appends output of function from two inputs with MyData
TreeDF <- data.frame(MyData, TreeHeight(MyData[3], MyData[2]))
colnames(TreeDF)[4] <- "Tree.Height.m"
# names column 4 containing output of function as "Tree.Height.m"

library(tools)
inputfile_name <- file_path_sans_ext(basename(args[1]))
# strips the extension and file path from file given as agrument one in command line
outputfile_name <- paste("../Results/", inputfile_name, "_treeheights.csv", sep = "")
# paste new file path , extension and addition to name together and assigns to variable
print(outputfile_name)#prints new name of output file
write.csv(TreeDF, outputfile_name, row.names = FALSE)
# saves dataframe (TreeDF) to file named above. 

