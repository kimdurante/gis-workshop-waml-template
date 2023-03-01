---
layout: default
title: Metadata
nav_order: 3
parent: Metadata
---

## Creating Metadata

Creating metadata using a csv template and scripts is usually a faster and more efficient cataloging method. 
It is also possible to create metadata directly in ArcCatalog by following the instructions here.

### Creating a Metadata Using a Spreadsheet

Copy the XML and CSV templates into the collection folder. Fill out the csv template

|Property|Description|Instructions|Example|
|:-----|:-----|:-----|:-----|
|filename|Filename of the data|**Required.**|alameda2014.shp|
|druid|the druid for the object|**Required.**|cr288qn9438|
|title|Title of the resource|**Required.** If there is an existing title, use it. Otherwise, create a title using the pattern: _What, Where, When_. For georeferenced maps, use the original map title plus '(Raster Image)'.|Important Farmland, Alameda County, California, 2014|
|originator|Personal or organization who created the resource|||
|publisher|Organization that published the data|Use an authorized name term when possible, or transcribe according to the relevant content standard.|California Farmland Mapping and Monitoring Program|
|publicationDate|Publication date for the resource||2014|
|abstract|Descriptive summary of the data|**Required**||
|theme||These should be consistent and chosen from a controlled vocabulary. In ArcCatalog, enter one keyword per line.|Census, Housing|
|place|Keywords containing place names|**Required.** These should be consistent and chosen from a controlled vocabulary. In ArcCatalog, enter one keyword per line.|Alaemda County (Calif.)|
|temporalExtent|Date or date range for which the content of the resource is valid. Sometimes this is referred to as ground condition or date of situation.||2014|
|collectionTitle|The title for the collection||California Farmland Mapping and Monitoring Program, 2014|
|collectionDruid|The druid for the collection object||gn292dc0234|
|relatedItemTitle||||
|relatedItemURL||||
|contactName||||
|contactEmail||||
|uuid||||
|format|File format of the data|Choose from values: Shapefile, GeoTIFF, ArcGRID|Shapefile|




