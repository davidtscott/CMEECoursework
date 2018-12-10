#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  November 2018
# Description: Plots data and outputs list of species to csv

## packages ##
rm(list = ls()) 
graphics.off() 

# Plots log(field metabolic rate) against log(body mass) for the Nagy et al 
# 1999 dataset to a file fmr.pdf.
# Writes the list of species names to species.csv

cat("Reading CSV\n") # prints to bash 

# loads csv data to nagy
nagy <- read.csv('../Data/NagyEtAl1999.csv', stringsAsFactors = FALSE)

cat("Creating graph\n")
pdf('../Results/fmr_plot.pdf', 11, 8.5) # opens pdf to save graph to
col <- c(Aves='purple3', Mammalia='red3', Reptilia='green3')  # defines colours
# plots log body mass vs log metablic rate
plot(log10(nagy$M.g), log10(nagy$FMR.kJ.day.1), pch=19, col=col[nagy$Class], # colour by class  
     xlab=~log[10](M), ylab=~log[10](FMR)) 
for(class in unique(nagy$Class)){  # linear model for each class subset
    model <- lm(log10(FMR.kJ.day.1) ~ log10(M.g), data=nagy[nagy$Class==class,])
    abline(model, col=col[class]) # adds line to graph 
}
dev.off() # clears graphs

cat("Finished in R!\n")
