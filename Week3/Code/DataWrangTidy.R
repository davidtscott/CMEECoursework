#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: Data wrangling in R with tidyr and dplyr

rm(list=ls()) # clears workspace
graphics.off() # clears graphics

## packages ##
require(dplyr)
require(tidyr)
require(reshape2) # load the reshape2 package

################################################################
################## Wrangling the Pound Hill Dataset ############
################################################################

## Script edited to use dplyr and tidyr packages 
##   instead of reshape2 and base R
# Old code left in to but hashed out, to show compare methodology

############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F)) 

# header = true because we do have metadata headers
MyMetaData <- read.csv("../Data/PoundHillMetaData.csv",header = T, sep=";", stringsAsFactors = F)

############# Inspect the dataset ###############

#head(MyData) # prints first 6 rows and headers
dplyr::tbl_df(MyData) #like head()
#dim(MyData) # prints dimensions
dplyr::dim_desc(MyData) #like dim()
#str(MyData) # prints structure
dplyr::glimpse(MyData) #like str()
#fix(MyData) #you can also do this
utils::View(MyData) #same as fix()
#fix(MyMetaData)
utils::View(MyMetaData) #same as fix()

############# Transpose ###############
# To get those species into columns and treatments into rows 
MyData <- t(MyData) 
#head(MyData)
dplyr::tbl_df(MyData) #like head()
#dim(MyData)
dplyr::dim_desc(MyData) #like dim()

############# Replace species absences with zeros ###############
MyData[MyData == ""] = 0

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!
colnames(TempData) <- MyData[1,] # assign column names from original data

rownames(TempData) <- NULL  # removes row names
#head(TempData)
dplyr::tbl_df(TempData) #like head()
############# Convert from wide to long format  ###############

#?melt #check out the melt function
#?gather #check out the gather function from tidyr package

#MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")
MyWrangledData <- TempData %>% tidyr::gather(., Species, count, -Cultivation, -Block, -Plot, -Quadrat) %>% mutate(Cultivation = as.factor(Cultivation), Block = as.factor(Block), Plot = as.factor(Plot), Quadrat = as.factor(Quadrat), count = as.integer(count))
# pipes data from TempData to tidyr function gather (alternative to melt function)
# assigns variables, -
# pipe to mutate function and change them into factors and integer variables. 

# melt collapses daat in wide format and stacks it into singl column
#head(MyWrangledData); tail(MyWrangledData)
dplyr::tbl_df(MyWrangledData); tail(MyWrangledData)

# assign the correct data type of each row
#MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
#MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
#MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
#MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
#MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])
#as.factor creates a factor column

#str(MyWrangledData)
dplyr::glimpse(MyWrangledData) #like str()
#head(MyWrangledData)
dplyr::tbl_df(MyWrangledData) #like head()
#dim(MyWrangledData)
dplyr::dim_desc(MyWrangledData) #like dim()

############# Exploring the data (extend the script below)  ###############

# from plyr to dplyr
# from reshape2 to tidyr

dplyr::tbl_df(MyWrangledData) #like head()
dplyr::glimpse(MyWrangledData) #like str()
utils::View(MyWrangledData) #same as fix()
dplyr::filter(MyWrangledData, count > 100) #like subset()
dplyr::slice(MyWrangledData, 10:15) # Look at an arbitrary set of data rows
