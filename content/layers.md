---
layout: default
title: Layers
nav_order: 2
---

## Layer-Level Workflows


Preparing geospatial data can involve inspecting or wrangling files in order to make sure they meet certain functional requirements of the infrastructure. 

### Preparing Data

Prior to cataloging/accessioning data, ensure that all layers have:

* a valid filename (containing only letters, numbers, or underscores)
* a valid geographic extent (bounding box coordinates)
* a valid spatial reference system (SRS)

The infrastructure accepts data in any valid SRS. During the gisAssembly workflow, data are normalized to the WGS84 coordinate system. A copy of both the original dataset and the WGS84 derivative are stored in SDR and made availble for download in EarthWorks, SearchWorks, and PURL. The WGS84 data are uploaded to GeoServer.

**Spatial Reference Systems**

### Registering Data

Register data layers using a csv file containing a **SourceID** and a **Label** for each layer. The SourceID contains the prefix  '*branner:*', an abbreviation of the collection name, and an underscore. The filename is appended to the prefix to create the SourceID (ex. *branner:fmmp12_alameda2012.shp*). The Label is the title of the data layer. 

Register the items in Argo using the appropriate APO and Collection. Use Content Type **File**. Format the csv as shown below.

|||SOURCEID||LABEL|
|:----|:----|:----|:----|:----|
|||branner:fmmp12_alameda2012.shp||Important Farmland, Alameda County, California, 2012|
|||branner:fmmp12_amador2012.shp||Important Farmland, Amador County, California, 2012|
|||branner:fmmp12_butte2012.shp||Important Farmland, Butte County, California, 2012|

A DRUID is created for each data layer


||SOURCEID|DRUID|LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|

_Example layers from the California Farmland Mapping and Monitoring Program, 2012 collection._
