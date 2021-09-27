---
layout: default
title: Creating a Collection
nav_order: 1
---

## Creating a Collection

* All data layers must belong to at least one collection. A 'collection' of geospatial data might include: data purchased from vendors, a set of georeferenced maps, open data downloaded from a website/portal, or scholarly research data. Collection objects in SDR do not store any data. They contain high-level metadata (descriptive, rights, technical) which describe the contents at a generic level.

## Assessment

* Survey the contents of the data collection to check for things such as: total number of layers, type(s) of data, file sizes, and supplemental files (codebooks or csv/text/PDF/html documents containing metadata and other information)

* Consider: 
  * What features do the data contain (population statistics, boundaries, geolocated imagery, etc.)? 
  * Where they are located (geographic extent)? 
  * When were they published and also in what time period are they situated (temporal extent)? 
  * Who created and/or published the data? 
  * How often are the data updated (edition/version)? 
  * What are the access and use restrictions (rights)?

### Determining Rights - Administrative Policy Objects

* All collections and data layers must be governed by an Administrative Policy Object (APO). Locate the appropriate APO from [this list of Admin Policies](https://argo.stanford.edu/catalog/facet/nonhydrus_apo_title_ssim). If an appropriate APO does not currently exist [follow these instructions](https://consul.stanford.edu/display/DLSSDOCS/Argo+-+How+to+Create+an+APO) to create a new one.


### Creating a Collection Object

* Collection objects are described using either MARC or MODS metadata. If a MARC record already exists in WorkFlows, enhance the record as recommended and create a collection from the catKey. MARC metadata are transformed to MODS during collection object creation.

* If no MARC record exists, create a MODS record for the collection using a title and description. Update the MODS after the object has accessioned.

* A Digital Repository Unique Identifier (DRUID) will be created for the collection.

### Collection-Level Metadata Recommendations

* In addition to common bibliographic elements (creator, publisher, subjects, publication date), the following MODS/MARC fields should be included:

|Field|MODS|MARC|Example|
|:-----|:------|:------|:------|
|Genre|genre authority="rdacontent"|336 (sub2='rdacontent')|cartographic dataset|
|Genre|genre authority="local"|655 (ind1='7'), (sub2='local')|Geographic information systems data|
|Genre|genre authority="lcgft"|655 (ind1='7'), (sub2='lcgft')|Geospatial data|
|Coordinates|subject/cartographics/coordinates|255|(W 121.4851--W 120.3878/N 038.0775--N 037.1347)|

* Example Collection PURL (from MARC): [https://purl.stanford.edu/qf529ms0562](https://purl.stanford.edu/qf529ms0562)

* Example Collection PURL (from MODS): [https://purl.stanford.edu/fy405sm5009](https://purl.stanford.edu/fy405sm5009)

