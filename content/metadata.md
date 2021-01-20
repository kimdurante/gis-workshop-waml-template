---
layout: default
title: Metadata
nav_order: 5
has_children: true
---

### Creating ISO 19139 Metadata in ArcCatalog

Metadata for shapefiles, geoTIFFs, and Grid layers are created in ArcCatalog and stored with the data in a manner that is appropriate for the data type. For shapefiles and geoTIFFs, metadata are recognizable by their file extensions _.shp.xml_ and _tif.xml_. ArcGRID metadata will always be named _metadata.xml_. ArcCatalog metadata are output in the ArcGIS metadata format and transformed into ISO 19139, ISO 19110, MODS, and GeoBlacklight using the [gis-robot-suite](https://github.com/sul-dlss/gis-robot-suite/tree/master/robots).

### Creating MODS Metadata

Geodatabases, GeoPDFs, and other geospatial data use MODS metadata. These metadata are created manually using either spreadsheets or XML files.
