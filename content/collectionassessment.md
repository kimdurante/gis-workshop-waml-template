---
layout: default
title: Creating a Collection
nav_order: 2
---

## Creating a Collection

All data layers must belong to at least one collection. The concept of a collection when applied to these kinds of data can sometimes be vague and might include: data purchased from vendors, georeferenced maps, open data downloaded from a website/portal, or scholarly research data.

### Assessing the Collection

Survey the contents of the collection to check for things such as:

* Type(s) of data
* Total number of layers
* Supplemental files (codebooks or csv/text/PDF/html documents containing metadata and other information)

Consider:

* What features do the data contain (i.e. population statistics, boundaries, geolocated imagery)
* Where they are located (geographic extent)
* When were they published and also in what time period are they situated (temporal extent)
* Who created and/or published the data
* Edition/version information
* What are the access and use restrictions (i.e. rights)


### Determining Rights - Administrative Policy Objects

All data layers and collections must be governed by an Administrative Policy Object (APO). Locate the appropriate APO from [this list of Admin Policies](https://argo.stanford.edu/catalog/facet/nonhydrus_apo_title_ssim). If an appropriate APO does not currently exist [follow these instructions](https://consul.stanford.edu/display/DLSSDOCS/Argo+-+How+to+Create+an+APO) to create a new one.

### Creating a Collection Object

Collection objects are created using either MARC or MODS metadata. 

### MARC

If a MARC record already exists for the collection, enhance the record in WorkFlows as needed and create a collection from the catKey:

Example catKey: 11715604

SearchWorks: [California Farmland Mapping and Monitoring Program, 2012](https://searchworks.stanford.edu/view/11715604)

DRUID: qf529ms0562

PURL: https://purl.stanford.edu/qf529ms0562

### MODS


If no MARC record exists, register the collection using a title and description. Update the MODS (descMetadata) after the object has accessioned.

Title: Stanislaus County, California, GIS Data and Maps

DRUID: fy405sm5009

PURL: https://purl.stanford.edu/fy405sm5009

SearchWorks: [Stanislaus County, California, GIS Data and Maps](https://searchworks.stanford.edu/view/fy405sm5009)

### Collection-Level Metadata Recommendations

In addition to common bibliographic elements (creator, publisher, subjects, issue date, etc.) the following MODS/MARC fields are recommended for GIS collections:


|Field|MODS|MARC|Example|
|:-----|:------|:------|:------|
|Genre|genre authority="rdacontent"|336 (sub2='rdacontent')|cartographic dataset|
|Genre|genre authority="local"|655 (ind1='7'), (sub2='local')|Geographic information systems data|
|Genre|genre authority="lcgft"|655 (ind1='7'), (sub2='lcgft')|Geospatial data|
|Coordinates|subject/cartographics/coordinates|255|(W 121.4851--W 120.3878/N 038.0775--N 037.1347)|

[Detailed instructions for creating a collection object](https://consul.stanford.edu/display/DLSSDOCS/Argo+-+How+to+create+and+apply+a+collection+object). 

