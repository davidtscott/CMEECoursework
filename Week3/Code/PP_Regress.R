#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 29 2018
# Description: Linear Regression with plots. Faceted by 2 variables

rm(list = ls()) #clears workspaces
graphics.off() #clears any images

## Packages
library(ggplot2)
library(plyr)
library(dplyr)

# read data from file to dataframe
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv", stringsAsFactors=FALSE)

#initiate plot and assign data to variables
#subset graph by Type of feeding interactio and colour by Predator.lifestage
p <- ggplot(MyDF, aes(x = Prey.mass, y = Predator.mass, colour = Predator.lifestage)) +
      facet_grid(rows = vars(Type.of.feeding.interaction))

# add points of shape 3(crosses) and regression lines with standard error. 
# adjusted length and width of line.
p <- p + geom_point(shape = 3) + geom_smooth(method = "lm", se=TRUE, fullrange=TRUE, size = 0.5) 

# changed x and y axis to log10 and added labels
p <- p + scale_x_log10() + scale_y_log10() + xlab("Prey Mass in grams") + ylab("Predator mass in grams") 

# changes theme to black and white
# moves legned to bottom and displays in one row
p <- p + theme_bw() + theme(legend.position = "bottom") + guides(colour = guide_legend(nrow = 1))

# Open blank pdf page using a relative path
pdf("../Results/PP_Regress.pdf", 11.7, 8.3)
print(p)

#calculate reg results for fitted lines in each subset of data 
#fitted_models <- MyDF %>% group_by(Type.of.feeding.interaction, Predator.lifestage) %>% do(model = lm(Predator.mass ~ Prey.mass, data = .))

#fitted_models$model
#library(broom)
#a <- fitted_models %>% tidy(model) 
#b <- fitted_models %>% glance(model) 


## calculate reg results for fitted lines in each subset of data 
LinearOutput <- dlply(MyDF,.(Type.of.feeding.interaction, Predator.lifestage), function(x) lm(Predator.mass~Prey.mass, data = x))

# Extract Coeffieciets r2, intercept, slope and p value
CoefOut <- ldply (LinearOutput, function(x) {
  intercept <- summary(x)$coefficients[1]
  slope <- summary(x)$coefficients[2]
  p.value <- summary(x)$coefficients[8]
  r2 <- summary(x)$r.squared
  data.frame(r2, intercept, slope, p.value)})

# Extract F statistic
F.statistic <- ldply(LinearOutput, function(x) summary(x)$fstatistic[1])

# Merge F stat with rest of coefficients into one dataframe
OutputDF <- merge(CoefOut, F.statistic, by = c("Type.of.feeding.interaction", "Predator.lifestage"), all = TRUE)

# change name of 7th columm
names(OutputDF)[7] <- "F.statistic"

# write results to a csv file in the results directory 
write.csv(OutputDF, "../Results/PP_Regress_Results.csv", row.names = FALSE, quote = FALSE)

#?write.csv
