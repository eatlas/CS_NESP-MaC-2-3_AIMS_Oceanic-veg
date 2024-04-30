# Coral Sea Oceanic Vegetation  (NESP MaC 2.3, AIMS)
This dataset is a vector shapefile mapping the deep vegetation on the bottom of the coral atoll lagoons in the Coral Sea. 

This repository contains a script to download all the public datasets used to map the vegetation. It also contains the QGIS files used to prepare the data and create the preview maps. 

This repository also contains a script (`02-plot-ocean-veg-vs-drop-cam.py`) that was used to compare the mapped vegetation to the JCU drop camera results. The drop camera data is not yet published and so is not made available as part of this repository. 

The input datasets are described in the `01-download-src-data.py` script.

See the [metadata record for this dataset](https://doi.org/10.26274/709g-aq12) for more information.

## Area calculations
The areas of the mapped vegetation were produced using the following process:
1. The CS_NESP-MaC-2-3_AIMS_Oceanic-veg.shp was opened in QGIS. This dataset already contains the area of each polygon in km2.
2. The layer was exported as a CSV in working/CS_NESP-MaC-2-3_AIMS_Oceanic-veg.csv
3. This was opened in Excel and a pivot chart used to determine the area of each density classification.
Resulting in the following totals:
High density: 7350 km2
Medium density: 1366 km2
Low density: 256 km2
Total: 8973 km2

It should be noted that the boundary between the low and medium density was not strongly deliniated in the source imagery and so the ratio between low, medium and high density is probably not very accurate. 
