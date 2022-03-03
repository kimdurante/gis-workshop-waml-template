---
layout: default
title: Collections
nav_order: 1
---

## Collections Workflow ##

* All data layers must belong to at least one collection. Collection objects in SDR do not store geospatial data. They allow for such things as browsing within collections, and rights/access management.

### Determining Rights - Administrative Policy Objects ###

* Access to collections and data layers is governed by an Administrative Policy Object (APO). If an appropriate APO does not currently exist [follow these instructions](https://consul.stanford.edu/display/DLSSDOCS/Argo+-+How+to+Create+an+APO) to create a new one.

### Creating a Collection ###

* Depending on how the data is acquired, Collection objects are described using either MARC or MODS metadata. If a MARC record already exists in WorkFlows, enhance the record as recommended and create a collection from the catKey. MARC metadata are transformed to MODS during collection object creation.

* If no MARC record exists, create a MODS record for the collection using a title and description. Update the MODS after the object has accessioned.

* A Digital Repository Unique Identifier (DRUID) will be created for the collection.

### Collection-Level Metadata Recommendations ###

* In addition to common bibliographic elements (creator, publisher, subjects, publication date), the following MODS/MARC fields should be included:

|Field|MODS|MARC|Example|
|:-----|:------|:------|:------|
|Genre|genre authority="rdacontent"|336 (sub2='rdacontent')|cartographic dataset|
|Genre|genre authority="local"|655 (ind1='7'), (sub2='local')|Geographic information systems data|
|Genre|genre authority="lcgft"|655 (ind1='7'), (sub2='lcgft')|Geospatial data|
|Coordinates|subject/cartographics/coordinates|255|(W 121.4851--W 120.3878/N 038.0775--N 037.1347)|

* Example Collection PURL (from MARC): [https://purl.stanford.edu/qf529ms0562](https://purl.stanford.edu/qf529ms0562)

* Example Collection PURL (from MODS): [https://purl.stanford.edu/fy405sm5009](https://purl.stanford.edu/fy405sm5009)
