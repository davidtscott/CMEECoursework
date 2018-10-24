#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 24 2018
# Description: calculates autocorrelation of time series mean temperature data

rm(list=ls()) # clears workspace

#Temperature data from Key West, Florida for 21st Century
# yeasr 1901 to 2000
load("../Data/KeyWestAnnualMeanTemperature.RData")
# loads data from data directory
# .RData taken from mulquo course page

#ats is automatic name for data from a .RData file

TempData <- ats #assigns to variable TempData
print(TempData) #print data
#copied from downloaded version
# wget https://.... gave error

str(TempData)
head(TempData) 
tail(TempData)
names(TempData) # prints column names

plot(TempData) #plot data
print("Plotted TempData")

print("Each year temperature was recorded:")
TempData[,1] # prints column 1 (years)
print("Each temperature recorded:")
TempData[,2]

keytemps <- TempData[,2] #assigns mean temperature (without corresponding year)
# to keytemps

######### AUTOCORRELATION #########
?cor()
#autocorrelation to asses if time series (mean temp)
# is dependent on its past 
# look at pairs. in this case 100 observations = 99 pairs
# pairs take form of (x[t],x[t-1])
# t is observatin index
# varies from 2 to 100 
# estimated sample correlation of these pairs is the lag-1 autocorrelation
#  of our data keytemps. 

#### create pairs of observations #####
# two vectors each of lenth n-1 (100 - 1)
#   thus rows are (x[t],x[t-1])

# Defines x_t0 as vector x[-1]
x_t0 <- keytemps[-1]

# Defines x_t1 as vector x[-n]
x_t1 <- keytemps[-100]

# Confirms that x_t0 and x_t1 are (x[t], x[t-1]) pairs  
head(cbind(x_t0, x_t1))

# Plots x_t0 and x_t1
plot(x_t0, x_t1)
print("Plotted (x_t0, x_t1)")

# View the correlation between x_t0 and x_t1
# apply cor() function to estimate lag-1 autocorrelation 
autocor <- cor(x_t0, x_t1)
print(paste("lag -1 autocorrelation of mean temperatures:", autocor))

### ALTERNTIVE METHOD (not base R) ##
# Use acf with x
#lag.max = 1 creates a single lag period
#acf(keytemps, lag.max = 1, plot = FALSE)

# difference between method above and alternatve method
# Confirm that difference factor is (n-1)/n 
# cor(x_t1, x_t0) * (100-1)/100

corfun <- function(keytemps){
  y_t0 <- sample(keytemps[-1], replace = TRUE)
  y_t1 <- sample(keytemps[-100], replace = TRUE)
  cor(y_t0, y_t1)
}
# function defined that creates (x[t],x[t-1]) pairs as above
# from keytemps and does so randomly
# generating random permutations
result <- lapply(1:10000, function(i) corfun(keytemps))
#  lapply function feeds corfun function 10,000 times with key temps data
# stores data for ech randomly permutated year sequence and stores it
result.numeric <- as.numeric(result)
# mutates results to numeric

print(result.numeric)

hist(result.numeric, col="gray", xlab="AutoCorrelations", main="KeyWest Temp Data (1901 - 2000)")
# histogram of results with heading and labels
abline(v = autocor, col = "red", lwd = 2)
#add abline to show where the initial correlation fell inrelation to the 10000

#par(mfrow = c(1,1))

length(result.numeric[result.numeric > autocor])/length((result.numeric)) 
# calculates the fraction of result.numeric (result from 10,000 random permutations)
# greater than first autocorrelation (autocor)
# used as an approximate p - value

# By looking at the abline i appears the intial correlation result autocor) 
# falls within 5% confidence interval 
# thus 95% confident not random. 

