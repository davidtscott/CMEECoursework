#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: Trigonometric function to calculate tree height 

rm(list=ls()) # clears workspace
graphics.off() # clears graphics


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


# import data with headers
# using read.csv function. File path goes to Data directory
MyData <- read.csv("../Data/trees.csv", header = TRUE)


#functin using degrees to calculate radians 
#   and radian with distance to calculate height. 
TreeHeight <- function(degrees, distance){
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    #print(paste("Tree height is:", height))
    return (height)
}

#creates a data frome (TreeDF) with data from 
# MyData (imported at beginning from trees.csv)
# and calls function TreeHeight defined above
# calls it with MyData column 3 (degrees) and MyData column 2 (distance)
# and thus appends output of function from two inputs with MyData
TreeDF <- data.frame(MyData, TreeHeight(MyData[3], MyData[2]))
colnames(TreeDF)[4] <- "Tree.Height.m"
# names column 4 containing output of function as "Tree.Height.m"

write.csv(TreeDF, "../Results/TreeHts.csv", row.names = FALSE)
print("Results saved to '../Results/TreeHts.csv'")
#write TreeDF data frame to a csv file called TreeHts.csv in Results directory
# does not include row names

# {} curly brackets required for multi line statements.
