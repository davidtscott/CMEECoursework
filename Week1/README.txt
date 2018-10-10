Author: David Scott David.Scott18@imperial.ac.uk
Desc: README file outlining subdirectories and content of Week1 directory
Date: Oct 2018

Summary: 
All files created using Ubunto, LaTex and bibtex as part of CMEE week 1. 
All code data and results are contained in their respective directories. 
Scripts either call from data directory or are written with a variable, in such case use bash SCRIPTNAME.sh ../Data/FILENAME

.
├── Code
│   ├── boilerplate.sh 		   Simple boilerplate for shell scripts
│   ├── CompileLaTeX.sh		   Compile LaTeX with bibtex
│   ├── ConcatenateTwoFiles.sh	   Merges two files
│   ├── CountLines.sh              Counts lines within a file
│   ├── csvtospace.sh		   Converts a comma seperated file to a space seperated file
│   ├── FirstBiblio.bib		   Example of a biblio reference
│   ├── FirstExample.tex	   Example of a LaTeX script
│   ├── MyExampleScript.sh	   Example shell script using variables
│   ├── tabtocsv.sh		   Converts a tab seperated file to a comma seprated file
│   ├── tiff2png.sh		   Converts a .tif file to a .png file
│   ├── TranslateEg.sh		   Three uses of the translate (tr) command: Remove spaces, letters, change case
│   ├── UnixPrac1.txt		   First CMEE practical for Unix. Questions, answers and comments included.
│   └── variables.sh		   Shell script using variables
├── Data
│   ├── fasta
│   │   ├── 407228326.fasta
│   │   ├── 407228412.fasta
│   │   └── E.coli.fasta
│   ├── spawannxs.txt
│   └── Temperatures
│       ├── 1800.csv
│       ├── 1800.txt
│       ├── 1801.csv
│       ├── 1801.txt
│       ├── 1802.csv
│       ├── 1802.txt
│       ├── 1803.csv
│       └── 1803.txt
├── README.txt
├── Results                	   All outputs will be directed here. Contains gitignore file, thus empty repository.  
│   └── FirstExample.pdf   	   LaTeX output pdf 
└── Sandbox
    ├── ListRootDir.txt
    ├── Sandbox.test.txt
    ├── TestFile
    ├── TestFind
    │   ├── Dir1
    │   │   ├── Dir11
    │   │   │   └── Dir111
    │   │   │       └── File111.txt
    │   │   ├── File1.csv
    │   │   ├── File1.tex
    │   │   └── File1.txt
    │   ├── Dir2
    │   │   ├── File2.csv
    │   │   ├── File2.tex
    │   │   └── File2.txt
    │   └── Dir3
    │       └── File3.txt
    ├── test.txt
    ├── test.txt.csv
    └── TestWild
        ├── Anotherfile.csv
        ├── Anotherfile.txt
        ├── File1.csv
        ├── File1txt
        ├── File2.csv
        ├── File2.txt
        ├── File3.csv
        ├── File3.txt
        ├── File4.csv
        └── File4.txt

13 directories, 50 files

