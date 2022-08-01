---
layout: default
title: Layers
nav_order: 2
---

## Layer-Level Workflows

Preparing geospatial data layers for accessioning.

### Preparing Data

Preparing geospatial data can involve inspecting or wrangling files in order to make sure they meet certain functional requirements of the infrastructure. 

All layers must have:

* a valid filename (containing only letters, numbers, or underscores)
* a geographic extent (bounding box coordinates)
* a valid spatial reference system (SRS)

Geospatial data can be accessioned using any valid SRS, however use of the Web Mercator projection is not recommended. During accessioning, data are normalized to the WGS84 coordinate system (EPSG:4326). A copy of the original dataset and a WGS84 derivative are stored in SDR and made availble for download in EarthWorks, SearchWorks, and PURL. WGS84 data are uploaded to GeoServer.

**Renaming Files**. Run [this script] to rename files containing invalid characters.

**List Data**. Run [this script](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/checkData.py) to create a csv list of filenames, SRSs, and data types for shapefiles and/or GeoTIFFs.

**Reprojecting Files**

### Registering Data

Register data layers using a csv file containing a **SourceID** and a **Label** for each layer. The SourceID contains the prefix  '*branner:*', an abbreviation of the collection name, and an underscore. The filename is appended to the prefix to create the SourceID (ex. *branner:fmmp12_alameda2012.shp*). The Label is the title of the data layer. 

Register the items in Argo using the appropriate APO and Collection. Use Content Type **File**. Format the csv as shown below.

|||SOURCEID||LABEL|
|:----|:----|:----|:----|:----|
|||branner:fmmp12_alameda2012.shp||Important Farmland, Alameda County, California, 2012|
|||branner:fmmp12_amador2012.shp||Important Farmland, Amador County, California, 2012|
|||branner:fmmp12_butte2012.shp||Important Farmland, Butte County, California, 2012|

_A DRUID is created for each data layer_


||SOURCEID|DRUID|LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|

_Example layers from the California Farmland Mapping and Monitoring Program, 2012 collection._
