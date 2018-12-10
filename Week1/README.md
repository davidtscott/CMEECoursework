# README Document for CMEECourseWork Week1
## Author: David Scott - _david.scott18@imperial.ac.uk_
## Date: _OCT - 2018_

### Description: [All files created using bash (Ubunto Linux distribution), LaTeX and bibtex as part of CMEE Week1. All code, data and results contained in their respective directories. A map of all directories and files is provded below. Scripts either call from data directory or are written with a variable, in such a case use command line: bash SCRIPTNAME.sh ../Data/FILENAME.]

### Map of directories with short description of each script.
```
.
├── Code
│   ├── boilerplate.sh :           Simple boilerplate for shell scripts.
│   ├── CompileLaTeX.sh :          Compile LaTeX with bibtex.
│   ├── ConcatenateTwoFiles.sh :   Merges two files (variables $1, $2).
│   ├── CountLines.sh :            Counts the number of lines in a file, assigns cout to a variable.
│   ├── csvtospace.sh :            Substitute a comma for a space, creating a new .txt version of file. 
│   ├── FirstBiblio.bib :          Reference Example.
│   ├── FirstExample.tex :         A simple Document.
│   ├── MyExampleScript.sh :       Example script printing using variables.
│   ├── tabtocsv.sh :              substitute the tabs in the files with commas.
│   ├── tiff2png.sh :              Converts a .tif file to a .png file.
│   ├── TranslateEg.sh :           Remove spaces, letters, change case.
│   ├── UnixPrac1.txt              Answers to Week1 fasta practical 
│   └── variables.sh :             Shell script. 
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
├── README.tmp                    
├── Results
│   └── FirstExample.pdf           .gitignored
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

```
