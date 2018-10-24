#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: creates a world map and plots data points using maps package

rm(list=ls()) # clears workspace

library(maps)
# loads maps package

load("../Data/GPDDFiltered.RData") #loads data from Data directory

names(gpdd)
head(gpdd)

lat <- gpdd[,2] # comma puts columns and not default row 
print("The Latitude coordinates are:")
print(lat) # lattitude data assigned to variable lat

long <- gpdd[,3] # comma puts columns and not default row 
print("The Longitudinal coordinates are:")
print(long) # longitude data assigned to variable long

map("world", fill=TRUE, col="white", bg="lightblue", ylim=c(-60, 90), mar=c(0,0,0,0))
# map funtions creates a base map of the "world". 
points(long,lat, col="purple", pch=16)
# points funtion plots location of species using longitude (long) and latitude (lat) data
#   on world map previous created

# most of the data is in the western countries.
# In europe, cluster occurs in Britain. 
# Also within countries where sampling occurs there are clusters observed.
# for example USA, dense clustering occurs along west coast as compared with the other regions,
# such as the east coast, southern and mid western states. 
# Thus there is a strong sample bias and is therefore not representative 
# of global vertebrate populations. 

