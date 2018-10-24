#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date: October 2018
# Description: vetorization example

rm(list=ls()) # clears workspace

a <- NA
for (i in 1:100000) {
  a <- c(a, i)
}
print(a)
## This on my computer takes about 1 sec
print(system.time(SumAllElements(a)))
## While this takes about 0.01 sec
print(system.time(sum(a)))

########################

a <- rep(NA, 1000000)

for (i in 1:1000000) {
  a[i] <- i
}
print(a)
## This on my computer takes about 1 sec
print(system.time(SumAllElements(a)))
## While this takes about 0.01 sec
print(system.time(sum(a)))
