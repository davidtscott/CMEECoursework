# README Document for CMEECourseWork Week7
## Author: David Scott - _david.scott18@imperial.ac.uk_
## Date: _Nov - 2018_

### Description:  [CMEE Coursework for Week7 - Python2. All scripts were written in visual studio code for python3 or Rstudio. Scripts stored in code directory and use relative paths to call data from Data and direct outputs to Results.]


### Map of directories with short description of each file. 
```
.
├── Code
│   ├── blackbirds.py : Using regex in python.
│   ├── DrawFW.py : Creates and plots a synthetic food web network
│   ├── fmr.R :  Rscript for use in subproccessing in python
│   ├── LV1.py : Lotka Volterra numerical integration model
│   ├── LV2.py : L-V model, takes parameter values from command line 
│   ├── LV3.py : Discrete time version of L-V model 
│   ├── MyFirstJupyterNb.ipynb
│   ├── Nets.R : Network in R
│   ├── profileme2.py : Second example of profiling functions in python
│   ├── profileme.py : Example of profiling functions in python
│   ├── __pycache__
│   │   ├── blackbirds.cpython-35.pyc                   .gitignored
│   │   ├── profileme2.cpython-35.pyc			.gitignored
│   │   └── profileme.cpython-35.pyc			.gitignored
│   ├── regexs.py : Example uses of regex in python. 
│   ├── run_fmr_R.py : Use of subprocess to run Rscript. Prints 'Succesful' if succesful
│   ├── RunLV.sh : Runs three scipts, LV1.py LV2.py and LV3.py and checks speed '
│   ├── TestR.py : Example script to run an Rscript from python using subprocess module
│   ├── TestR.R : Rscript for demonstrating subprocces in python '
│   ├── timeitme.py : Example of timeit module in python.  Imports modules from profileme and profileme2.
│   └── using_os.py : Use the subprocess.os module to get list of files and  directories  in ubuntu home directory. 
├── Data
│   ├── blackbirds.txt
│   ├── NagyEtAl1999.csv
│   ├── QMEE_Net_Mat_edges.csv
│   ├── QMEE_Net_Mat_nodes.csv
│   └── TestOaksData.csv
├── README.md
├── Results
│   ├── DrawFW.pdf			.gitignored
│   ├── fmr_errFile.Rout		.gitignored
│   ├── fmr_plot.pdf			.gitignored
│   ├── fmr.R : b''out			.gitignored
│   ├── LV2_model2.pdf			.gitignored
│   ├── LV2_model.pdf			.gitignored
│   ├── LV3_model1.pdf			.gitignored
│   ├── LV3_model2.pdf			.gitignored
│   ├── LV_model2.pdf			.gitignored
│   ├── LV_model.pdf			.gitignored
│   └── QMEENet.svg			.gitignored
└── Sandbox

5 directories, 38 files

```