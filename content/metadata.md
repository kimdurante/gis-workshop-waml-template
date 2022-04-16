---
layout: default
title: Metadata
nav_order: 3
has_children: true
---
## Metadata Workflows

Metadata workflows for geospatial data manage the creation, transformation, and interoperability of metadata. 

### Metadata Schemas

The GIS infrastructure stores and publishes metadata in a variety of schemas so that data can be made availble within different environments. 

![Workflow](https://github.com/kimdurante/geospatial-data-management/blob/main/images/MDWorkflow.jpg?raw=true)

**ArcGIS XML**. ArcGIS provides a catalog interface for geospatial data as well as a number of processing and analysis tools which are useful in data wrangling and automation. Metadata created in ArcGISPro are stored in the ArcGIS XML format.

**ISO19139/ISO19110**. Geospatial Metadata Standard. ISO19139 metadata are created for all layers. ISO19119 metadata describing feature catalogs are created for shapefiles using an XSLT.

**MODS**. MODS metadata are derived from the ISO19139 metadata. Used in PURL, SearchWorks.

**GeoBlacklight Metadata Schema**. GeoBlacklight metadata are derived from MODS metadata. Used in EarthWorks.


### Metadata Creation

Although ArcGISPro is the primary cataloging interface for geospatial metadata, automation routines are available to alleviate the tediousness of data entry. Most often, metadata creation begins in a spreadsheet that is used to autogenerate most of the ArcGIS XML metadata. The automated metadata creation workflow for geospatial data is incredibly more efficient than creating individual metadata records from scratch. 

### Automated Workflow

Copy the following files into the collection folder containing the data.

addMetadata.py

geoTemplate.xml

metadata.csv

moveFiles.py


