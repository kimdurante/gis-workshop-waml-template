---
layout: default
title: Layers
nav_order: 2
---

## Layer-Level Data Workflows

Ensure that all geospatial data layers have:

* a valid filename (containing only letters, numbers, or underscores)
* a valid spatial reference system (SRS). Use of the Web Mercator projection (EPSG:3857) is not recommended.
* coordinate metadata (geographic extent). 

* Run [this script](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/checkData.py) to create a csv list of filenames, SRSs, and data types for shapefiles and/or GeoTIFFs.


### Creating a File Manifest

Create a CSV file containing a **SourceID** and a **Label** for each layer in the collection. The SourceID prefix for all GIS layers is '*branner:*' plus an abbreviation for the collection name, followed by an underscore. Append the filename to the end of this prefix to create the SourceID. (ex. branner: _fmmp12_alameda2012.shp_)

The Label is the title of the data layer. If there is an existing title, use it. Otherwise, for georeferenced maps, use the original map title plus '(_Raster Image_)' (ex. _Topographical map of the Yosemite Valley and vicinity (Raster Image)_. For other data, create a title using the pattern: *What, Where, When*  (ex. _Important Farmland, Alameda County, California, 2012_)

Format the CSV as shown below, leaving the first and third columns blank:

||SOURCEID||LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp||Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp||Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp||Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp||Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp||Important Farmland, Contra Costa County, California, 2012|


_Example layers from the California Farmland Mapping and Monitoring Program, 2012 collection._


* Register the items in Argo using the APO/Collection and the Content Type **File**. Paste the DRUIDs into the CSV.

||SOURCEID|DRUID|LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp|rc560ns7872|Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp|rc560ns7872|Important Farmland, Contra Costa County, California, 2012|

* Save the file (ex. _layers.csv_). This can used to generate metadata during cataloging.
