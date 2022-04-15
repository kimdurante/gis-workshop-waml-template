---
layout: default
title: Metadata
nav_order: 3
has_children: true
---
## Metadata Workflows

Metadata workflows for geospatial data are designed to manage creation, transformation, and interoperability of metadata. The spatial data infrastructure uses automated routines to generate metadata in different schemas and formats, so that they can be used within different applications.

|Schema|Description|
|:-----|:--|
|ArcGIS XML|Metadata format used in ArcGIS/ArcCatalog. ArcGIS metadata are created in ArcCataloged and transformed to ISO metadata using a system-supplied XSLT.|
|ISO19139/ISO19110|Geospatial Metadata Standard. ISO19139 metadata are created for all layers. ISO19119 metadata describing feature catalogs are created for shapefiles using an XSLT.|
|MODS|MODS metadata are derived from the ISO19139 metadata. Used in PURL, SearchWorks|
|GeoBlacklight Metadata Schema|GeoBlacklight metadata are derived from MODS metadata. Used in EarthWorks|

### ISO 19139/19110 Metadata

* Metadata for vector and raster data are created in ArcCatalog using the ISO 19139 Metadata Specification. ISO 19110 Metadata describing feature catalogs (data attributes) are generated for vector data.

* Metadata for these layers are stored with the data in a manner that is appropriate for the data type. Metadata for shapefiles and geoTIFFs are recognizable by their file extensions _.shp.xml_ and _tif.xml_. Metadata for GRID files will always be named _metadata.xml_. 
 
* Metadata are output in the ArcGIS metadata format and transformed into ISO 19139, ISO 19110, MODS, and GeoBlacklight.

* Data and metadata are accessioned into SDR using [GIS Robot Workflows](https://github.com/sul-dlss/gis-robot-suite).

### MODS Metadata

* MODS metadata are created for all other file formats (geodatabases, geoPDFs, etc.) using either XML documents or a spreadsheet.

* Data are accessioned into SDR using the PreAssembly Application. 

### Web Applications

* JSON Metadata for web maps are stored here. These items are not accessioned into SDR.
