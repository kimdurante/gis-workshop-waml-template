---
layout: default
title: Metadata
nav_order: 3
parent: Metadata
---

## Creating Metadata

Creating metadata using a spreadsheet and scripts is usually faster and more efficient than creating metadata directly in ArcCatalog.

### Create a Spreadsheet

Copy the metadata management files (LINK) into the collection folder. Fill out the following fields for each layer in data.csv, leave all other columns blank.


|Field|Example|
|:-----|:-----|
|filename|alameda2014.shp|
|sourceID|branner:fmmp14_alameda2014.shp|
|title|Important Farmland, Alameda County, California, 2014|
|publisher|California Farmland Mapping and Monitoring Program|
|publicationDate|2014|
|abstract|This polygon shapefile represents areas of important farmland in Alameda County, California for 2014. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public. The data is a current inventory of agricultural resources. This data is for general planning purposes and has a minimum mapping unit of ten acres. |
|topic||Land use\|Urbanization\|Agriculture|
|place|Alaemda County (Calif.)|
|collectionTitle|California Farmland Mapping and Monitoring Program, 2014|
|collectionDruid|gn292dc0234|
|contactName|California Farmland Mapping and Monitoring Program|
|contactEmail|fmmp@conservation.ca.gov|
|format|Shapefile|
|uuid|ffbac2ee-53a7-425d-b3ab-beed0b718de6|
|access|Public|
|usage|This item is in the public domain. There are no restrictions on use.|

### Register Data

Using the sourceId and Title for each layer, register the items in Argo under their APO/Collection. Use content type: File. This will create a DRUID for each layer. Add the DRUIDs to data.csv.

### Generate XML Metadata

Open a terminal and run ```createMetadata.py```.

The layers must then be updated (synchronized) in ArcCatalog. In ArcCatalog, open a python window and run the following:

```
import arcpy
from arcpy import env
from arcpy import metadata as md
import os

#Path to the data directory
env.workspace = "W:\Africa_Marine_Atlas"

for dirs, subdirs, files in os.walk(env.workspace):
    for f in files:
        if f.endswith(".shp") or f.endswith(".tif"):
            filePath = os.path.join(dirs, f)
            src_item_md = md.Metadata(filePath)
            print (src_item_md)
            src_item_md.synchronize("ALWAYS")
```

### Creating Thumbnail Images






