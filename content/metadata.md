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
|ISO 19139|The ISO suite of Metadata Standards define how to describe geospatial information and services, including spatial-temporal extents, data sources, and feature catalogs. ISO 19139 metadata are created for all data layers. ISO 19110 metadata describing feature catalogs are created for shapefiles.|GeoServer, geoMetadata |
|MODS||SearchWorks, PURL, descMetadata|
|GeoBlacklight Metadata Schema|A discovery schema for federated searching of geospatial data.|GeoBlacklight (EarthWorks)|

### Creating Metadata

Metadata is most often created for spatial data using a combination of spreadsheets, Python scripts, and ArcGIS. Using scripts and spreadsheets to manage both data and metadata is vastly more efficient, especially when working with multiple layers. Using ArcCatalog is sometimes necessary in cases where complex editing or data wrangling is required. Programs such as QGIS, and GDAL/OGR are also extremely useful for wrangling data. 

[Creating metadata with a Spreadsheet](https://kimdurante.github.io/geospatial-data-management/content/metadata/metadata)

Creating metadata with ArcGIS

Data Wrangling with GDAL\OGR











