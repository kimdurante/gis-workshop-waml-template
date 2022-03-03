---
layout: default
title: Collections
nav_order: 2
---

## Collections Workflow


All data layers must be governed by an Administrative Policy Object (APO) and they must all belong to at least one collection. Collections in SDR do not store geospatial data. They provide rights functionality, high-level description, and browsability. 

### Administrative Policy Objects

Access to collections and data is governed by an Administrative Policy Object. APOs provide If an appropriate APO does not currently exist [follow these instructions](https://consul.stanford.edu/display/DLSSDOCS/Argo+-+How+to+Create+an+APO) to create a new one.

### Collection-Level Metadata

Collection-level records are created using either MARC or MODS metadata. This often depends on how or when the collection was acquired. Data purchased through traditional library acquisitions channels tend to originate in Symphony (WorkFlows), and thus use MARC as their source metadata. MODS metadata are increasingly used to describe digital collections. Either method is acceptable. If a MARC record already exists in WorkFlows, enhance the record as recommended below. If no MARC record exists, create a MODS record using a title and description and update the record after the collection has been created.

In addition to common bibliographic elements (creator, publisher, subjects, publication date), the following fields should be included for geospatial data:

|Field|MODS|MARC|Value|
|:-----|:------|:------|:------|
|Genre|genre authority="rdacontent"|336 (sub2='rdacontent')|cartographic dataset|
|Genre|genre authority="local"|655 (ind1='7'), (sub2='local')|Geographic information systems data|
|Genre|genre authority="lcgft"|655 (ind1='7'), (sub2='lcgft')|Geospatial data|
|Coordinates|subject/cartographics/coordinates|255|(W 121.4851--W 120.3878/N 038.0775--N 037.1347)|

Example Collection PURL (from MARC): [https://purl.stanford.edu/qf529ms0562](https://purl.stanford.edu/qf529ms0562)

Example Collection PURL (from MODS): [https://purl.stanford.edu/fy405sm5009](https://purl.stanford.edu/fy405sm5009)
