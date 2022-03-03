---
layout: default
title: Accessioning Data
nav_order: 4
---
## Accessioning Workflow

Staging files for accessioning.

### Staging Data

Create a new directory folder) for the collection.
Example: California_Farmland_Mapping_2012

In the directory, make a folder for each layer using the DRUID as the name. In each DRUID folder, make a folder called ```temp```.

Example:
```
California_Farmland_Mapping_2012
 
-bd235mg0255  
--temp

-bw755mz6720  
--temp
```


[Run this script](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/scripts/makeFolders.py) in the collection directory to create ```DRUID/temp``` folders for each layer.


Move all files associated with the layer into the appropriate ```DRUID/temp``` folder. [This script](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/scripts/moveFiles.py) will find all files and move them into the staging environment.

### SDR Accessioning and EarthWorks

Run the following workflows on each layer

* gisAssemblyWF
* gisDeliveryWF
* accessionWF

See the [gis-robot-suite](https://github.com/sul-dlss/gis-robot-suite/tree/master/robots) for more information.

See the [consul instructions for Accessioning Data into SDR and EarthWorks](https://consul.stanford.edu/display/SULAIRGIS/HOWTO+-+Accession+layers)
