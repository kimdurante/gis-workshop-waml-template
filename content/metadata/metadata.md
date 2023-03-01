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

Copy the files (XML and CSV templates) into the collection folder. Fill out data.csv, leaving the druid column blank. 

| filename            | sourceId                           | druid                                                     | title                                                                                                                                                                                                                                                                                                             | abstract                                           | originator | publisher | pubDate                           | isoTopic                     | theme | geographic | temporal | updateFreq                                               | language    | collectionTitle | collectionId | access                               | usage | uuid    | spatial reference | type | format |
| ------------------- | ---------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------- | --------- | --------------------------------- | ---------------------------- | ----- | ---------- | -------- | -------------------------------------------------------- | ----------- | --------------- | ------------ | ------------------------------------ | ----- | ------- | ----------------- | ---- | ------ |
| alameda2014.shp     | branner:fmmp14_alameda2014.shp     | Important Farmland, Alameda County, California, 2014      | This polygon shapefile represents areas of important farmland in Alameda County, California for 2014. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.      | California Farmland Mapping and Monitoring Program | 2014       | farming   | Land use|Urbanization|Agriculture | Alameda County (Calif.)      | 2014  |            | English  | California Farmland Mapping and Monitoring Program, 2014 | gn292dc0234 | Public          |              | ffbac2ee-53a7-425d-b3ab-beed0b718de6 | 3310  | Polygon | Shapefile         |
| amador2014.shp      | branner:fmmp14_amador2014.shp      | Important Farmland, Amador County, California, 2014       | This polygon shapefile represents areas of important farmland in Amador County, California for 2014. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.       | California Farmland Mapping and Monitoring Program | 2014       | farming   | Land use|Urbanization|Agriculture | Amador County (Calif.)       | 2014  |            | English  | California Farmland Mapping and Monitoring Program, 2014 | gn292dc0234 | Public          |              | d52f6807-52f2-4fe1-9ba6-c86a8bca56f6 | 3310  | Polygon | Shapefile         |
| butte2014.shp       | branner:fmmp14_butte2014.shp       | Important Farmland, Butte County, California, 2014        | This polygon shapefile represents areas of important farmland in Butte County, California for 2014. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.        | California Farmland Mapping and Monitoring Program | 2014       | farming   | Land use|Urbanization|Agriculture | Butte County (Calif.)        | 2014  |            | English  | California Farmland Mapping and Monitoring Program, 2014 | gn292dc0234 | Public          |              | 765b51ad-a938-4ebf-b840-f0c6202fd6ac | 3310  | Polygon | Shapefile         |
| colusa2014.shp      | branner:fmmp14_colusa2014.shp      | Important Farmland, Colusa County, California, 2014       | This polygon shapefile represents areas of important farmland in Colusa County, California for 2014. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.       | California Farmland Mapping and Monitoring Program | 2014       | farming   | Land use|Urbanization|Agriculture | Colusa County (Calif.)       | 2014  |            | English  | California Farmland Mapping and Monitoring Program, 2014 | gn292dc0234 | Public          |              | 07c4576c-c80b-4705-a98f-a83b4755e0b5 | 3310  | Polygon | Shapefile         |
| contracosta2014.shp | branner:fmmp14_contracosta2014.shp | Important Farmland, Contra Costa County, California, 2014 | This polygon shapefile represents areas of important farmland in Contra Costa County, California for 2014. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public. | California Farmland Mapping and Monitoring Program | 2014       | farming   | Land use|Urbanization|Agriculture | Contra Costa County (Calif.) | 2014  |            | English  | California Farmland Mapping and Monitoring Program, 2014 | gn292dc0234 | Public          |              | c6e6fbca-7bd1-40ae-a69b-e98170a1e0dd | 3310  | Polygon | Shapefile         |      |

|Property|Description|Instructions|Example|
|:-----|:-----|:-----|:-----|
|filename|Filename of the data|**Required.**|alameda2014.shp|
|sourceID|The source ID for the object|SourceIds use the prefix: ‘branner:’ + an abbreviation of the collection + _ + filename.|branner:fmmp14_alameda2014.shp|
|druid|the druid for the object|**Required.**|cr288qn9438|
|title|Title of the resource|**Required.** If there is an existing title, use it. Otherwise, create a title using the pattern: _What, Where, When_. For georeferenced maps, use the original map title plus '(Raster Image)'.|Important Farmland, Alameda County, California, 2014|
|originator|Personal or organization who created the resource|||
|publisher|Organization that published the data|Use an authorized name term when possible, or transcribe according to the relevant content standard.|California Farmland Mapping and Monitoring Program|
|publicationDate|Publication date for the resource||2014|
|abstract|Descriptive summary of the data|**Required.** Describes the contents of the data. |This polygon shapefile represents areas of important farmland in Alameda County, California for 2014. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public. The data is a current inventory of agricultural resources. This data is for general planning purposes and has a minimum mapping unit of ten acres. |
|topic||Topical subject terms. These should be consistent and chosen from a controlled vocabulary. Separate multiple entries with "\|".|Land use\|Urbanization\|Agriculture|
|place|Geographical subject terms|**Required.** These should be consistent and chosen from a controlled vocabulary.|Alaemda County (Calif.)|
|temporalExtent|Temporal subject expressed as a date or date range for which the content of the resource is valid.|If same as the publication date, leave blank. Otherwise, enter as either YYYY, YYYY-MM, or YYYY-MM-DD.|2014|
|collectionTitle|The title for the collection||California Farmland Mapping and Monitoring Program, 2014|
|collectionDruid|The druid for the collection object||gn292dc0234|
|contactName|Name of the person or organization to contact with questions about the data||California Farmland Mapping and Monitoring Program|
|contactEmail|Email of the person or organization to contact with questions about the data||fmmp@conservation.ca.gov|
|format|File format of the data|Choose from values: Shapefile, GeoTIFF, ArcGRID|Shapefile|
|uuid|Unique identifier for the ISO 19110 feature catalog (entity and attribute definitions)|Use for shapefiles only|ffbac2ee-53a7-425d-b3ab-beed0b718de6|
|access|Restrictions on user access to the data|Choose from values: Public or Restricted|Public|
|usage|Restrictions on use and reproduction of the data||'This item is in the public domain. There are no restrictions on use.'|


