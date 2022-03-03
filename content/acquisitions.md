---
layout: default
title: Acquisitions
nav_order: 1
---

## Acquisitions Workflow ##

SUL acquires geospatial data from a number of sources, including:

* Commercial vendors
* Public data providers
* Scholarly research
* Special projects and support initiaitves

Data often are acquired as 'collections', meaning they contain multiple layers relating to a common theme, place, or event. It is useful to identify these similarities by performing an assessment of the data and/or opening files in a GIS.

It is crucial to understand what access and use restrictions apply to the data before downloading and distributing it. This may require consultation with the data provider or publisher.

## Assessment ##

Survey the contents of the collection to check for things such as: total number of layers, data types/formats, file sizes, and supplemental files (codebooks or csv/text/PDF/html documents containing metadata and other information)

* Consider: 
  * What features do the data contain (population statistics, boundaries, geolocated imagery, etc.)? 
  * Where they are located (geographic extent)? 
  * When were they published and also in what time period are they situated (temporal extent)? 
  * Who created and/or published the data? 
  * How often are the data updated (edition/version)? 
  * What are the access and use restrictions (rights)?

## Preparing Data ##

* Load all data into a directory (folder) and connect to the folder in ArcCatalog.

* Ensure that all layers have a valid filename (containing only letters, numbers, or underscores)

* Ensure that all layers have a valid spatial reference system (SRS). Use of the Web Mercator projection (EPSG:3857) is not recommended.

* All layers must have valid coordinate metadata (geographic extent). 

### Creating a Layer List ###

* Run [this script](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/checkData.py) to create a csv list of filenames, SRSs, and data types for shapefiles and/or GeoTIFFs.


| FILENAME       | SRS   | TYPE |
| ------------- |-------------|-----------------|
|airmonitoringstations.shp|3310|Point|
|arb_california_airbasins_aligned_03.shp|3310|Polygon|
|arb_california_airdistricts_aligned_03.shp|3310| Polygon|
|arb_california_counties_aligned_03.shp|3310| Polygon|
|fed_1hr_coabdis.shp|3310| Polygon|





