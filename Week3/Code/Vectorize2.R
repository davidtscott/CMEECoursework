#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date: October 2018
# Description: Runs the stochastic (with gaussian fluctuations) Ricker Eqn .

rm(list=ls())

stochrick<-function(p0=runif(1000,.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{                # runif here makes it stchastic
  #initialize
  N<-matrix(NA,numyears,length(p0))
  N[1,]<-p0
  
  for (pop in 1:length(p0)) #loop through the populations
  {   # each rep of for loop, R has to re-size the vector and reallocate memory
    for (yr in 2:numyears) #for each pop, loop through the years
    {
      N[yr,pop]<-N[yr-1,pop]*exp(r*(1-N[yr-1,pop]/K)+rnorm(1,0,sigma))
    }
  }
  return(N)

}

print("Stochastic Ricker takes:")
print(system.time(res2<-stochrick()))

# Now write another function called stochrickvect that vectorizes the above 
# to the extent possible, with improved performance: 

# vectorised 

rm(list=ls())

stochrickvect<-function(p0=runif(1000,.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{
  #initialize
  N<-matrix(NA,numyears,length(p0))
  N[1,]<-p0
    for (yr in 2:numyears) #for each pop, loop through the years
    {
      N[yr,]<-N[yr-1,]*exp(r*(1-N[yr-1,]/K)+rnorm(1,0,sigma))
  }
  return(N)
}
# removed pop loop and removed it from equation.
# years = t

print("Vectorized Stochastic Ricker takes:")
print(system.time(res2<-stochrickvect()))

