# Coral Sea Oceanic Vegetation  (NESP MaC 2.3, AIMS)
Eric Lawrey, AIMS
This dataset is a vector shapefile mapping the deep vegetation on the bottom of the coral atoll lagoons in the Coral Sea. 

This repository contains a script to download all the public datasets used to map the vegetation. It also contains the QGIS files used to prepare the data and create the preview maps. It also contains scripts to perform the comparison between the vegetation mapping and drop camera surveys.

The input datasets are described in the `01-download-src-data.py` script.

See the [metadata record for this dataset](https://doi.org/10.26274/709g-aq12) for more information about this dataset and how it was produced.

## Input data
This repository contains an extract of the drop camera surveys conducted by JCU used for validation of the vegetation mapping. This is prepared from the original source data (which is not made available here) using the `02-drop-cam-data-prep.py` script. This produces an extract that only contains the data relevant for the validation of this dataset, align with metadata attributes. This data is stored in `public-src-data/CS_JCU_Tol_Drop-cam_Validation_Dec-2022.csv`. All other input data is not included in the repository due to the size of the data. It can be downloaded by running the `01-download-src-data.py` script.

`CS_AIMS_Oceanic-vegetation.qgz` corresponds to the QGIS file used for editing the dataset and preparing the preview maps.

## Validation
`03-vegetation-map-validation.py` This script performs the comparison between the drop camera results and the mapped oceanic vegetation.



## Area calculations
The areas of the mapped vegetation were produced using the following process:
1. The CS_NESP-MaC-2-3_AIMS_Oceanic-veg.shp was opened in QGIS. The area attribute was updated using the field calculator.
`round($area / 1e6, 3)`
2. The layer was exported as a CSV in working/CS_NESP-MaC-2-3_AIMS_Oceanic-veg.csv
3. This was opened in Excel and a pivot chart used to determine the area of each density classification.
Resulting in the following totals:
High density: 7192 km2
Medium density: 1409 km2
Low density: 360 km2
Total: 8961 km2

It should be noted that the boundary between the low and medium density was not strongly deliniated in the source imagery and so the ratio between low, medium and high density is probably not very accurate. 
