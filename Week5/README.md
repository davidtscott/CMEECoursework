# README Document for CMEECourseWork Week5
## Author: David Scott- _david.scott18@imperial.ac.uk_
## Date: _Nov - 2018_

### Description: [CMEE coursework for Week5, introduction to spatial data analysis. All work was done using QGIS oen source software. gitignored all files above 10mb in size, available on request.]

### Tree map
```
.
├── Code
│   └── QGIS_Prac1.py : Script to convert bioclim temperature and rainfall data and CORINE landcover files into a shared projection and resolution (BNG 2km grid) and then extract mean climatic values within land cover classes  Code is PEP8 compliant: https://www.python.org/dev/peps/pep-0008
├── Data
│   ├── Borneo
│   │   ├── MODIS_blue_reflectance.tif            .gitignored
│   │   ├── MODIS_blue_reflectance.tif.aux.xml
│   │   ├── MODIS_NIR_reflectance.tif             .gitignored
│   │   ├── MODIS_NIR_reflectance.tif.aux.xml
│   │   ├── MODIS_red_reflectance.tif             .gitignored
│   │   ├── MODIS_red_reflectance.tif.aux.xml
│   │   ├── SAFE_layout_UTM50N_WGS84.dbf
│   │   ├── SAFE_layout_UTM50N_WGS84.prj
│   │   ├── SAFE_layout_UTM50N_WGS84.shp
│   │   └── SAFE_layout_UTM50N_WGS84.shx
│   ├── EU
│   │   ├── bio1_15.tif                 .gitignored
│   │   ├── bio1_16.tif                 .gitignored
│   │   ├── bio12_15.tif                .gitignored
│   │   ├── bio12_16.tif                .gitignored
│   │   ├── bio12_UK_BNG.tif
│   │   ├── bio1_UK_BNG.tif
│   │   ├── clc_legend_qgis.txt
│   │   ├── g250_06.tif                 .gitignored
│   │   ├── G250_06_UK_BNG.tif
│   │   └── zonalstats.csv
│   ├── Global
│   │   ├── Background.dbf
│   │   ├── Background.prj
│   │   ├── Background.shp
│   │   ├── Background.shx
│   │   ├── bio12.bil
│   │   ├── bio12.hdr
│   │   ├── bio1.bil
│   │   ├── bio1.hdr
│   │   ├── cntry98.dbf
│   │   ├── cntry98.prj
│   │   ├── cntry98.shp
│   │   ├── cntry98.shx
│   │   ├── tissot.dbf
│   │   ├── tissot.prj
│   │   ├── tissot.shp
│   │   └── tissot.shx
├── README.md
├── Results
└── Sandbox

7 directories, 39 files

```
