#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 26 2018
# Description: Lattice graphs with mean and median calc. by factor 

rm(list = ls()) # clears workspace
graphics.off() # closes all open graphics

## Packages ##
library(lattice)
library(plyr)
library(dplyr)
require(tidyr)

## load data
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")

## examine dataframe
# dim(MyDF)
# str(MyDF)
# head(MyDF)
# names(MyDF)

## draws and saves three lattic graphs by feding interaction type
# use of log of masses (or mass-ratios) for all three

## predator mass:   Pred_Lattice.pdf
pdf("../Results/Pred_Lattice.pdf") #11.7, 8.3) 
# Open blank pdf page using a relative path and specifies page dimensions in inches
print(densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF, 
    xlab="Log Predator Mass (g)", main="Density Plot by Feeding Interaction Type", col="purple"))
dev.off()         

## prey mass:      Prey_Lattice.pdf
pdf("../Results/Prey_Lattice.pdf") # 11.7, 8.3) 
print(densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data=MyDF,
    main= "Density Plot by Feeding Interaction Type", xlab="Log Prey Mass (g)", col="purple"))
     # scales=list(cex=1.2, col="red")
dev.off() 

## size ratio of predator mass over prey mass:   SizeRatio_Lattice.pdf
pdf("../Results/SizeRatio_Lattice.pdf") # 11.7, 8.3) 
print(densityplot(~(log(Predator.mass/Prey.mass)) | Type.of.feeding.interaction, data=MyDF,
    main= "Density Plot by Feeding Interaction Type", xlab="Log Pred/Prey Size Ratio (g)", col="purple"))
dev.off()

# Calculated mean and meadian log pred mass, prey mass, and pred prey size ratio, by feeding type

## Mean and median of log predator mass
#Mean
LogPredMean <- ddply(MyDF, .(Type.of.feeding.interaction), summarize, Pred.Mean=mean(log(Predator.mass)))
#Median
LogPredMedian <- ddply(MyDF, .(Type.of.feeding.interaction), summarize, Pred.Median=median(log(Predator.mass)))
#join both
LogPred <- join(LogPredMean, LogPredMedian, type ="inner")

## Mean and median of log prey mass
LogPreyMean <- ddply(MyDF, .(Type.of.feeding.interaction), summarize, Prey.Mean=mean(log(Prey.mass)))
LogPreyMedian <- ddply(MyDF, .(Type.of.feeding.interaction), summarize, Prey.Median=median(log(Prey.mass)))
LogPrey <- join(LogPreyMean, LogPreyMedian, type ="inner")

# join median and mean of log prey with that of log predator
LogPredPrey <- join(LogPred, LogPrey, type ="inner")

# Mean and median of log ratio mass
LogRatioMean <- ddply(MyDF, .(Type.of.feeding.interaction), summarize, Pred.Prey.Ratio.Mean=mean(log(Predator.mass/Prey.mass)))
LogRatioMedian <- ddply(MyDF, .(Type.of.feeding.interaction), summarize, Pred.Prey.Ratio.Median=median(log(Predator.mass/Prey.mass)))
LogRatio <- join(LogRatioMean, LogRatioMedian, type ="inner")

# join previous two joined with that fo ration. Created final dataframe
LogDF <- join(LogPredPrey, LogRatio, type ="inner")
#print(LogDF)
# output results to a csv
write.csv(LogDF, "../Results/PP_Results.csv", row.names = FALSE)
