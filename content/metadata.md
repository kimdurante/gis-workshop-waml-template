---
layout: default
title: Metadata
nav_order: 3
has_children: true
---
## Metadata Workflows

Metadata workflows for geospatial data manage the creation, transformation, and interoperability of metadata within a number of applications.

### Metadata Schemas

The spatial data infrastructure preserves and publishes metadata in a variety of schemas so that data can be made accessible within different environments. 

![Workflow](https://github.com/kimdurante/geospatial-data-management/blob/main/images/MDWorkflow.jpg?raw=true)

|Schema|Description|Application|
|:--|:--|:--|
|ArcGIS XML|Proprietary metadata format used in ArcGIS software.|ArcGIS|
|ISO 19139|The ISO suite of Metadata Standards define how to describe geospatial information and services, including spatial-temporal extents, data sources, and feature catalogs. ISO 19139 metadata are created for all data layers. ISO 19110 metadata describing feature catalogs are created for shapefiles.|geoMetadata |
|MODS||SearchWorks, PURL, descMetadata|
|GeoBlacklight Metadata Schema|A discovery schema for federated searching of geospatial data.|GeoBlacklight (EarthWorks)|

### Metadata Creation Tools

Although ArcGISPro is the primary cataloging interface for geospatial metadata, several automation routines may be used to alleviate the tediousness of many tasks. Most often, metadata creation begins in a spreadsheet that is used to autogenerate most ArcGIS XML metadata. The automated metadata creation workflow for geospatial data is incredibly more efficient than creating individual metadata records from scratch. 

### Automated Metadata Creation Workflow

Copy the following files into the collection folder containing the data.

geoTemplate.xml

metadata.csv

moveFiles.py


