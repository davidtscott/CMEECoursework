#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 31 2018
# Description: Linear regession . Faceted by 3 variables. 

rm(list = ls()) 
graphics.off() 

## Packages
library(plyr)
library(dplyr)

# read data from file to dataframe
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv", stringsAsFactors=FALSE)

## calculate reg results for fitted lines in each subset of data 
LinearOutput2 <- dlply(MyDF,.(Type.of.feeding.interaction, Predator.lifestage, Location), function(x) lm(Predator.mass~Prey.mass, data = x))

# Extract Coeffieciets r2, intercept, slope and p value
CoefOut2 <- ldply (LinearOutput2, function(x) {
  intercept <- summary(x)$coefficients[1]
  slope <- summary(x)$coefficients[2]
  p.value <- summary(x)$coefficients[8]
  r2 <- summary(x)$r.squared
  data.frame(r2, intercept, slope, p.value)})

# Extract F statistic
F.statistic2 <- ldply(LinearOutput2, function(x) summary(x)$fstatistic[1])

# Merge F stat with rest of coefficients into one dataframe
OutputDF2 <- merge(CoefOut2, F.statistic2, by = c("Type.of.feeding.interaction", "Predator.lifestage", "Location"), all = TRUE)

# change name of 7th columm
names(OutputDF2)[7] <- "F.statistic"
OutputDF2
# write results to a csv file in the results directory 
write.csv(OutputDF2, "../Results/PP_Regress_loc_Results.csv", row.names = FALSE, quote = FALSE)
