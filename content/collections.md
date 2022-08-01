---
layout: default
title: Collections
nav_order: 2
---

## Collections Workflow

All geospatial data layers must belong to at least one collection. Collection objects in SDR do not store data. They provide with high-level description, browsability, and rights functionality. Access protocols for geospatial data are managed by an Administrative Policy Object (APO). APOs define access to data as either 'world' (public) or 'stanford' (restricted). This definition specifies whether data are stored in the public or restricted GeoServer. APOs also contain a Use and Reproduction statement that specifies instructions for research purpose and reuse. 

### Creating a Collection

To create a collection object in SDR, locate the APO and create the collection using either "Title/Abstract" (MODS) or "Symphony" (MARC). If the collection has a record in Symphony, enhance the MARC record as recommended below and register the collection using the catKey. 

If no MARC record exists, register the collection using a Title and Abstract. Update the MODS record later with the values shown below.

|Field|MODS|MARC|Value|
|:-----|:------|:------|:------|
|Genre|genre authority="rdacontent"|336 (sub2='rdacontent')|cartographic dataset|
|Genre|genre authority="local"|655 (ind1='7'), (sub2='local')|Geographic information systems data|
|Genre|genre authority="lcgft"|655 (ind1='7'), (sub2='lcgft')|Geospatial data|
|Coordinates|subject/cartographics/coordinates|255|(W 121.4851--W 120.3878/N 038.0775--N 037.1347)|

Example Collection PURL (from MARC): [https://purl.stanford.edu/qf529ms0562](https://purl.stanford.edu/qf529ms0562)

Example Collection PURL (from MODS): [https://purl.stanford.edu/fy405sm5009](https://purl.stanford.edu/fy405sm5009)
