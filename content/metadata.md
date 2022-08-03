---
layout: default
title: Metadata
nav_order: 3
has_children: true
---
## Metadata Workflows

Metadata workflows for geospatial data manage the creation, transformation, and interoperability of metadata within a number of applications.

### Metadata Schemas

The spatial data infrastructure preserves and publishes metadata in a variety of schemas. Metadata for spatial datasets is created in ArcGIS XML, then transformed into ISO 19139/19110, MODS, and GeoBlacklight metadata, in order to make data discoverable and accessible within different environments.

![Workflow](https://github.com/kimdurante/geospatial-data-management/blob/main/images/MDWorkflow.jpg?raw=true)

|Schema|Description|Application|
|:--|:--|:--|
|ArcGIS XML|Proprietary metadata format used in ArcGIS software.|ArcGIS|
|ISO 19139|The ISO suite of Metadata Standards define how to describe geospatial information and services, including spatial-temporal extents, data sources, and feature catalogs. ISO 19139 metadata are created for all data layers. ISO 19110 metadata describing feature catalogs are created for shapefiles.|geoMetadata |
|MODS||SearchWorks, PURL, descMetadata|
|GeoBlacklight Metadata Schema|A discovery schema for federated searching of geospatial data.|GeoBlacklight (EarthWorks)|

### Metadata Creation

Metadata is most often created for spatial data using a combination of spreadsheets, Python scripts, and ArcGIS. Using scripts and spreadsheets to manage both data and metadata is vastly more efficient, especially when working with multiple layers. Programs such as ArcGIS, QGIS, and GDAL/OGR are also extremely useful for wrangling data.

### Using the Metadata Spreadsheet

Make a copy of the GIS Metadata Spreadsheet in the collection folder. Add the filenames, druids, and titles, from the list of registered layers.







