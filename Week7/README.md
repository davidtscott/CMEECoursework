# README Document for CMEECourseWork Week7
## Author: David Scott - _david.scott18@imperial.ac.uk_
## Date: _NOV - 2018_

### Description: [Biological Computing in Python 2. All scripts were written in visual studio code for python3 or Rstudio for R. Scripts stored in code directory and use relative paths to call data from Data and direct outputs to Results.]

### Map of directories with short description of each script. 
```
.
├── Code
│   ├── blackbirds.py :                         Using regex in python.
│   ├── DrawFW.py :                             Creates and plots a synthetic food web network.
│   ├── fmr.R :                                 Plots data and outputs list of species to csv\r. '
│   ├── LV1.py :                                Lotka-Volterra numerical integration model, generates two figures.
│   ├── LV2.py :                                L-V model, takes parameter values from command line. Has defaults also.  
│   ├── LV3.py :                                Discrete time version of L-V model.
│   ├── LV4.py :                                Discrete time version of L-V model with random gausian fluctuation.
│   ├── Nets.R :                                Plots network using igraph in R.'
│   ├── profileme2.py :                         Second example of profiling functions in python.
│   ├── profileme.py :                          Example of profiling functions in python.
│   ├── regexs.py :                             Example uses of regex in python. 
│   ├── run_fmr_R.py :                          Use of subprocess to run Rscript fmr.R. Prints 'Succesful' if succesful
│   ├── RunLV.sh :                              Runs three scipts, LV1.py LV2.py and LV3.py and checks speed '
│   ├── TestR.py :                              Example script to run an Rscript from python using subprocess module
│   ├── TestR.R :                               Rscript for demonstrating subprocces in python '
│   ├── timeitme.py :                           Example of timeit module in python.  Imports modules from profileme and profileme2.
│   └── using_os.py :                           Use the subprocess.os module to get list of files and  directories  in ubuntu home directory. 
├── Data
│   ├── blackbirds.txt
│   ├── NagyEtAl1999.csv
│   ├── QMEE_Net_Mat_edges.csv
│   ├── QMEE_Net_Mat_nodes.csv
│   └── TestOaksData.csv
├── README.tmp
├── Results
│   ├── fmr_plot.pdf                          .gitignored
│   ├── LV2_model2.pdf                        .gitignored
│   ├── LV2_model.pdf                         .gitignored
│   ├── LV3_model1.pdf                        .gitignored
│   ├── LV3_model2.pdf                        .gitignored
│   ├── LV4_model1.pdf                        .gitignored
│   ├── LV4_model2.pdf                        .gitignored
│   ├── LV_model2.pdf                         .gitignored
│   ├── LV_model.pdf                          .gitignored
│   └── QMEENet.svg                           .gitignored
└── Sandbox

4 directories, 33 files

```
