#!/usr/bin/env Rscript
# Author: David Scott
# Contact: david.scott18@imperial.ac.uk
# Date:  October 29 2018
# Description: Girko's Law Simulation

rm(list = ls()) 
graphics.off() 

## packages##
library(ggplot2)

# function that returns an ellipse
build_ellipse <- function(hradius, vradius){ 
  npoints = 250
  a <- seq(0, 2 * pi, length = npoints + 1)
  x <- hradius * cos(a)
  y <- vradius * sin(a)  
  return(data.frame(x = x, y = y))
}

# Assign size of the matrix
N <- 250 

# Build the matrix
M <- matrix(rnorm(N * N), N, N) 

# Find the eigenvalues
eigvals <- eigen(M)$values 

# Build a dataframe
eigDF <- data.frame("Real" = Re(eigvals), "Imaginary" = Im(eigvals)) 

# The radius of the circle is sqrt(N)
my_radius <- sqrt(N) 

# Dataframe to plot the ellipse
ellDF <- build_ellipse(my_radius, my_radius) 

# rename the columns
names(ellDF) <- c("Real", "Imaginary") 

# Plot the eigenvalues
p <- ggplot(eigDF, aes(x = Real, y = Imaginary))
p <- p + geom_point(shape = I(3)) + theme(legend.position = "none")

# Add the vertical and horizontal line
p <- p + geom_hline(aes(yintercept = 0))
p <- p + geom_vline(aes(xintercept = 0))

# Add the ellipse
p <- p + geom_polygon(data = ellDF, aes(x = Real, y = Imaginary, alpha = 1/20, fill = "red"))

# Save as pdf, Open blank pdf page using a relative path
pdf("../Results/Girko.pdf") 
print(p)
graphics.off() 
