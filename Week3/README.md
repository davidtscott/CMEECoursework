# README Document for CMEECourseWork Week3
## Author: David Scott - _david.scott18@imperial.ac.uk_
## Date: _OCT - 2018_

### Description: Biological Computing in R & Data Management, Exploration and Visualisation in R. All R scipts were written with R studio. Scripts are stored in the Code directory and use relative paths to call data from the Data directory and all outputs are directed to the Results directory. Thus, set working directory to Code. NOTE: Data for GPDDmap.R and TAutoCorr.R were not pushed (.RData).

### Packages: ggplot2, tidyr, dplyr, plyr, lattice.

### Map of directories with short description of each script:
```
.
├── Code
│   ├── apply1.R :                                    Use of apply function '
│   ├── apply2.R :                                    Use of apply function '
│   ├── basic_io.R :                                  A simple script to illustrate R input-output '
│   ├── boilerplate.R :                               Example boilerplate in R '
│   ├── break.R :                                     Use of break in functions '
│   ├── browse.R :                                    Use of browse function '
│   ├── control.R :                                   Example of control flow constructs in R '
│   ├── DataWrang.R :                                 Wrangling data with base R and reshape2 package '
│   ├── DataWrangTidy.R :                             Data wrangling in R with tidyr and dplyr '
│   ├── get_TreeHeight.py :                           Calculates tree height using trigonometric function in python
│   ├── get_TreeHeight.R :                            Trigonometric function to calculate tree height  in R '
│   ├── Girko.R :                                     Girko's Law Simulation "
│   ├── GPDDmap.R :                                   Creates a world map and plots data points using maps package '
│   ├── MyBars.R :                                    Annotating Histogram '
│   ├── next.R :                                      Use of next in R functions '
│   ├── plotLin.R :                                   Mathematical Annotation '
│   ├── PP_Lattice.R :                                Lattice graphs with mean and median calc. by factor  '
│   ├── PP_Regress_loc.R :                            Linear regession . Faceted by 3 variables.  '
│   ├── PP_Regress.R :                                Linear Regression with plots. Faceted by 2 variables '
│   ├── preallocate.R :                               Vetorization example '
│   ├── run_get_TreeHeight.sh :                       Runs R and python3 scripts (both cal. tree height) '
│   ├── Run_Vectorize.sh :                            Compares speed of functions with and without vectorization(R & Python) '
│   ├── sample.R :                                    Run a simulation that involves sampling from a population '
│   ├── TAutoCorr.R :                                 Calculates autocorrelation of time series mean temperature data '
│   ├── TAutoCorr.tex :                               Time Series Autocorrelation of Key West Yearly Mean Tempertures (1901 - 2000) '
│   ├── TreeHeight.R :                                Trigonometric function to calculate tree height  '
│   ├── try.R :                                       Runs a simulation that involves sampling from a population with try '
│   ├── Vectorize1.py :                               Compares speed of two functions with and without vectorization
│   ├── Vectorize1.R :                                Sums all elements of a matrix  '
│   ├── Vectorize2.py :                               Compares speed of two Stochastic Ricker models with and without Vectorization
│   └── Vectorize2.R :                                Stochastic (Gaus.) Ricker Eqn with and without vectorization '
├── Data
│   ├── EcolArchives-E089-51-D1.csv
│   ├── GPDDFiltered.RData                          .gitignored
│   ├── KeyWestAnnualMeanTemperature.RData          .gitignored
│   ├── PoundHillData.csv
│   ├── PoundHillMetaData.csv
│   ├── Results.txt
│   └── trees.csv
├── README.tmp
├── Results
│   ├── Girko.pdf                                   .gitignored
│   ├── MyData.csv                                  .gitignored
│   ├── MyLinReg.pdf                                .gitignored
│   ├── PP_Regress.pdf                              .gitignored
│   ├── PP_Regress_Results.csv                      .gitignored
│   ├── PP_Results.csv                              .gitignored
│   ├── Pred_Lattice.pdf                            .gitignored
│   ├── Prey_Lattice.pdf                            .gitignored
│   ├── Rplots.pdf                                  .gitignored
│   ├── SizeRatio_Lattice.pdf                       .gitignored
│   ├── TAutoCorr_Histogram.pdf                     .gitignored
│   ├── TreeHts.csv                                 .gitignored
│   └── trees_treeheights.csv                       .gitignored
└── Sandbox

4 directories, 52 files

```
