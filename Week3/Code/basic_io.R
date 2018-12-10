#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: A simple script to illustrate R input-output

rm(list=ls()) # clears workspace
graphics.off() # clears graphics

# Run line by line and check inputs outputs to understand what is happening

# import with headers
MyData <- read.csv("../Data/trees.csv", header = TRUE) 

#write it out as a new file
write.csv(MyData, "../Results/MyData.csv") 

# Append to it 
write.table(MyData[1,], file = "../Results/MyData.csv", append=TRUE, col.names = FALSE) 

# write row names
write.csv(MyData, "../Results/MyData.csv", row.names = TRUE) 

 # ignore column names
write.table(MyData, "../Results/MyData.csv", col.names = FALSE) 
