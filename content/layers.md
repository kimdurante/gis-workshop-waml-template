---
layout: default
title: Layers
nav_order: 2
---

## Layer-Level Workflows

Preparing geospatial data for accessioning can involve inspecting or wrangling files in order to make sure they meet certain functional requirements on the infrastructure. 

All layers must have:

* a valid filename (containing only letters, numbers, or underscores)
* a valid spatial reference system (SRS). Use of the Web Mercator projection (EPSG:3857) is not recommended
* a geographic extent (bounding box coordinates)

**Renaming Files**. Run [this script] to rename files containing invalid characters.

**List Data**. Run [this script](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/checkData.py) to create a csv list of filenames, SRSs, and data types for shapefiles and/or GeoTIFFs.


### Registering Data Layers in SDR

Create a CSV file containing a **SourceID** and a **Label** for each layer in the collection. The SourceID contains a prefix and a filename. The prefix consists of '*branner:*' followed by an abbreviation of the collection name followed by an underscore. The filename for the layer is appended to this prefix to create the SourceID (ex. *branner:fmmp12_alameda2012.shp*). The Label is the title of the data layer. 

Format the CSV as shown below, leaving the first and third columns blank:

||SOURCEID||LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp||Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp||Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp||Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp||Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp||Important Farmland, Contra Costa County, California, 2012|


_Example layers from the California Farmland Mapping and Monitoring Program, 2012 collection._


### Registering Data in Argo

Register the items in Argo using the relevant APO and Collection. Use Content Type **File**.

||SOURCEID|DRUID|LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp|rc560ns7872|Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp|rc560ns7872|Important Farmland, Contra Costa County, California, 2012|

### Creating Metadata

Metadata are created in the ArcGIS metadata format and transformed into ISO 19139, ISO 19110, MODS, and GeoBlacklight.
Metadata are created in ArcCatalog using the ISO 19139 Metadata Specification. ISO 19110 Metadata describing feature catalogs (data attributes) are generated for vector data. Metadata for shapefiles and geoTIFFs are recognizable by their file extensions *.shp.xml* and *tif.xml*. Metadata for GRID files will always be named *metadata.xml*.

