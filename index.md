---
layout: default
title: Overview
nav_order: 0
---
## Geospatial Data Management at SUL ##

These guidelines describe geospatial data curation workflows for the Stanford Digital Repository (SDR), the Stanford Spatial Data Infrastructure (SSDI), [EarthWorks](https://earthworks.stanford.edu) and [SearchWorks](https://searchworks.stanford.edu).

## Geospatial Data ## 

Geospatial data contain relative geographic information about a place and its features. 

### Types ###

Geospatial data are of two types - raster and vector. Raster data are composed of grid cells (rows and columns). Vector data contain points, lines, and polygons. 

### Formats ###

Geospatial data file formats are containers used for encoding and exchanging geographic information. File formats store and organize references about entities and events (locations, dates, etc.). Formats also determine how the data can be used. The [Geospatial Data workflows](https://github.com/sul-dlss/gis-robot-suite) at SUL currently work with the following formats:

 * Shapefile - a widely-used format for vector data which can be read by almost all GIS systems. Shapefiles are comprised of at least 3 files with the same name and the following extensions: *.shp*, *.dbf*, *.shx*. Other files, such as *.prj*,*.cpg*, or *.shp.xml* may be present. All files must be saved in the same workspace (folder).
   
 * GeoTiFF - a raster format used for storing georeferencing/geocoding information in a TIFF file by tying a raster image to a space or map projection. GeoTIFFs must contain at least one file with the extension *.tif*. GeoTIFFs may be accompanied by other files with the same name and the following extensions: *.prj*, *.aux*, *.ovr*, *.tfw*.*.tif.xml*. All files must be saved in the same workspace (folder).

 * ArcGRID - a raster format that defines geographic space as an array of equally sized square grid points arranged in rows and columns. Each grid point stores a numeric value that represents a geographic attribute for that unit of space. ArcGRID files contain many files in at least two directories: the name directory and an info directory. Metadata for ArcGRIDs are always stored in a file title *metadada.xml*
   
## Geospatial Data Acquisitions ## 

SUL acquires geospatial data though a number of channels, including:

* Licensed data contracted or purchased from vendors.

* Open data

* Research data

* Projects





