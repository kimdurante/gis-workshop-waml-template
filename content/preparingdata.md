---
layout: default
title: Preparing Data
nav_order: 3
has_children: true
---

## Preparing Data

* All data layers should be loaded into a collection directory (folder) that can be connected to ArcGIS.

* Layers must adhere to certain requirements to function properly within SDR, SSDI, and EarthWorks.

### Checking Data Properties

* Ensure that each layer has a valid filename, spatial reference, and geographic extent before accessioning begins. Refer to the instructions for Data Wrangling if you encounter problems with content.

* [Run this script to create a csv list of filenames, SRSs, and data types for shapefiles and/or GeoTIFFs.](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/checkData.py)

| FILENAME       | SRS   | TYPE |
| ------------- |-------------|-----------------|
|airmonitoringstations.shp|3310|Point|
|arb_california_airbasins_aligned_03.shp|3310|Polygon|
|arb_california_airdistricts_aligned_03.shp|3310| Polygon|
|arb_california_counties_aligned_03.shp|3310| Polygon|
|fed_1hr_coabdis.shp|3310| Polygon|


### Registering Data in Argo

* Create a spreadsheet containing a **SourceID** and a **Label** for each layer in the collection. The Source ID prefix for all GIS layers is '*branner:*' plus an abbreviation for the collection name, followed by an underscore. Append the filename of the layer to the end of this prefix to create the Source ID. (ex. branner: _fmmp12_alameda2012.shp_)

* The Label is the title of the data layer. If the data already have an existing title, use it. For georeferenced maps, use the original map title plus '(Raster Image)'. Otherwise, create a title using the pattern: *What, Where, When*. (ex. Examples: _Topographical map of the Yosemite Valley and vicinity (Raster Image)_ or _Roads, Congo, 2009_)

* Format the spreadsheet as shown below, leaving the first and third columns blank. The following layers are part of the California Farmland Mapping and Monitoring Program, 2012 collection.

||SOURCEID||LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp||Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp||Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp||Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp||Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp||Important Farmland, Contra Costa County, California, 2012|


* Register the items in Argo under the appropriate APO and Collection using the Content Type _File_. Paste the DRUIDs into the spreadsheet.

||SOURCEID|DRUID|LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp|rc560ns7872|Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp|rc560ns7872|Important Farmland, Contra Costa County, California, 2012|
