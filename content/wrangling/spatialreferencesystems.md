---
layout: default
title: Spatial Reference Systems
nav_order: 1
parent: Data Wrangling and Inspection
---
# Spatial Reference Systems

All GIS layers must have an associated spatial reference system (SRS). SRS metadata are recorded using a code and a codespace (namespace). Codespaces represent registries that maintain identifiers for SRSs, the most common being the [EPSG Geodetic Parameter Dataset (EPSG)](http://www.epsg-registry.org). 

Example SRS Codespace: EPSG<br/>Example SRS Code: 2227

All layers with an SRS that is not WGS84 (EPSG:4326) are transformed during accessioning and made available for download in both the original and transformed ('generated') versions.

Use of the Web Mercator (EPSG:3857) SRS is not recommended.
