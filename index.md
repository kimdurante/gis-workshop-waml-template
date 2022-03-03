---
layout: default
title: Overview
nav_order: 0
---
## Geospatial Data Management at SUL ##

These guidelines describe geospatial data curation workflows for the Stanford Digital Repository (SDR), the Stanford Spatial Data Infrastructure (SSDI), [EarthWorks](https://earthworks.stanford.edu) and [SearchWorks](https://searchworks.stanford.edu).

SUL's [GIS Data Robots](https://github.com/sul-dlss/gis-robot-suite) support the preservation, access, and discovery of geospatial data at the layer-level. Every data layer (e.g. shapefile) is identiifed by its own DRUID and can be accessed through a number of applications including: PURL, EarthWorks, SearchWorks, GeoServer, and WMS/WFS.

## Geospatial Data ## 

Geospatial data are of two types: raster and vector. Raster data are composed of grid cells (rows and columns). Vector data contain points, lines, and polygons. 

Formats - GIS file formats are containers used for encoding and exchanging geographic information. File formats store and organize references about entities and events (locations, dates, etc.). Additionally, file formats play a crucial role in determining how the data can be used. 

The GIS robots currently accept the following file formats:

 * Shapefile - a widely-used format for vector data which can be read by almost all GIS systems. Shapefiles are comprised of at least 3 files with the same name and the following extensions: *.shp*, *.dbf*, *.shx*. Other files, such as *.prj*,*.cpg*, or *.shp.xml* may be present.
   
 * GeoTiFF - a raster format used for storing georeferencing/geocoding information in a TIFF file by tying a raster image to a space or map projection. GeoTIFFs must contain at least one file with the extension *.tif*. GeoTIFFs may be accompanied by other files with the same name and the following extensions: *.prj*, *.aux*, *.ovr*, *.tfw*.*.tif.xml*.

 * ArcGRID - a raster format that defines geographic space as an array of equally sized square grid points arranged in rows and columns. Each grid point stores a numeric value that represents a geographic attribute for that unit of space. ArcGRID files contain many files in at least two directories: the name directory and an info directory. Metadata for ArcGRIDs are always stored in a file named *metadata.xml*





