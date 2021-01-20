layout: default
title: Creating Metadata with ArcCatalog
nav_order: 1
parent: Metadata
---

[Setting Up ArcCatalog](#Setting-Up-ArcCatalog)  
[Creating a Collection Template](#Creating-a-Collection-Template)  
[Importing a Template](#Importing-a-Template)  
[Updating Metadata for Individual Layers](#Updating-Metadata-for-Individual-Layers)  
[Autogenerating Metadata](#Autogenerating-Metadata)  
[Autogenerating Thumbnail Images](#Autogenerating-Thumbnail-Images)  

### Setting Up ArcCatalog

Open ArcCatalog. Set the Metadata Style to ISO 19139. From the Menu bar:

```Customize > ArcCatalog Options > Metadata > ISO 19139 Metadata Implementation Specification```

Connect to the directory (folder) containing the data collection.

### Creating a Collection Template

[Make a copy of this metadata template into the data directory.](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/templates/template.xml) Update elements in the template with metadata that are common among all layers. 

This is a very straightforward example. The theme keywords, temporal extent, and attribute definitions are identical for each shapefile. The text for the abstract varies only in the name of the county.

Example Template: California Farmland Mapping and Monitoring Program, 2012

Edit the following fields of the template:


|FIELD|VALUE|
|:-----|:-----|
|Abstract|This polygon shapefile represents areas of important farmland in COUNTY, California for 2012. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.|
|Purpose|The Farmland Mapping and Monitoring Program (FMMP) provides data to decision makers for use in planning for the present and future use of California's agricultural land resources. The data is a current inventory of agricultural resources. This data is for general planning purposes and has a minimum mapping unit of ten acres.|
|ISO topic category|Farming|
|Theme keywords|Land use<br/>Urbanization<br/>Agriculture|
|Collective title|California Farmland Mapping and Monitoring Program, 2012|
|Publication Date|2012-01-01|
|Publisher|California. Farmland Mapping and Monitoring Program|
|Originator|California. Farmland Mapping and Monitoring Program|
|Parent metadata identifier|https://purl.stanford.edu/rn450jx3747.mods|
|Temporal extent description|ground condition|
|Temporal extent|2012-01-01|
|Point of contact|California. Farmland Mapping and Monitoring Program|
|Maintenance and Update Frequency|Biannually|
|Use constraints|This item is in the public domain. There are no restrictions on use.|
|Aggregate dataset title|California Farmland Mapping and Monitoring Program, 2012|
|Aggregate dataset identifier|https://purl.stanford.edu/rn450jx3747|
|Attribute Labels|county_nam<br/>upd_year<br/>polygon_ty</br>|
|Attribute Definitions|County name<br/>Update year<br/>Farmland categories: Prime Farmland (P), Farmland of Statewide Importance (S), Unique Farmland (U), Farmland of Local Importance (L), Grazing Land (G), Urban and Built-up Land (D), Other Land (X)|

Save the template.

### Importing a Template

Import the template into each layer using either ArcCatalog (ArcPy/Metadata Importer Tool) or an external script. Note that importing a template will overwrite any existing metadata.
#### ArcPy

From the Menu bar: ```GeoProcessing > Python```

Enter the code below. Replace ```C:/PATH/TO/DIRECTORY``` with the correct path:

```
>>> import os, arcpy
>>> from arcpy import env
>>> env.workspace: r‘C:/PATH/TO/DIRECTORY’
>>> layers = arcpy.ListFeatureClasses('*')
>>> for layer in layers:
    arcpy.ImportMetadata_conversion(r"C:/PATH/TO/TEMPLATE/template.xml",FROM_ARCGIS",layer)
```

#### ArcGIS Metadata Importer

The Metadata Importer Tool can import a template into one or more layers using singular or batch import methods. 
When importing into a single layer select the import type: ```FROM_ARCGIS```.



#### Python

This is the quickest method. [Copy this Python script into the data directory and run it.](https://github.com/kimdurante/metadataWorkflow/blob/master/scripts/importTemplate.py)

```>>> python importTemplate.py```

### Updating Metadata for Individual Layers

Select a layer from the directory. Update the metadata elements with values unique to that layer.  

Example: alameda2012.shp

|FIELD|VALUE|
|:-----|:-----|
|Title|Important Farmland, Alameda County, California, 2012|
|Abstract|This polygon shapefile represents areas of important farmland in Alameda County, California for 2012. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.|
|Credit|California Farmland Mapping and Monitoring Program. (2012). Important Farmland, Alameda County, California, 2012. California Farmland Mapping and Monitoring Program. Available at: http://purl.stanford.edu/rp378rd3804.|
|Place keywords|Alameda County (Calif.)|
|Identifier|https://purl.stanford.edu/rp378rd3804|
|Metadata File Identifier|edu.stanford.purl:rp378rd3804|
|Dataset URI|https://purl.stanford.edu/rp378rd3804|
|Distribution Online Linkage|https://purl.stanford.edu/rp378rd3804|
|Distribution Online Name|alameda2012.shp|
|Feature Catalog Identifier|564c855e-e45a-47dc-b0c4-001839b00864|

Save the file.

#### Create a Thumbnail Image

On the Preview tab use the Thumbnail Generator tool to create a thumbnail preview for the layer.

![alameda.jpg](https://github.com/kimdurante/metadataWorkflow/blob/master/images/alameda.jpg)

Open the next layer in the directory and add the unique values

Example: amador2012.shp

|FIELD|VALUE|
|:-----|:-----|
|Title|Important Farmland, Amador County, California, 2012|
|Abstract|This polygon shapefile represents areas of important farmland in Amador County, California for 2012. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.|
|Credit|California Farmland Mapping and Monitoring Program. (2012). Important Farmland, Amador County, California, 2012. California Farmland Mapping and Monitoring Program. Available at: http://purl.stanford.edu/mc357cj1107.|

<details><summary>See All</summary>
<br/>
<table>
  <tr>
    <td class="tg-0lax">Place Keywords</td>
    <td class="tg-0lax">Almador County (Calif.)</td>
  </tr>
  <tr>
    <td class="tg-0lax">Identifier</td>
    <td class="tg-0lax">https://purl.stanford.edu/mc357cj1107</td>
  </tr>
  <tr>
    <td class="tg-0lax">Metadata File Identifier</td>
    <td class="tg-0lax">edu.stanford.purl:mc357cj1107</td>
  </tr>
  <tr>
    <td class="tg-0lax">Dataset URI</td>
    <td class="tg-0lax">https://purl.stanford.edu/mc357cj1107</td>
  </tr>
  <tr>
    <td class="tg-0lax">Distribution Online Linkage</td>
    <td class="tg-0lax">https://purl.stanford.edu/mc357cj1107</td>
  </tr>
  <tr>
    <td class="tg-0lax">Distribution Online Name</td>
    <td class="tg-0lax">amador2012.shp</td>
  </tr>
  <tr>
    <td class="tg-0lax">Feature Catalog Identifier</td>
    <td class="tg-0lax">e011c181-590e-4d9a-bcbd-de2df592d00c</td>
  </tr>
</table>
</details>


In these examples the first four elements (title, abstract, place keyword, and credit) contain free text referencing the specific county (Alameda, Amador, etc.). The remaining elements are strings containing identifiers or filenames. 

The credit element contains the preferred citation text used MODS (PURL) metadata. In most cases this element can be derived from existing metadata elements: originator, date, title, publisher, and PURL.


### Autogenerating Metadata

Even a relatively simple collection example like the one above requires lot of manual entry across dozens of files. Using tools to automate input, especially when metadata contain URLs or redundant information, can make processing XML faster and less susceptible to error.

Create a csv file called ```layers.csv``` containing four columns: FILENAME, DRUID, TITLE, UUID. The filename, title, and DRUID for each layer can be obtained from an Argo report. The UUID column contains the identifier for linking the ISO 19139 and ISO 19110 metadata. [Generate UUIDs here](https://www.uuidgenerator.net).

Save ```layers.csv``` to the collection directory.


|FILENAME|DRUID|TITLE|UUID|
|:-----|:-----|:-----|:-----|
|alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|564c855e-e45a-47dc-b0c4-001839b00864|
|amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|e011c181-590e-4d9a-bcbd-de2df592d00c|
|butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|0cb51486-aebf-4e64-8d07-2f1039bafee1|
|colusa2012.shp|rc560ns7872|Important Farmland, Colusa County, California, 2012|8837d532-7ae4-4fa6-8adf-b1ad7abd89ac|

<details><summary>See All</summary>
<br/>
<table>
  <tr>
    <td class="tg-0lax">contracosta2012.shp</td>
    <td class="tg-0lax">tw099dq1877</td>
    <td class="tg-0lax">Important Farmland, Contra Costa County, California, 2012</td>
    <td class="tg-0lax">31ebffd3-caac-4e59-aa75-67cfdbaaea91</td>
  </tr>
  <tr>
    <td class="tg-0lax">eldorado2012.shp</td>
    <td class="tg-0lax">bd235mg0255</td>
    <td class="tg-0lax">Important Farmland, El Dorado County, California, 2012</td>
    <td class="tg-0lax">def7c22e-3370-405c-80a4-21e0755be69f</td>
  </tr>
  <tr>
    <td class="tg-0lax">fresno2012.shp</td>
    <td class="tg-0lax">df831fg6767</td>
    <td class="tg-0lax">Important Farmland, Fresno County, California, 2012</td>
    <td class="tg-0lax">ed7ba613-3d50-40e3-bebc-a0365869c979</td>
  </tr>
  <tr>
    <td class="tg-0lax">glenn2012.shp</td>
    <td class="tg-0lax">nd302nb7780</td>
    <td class="tg-0lax">Important Farmland, Glenn County, California, 2012</td>
    <td class="tg-0lax">3736bcc1-903e-4675-b794-7c74fce14bf0</td>
  </tr>
  <tr>
    <td class="tg-0lax">imperial2012.shp</td>
    <td class="tg-0lax">bw755mz6720</td>
    <td class="tg-0lax">Important Farmland, Imperial County, California, 2012</td>
    <td class="tg-0lax">082567a3-c082-4000-9ac3-eff3160c46b2</td>
  </tr>
  <tr>
    <td class="tg-0lax">kern2012.shp</td>
    <td class="tg-0lax">tg135ph2124</td>
    <td class="tg-0lax">Important Farmland, Kern County, California, 2012</td>
    <td class="tg-0lax">aad08d15-a7b1-4348-a730-d71f309ef3f4</td>
  </tr>
  <tr>
    <td class="tg-0lax">kings2012.shp</td>
    <td class="tg-0lax">vx330xj9508</td>
    <td class="tg-0lax">Important Farmland, Kings County, California, 2012</td>
    <td class="tg-0lax">e7dfc9e8-09dd-4168-bb59-9abac1486d9e</td>
  </tr>
  <tr>
    <td class="tg-0lax">lake2012.shp</td>
    <td class="tg-0lax">vd631sr7734</td>
    <td class="tg-0lax">Important Farmland, Lake County, California, 2012</td>
    <td class="tg-0lax">2bed04fe-b0cd-4c9b-8f57-a0d1b21f5914</td>
  </tr>
  <tr>
    <td class="tg-0lax">losangeles2012.shp</td>
    <td class="tg-0lax">hk094xr8182</td>
    <td class="tg-0lax">Important Farmland, Los Angeles County, California, 2012</td>
    <td class="tg-0lax">bc0a0699-3dfd-4187-96f0-4eb63d2abb07</td>
  </tr>
  <tr>
    <td class="tg-0lax">madera2012.shp</td>
    <td class="tg-0lax">hc191sp2641</td>
    <td class="tg-0lax">Important Farmland, Madera County, California, 2012</td>
    <td class="tg-0lax">714dd17e-2e71-4db8-b432-9473bf5fe2cc</td>
  </tr>
  <tr>
    <td class="tg-0lax">marin2012.shp</td>
    <td class="tg-0lax">sm826hp4918</td>
    <td class="tg-0lax">Important Farmland, Marin County, California, 2012</td>
    <td class="tg-0lax">188e160c-1b15-4056-9b77-78185749ea99</td>
  </tr>
  <tr>
    <td class="tg-0lax">mariposa2012.shp</td>
    <td class="tg-0lax">jw394jv6304</td>
    <td class="tg-0lax">Important Farmland, Mariposa County, California, 2012</td>
    <td class="tg-0lax">cbd95149-e0ae-4f48-a031-654877bc9dc5</td>
  </tr>
  <tr>
    <td class="tg-0lax">mendocino2012.shp</td>
    <td class="tg-0lax">cm997rw6211</td>
    <td class="tg-0lax">Important Farmland, Mendocino County, California, 2012</td>
    <td class="tg-0lax">aa99ca64-6c5b-48be-beaa-551d0e322ebc</td>
  </tr>
  <tr>
    <td class="tg-0lax">merced2012.shp</td>
    <td class="tg-0lax">zq426cm9039</td>
    <td class="tg-0lax">Important Farmland, Merced County, California, 2012</td>
    <td class="tg-0lax">9b31316a-ce04-4138-b517-7d53569e95c9</td>
  </tr>
  <tr>
    <td class="tg-0lax">modoc2012.shp</td>
    <td class="tg-0lax">pr305dz0124</td>
    <td class="tg-0lax">Important Farmland, Modoc County, California, 2012</td>
    <td class="tg-0lax">01a7197c-0e10-4779-ba4b-b2a42d76949d</td>
  </tr>
  <tr>
    <td class="tg-0lax">monterey2012.shp</td>
    <td class="tg-0lax">xz952pd7686</td>
    <td class="tg-0lax">Important Farmland, Monterey County, California, 2012</td>
    <td class="tg-0lax">4d90d227-6ba0-4cd6-b6f7-f140140448fa</td>
  </tr>
  <tr>
    <td class="tg-0lax">napa2012.shp</td>
    <td class="tg-0lax">ky438ry5906</td>
    <td class="tg-0lax">Important Farmland, Napa County, California, 2012</td>
    <td class="tg-0lax">8d1fa794-37c3-42b9-a0b6-f40a0dcb5f48</td>
  </tr>
  <tr>
    <td class="tg-0lax">nevada2012.shp</td>
    <td class="tg-0lax">ts340ts1571</td>
    <td class="tg-0lax">Important Farmland, Nevada County, California, 2012</td>
    <td class="tg-0lax">9cd09589-0a18-435d-9f6e-e22ca229746a</td>
  </tr>
  <tr>
    <td class="tg-0lax">orange2012.shp</td>
    <td class="tg-0lax">vn468vq4911</td>
    <td class="tg-0lax">Important Farmland, Orange County, California, 2012</td>
    <td class="tg-0lax">b593a2d0-a673-4dcc-a989-0e159afb54f5</td>
  </tr>
  <tr>
    <td class="tg-0lax">placer2012.shp</td>
    <td class="tg-0lax">nt745qn0438</td>
    <td class="tg-0lax">Important Farmland, Placer County, California, 2012</td>
    <td class="tg-0lax">11849ef6-2e3a-49bf-ada9-48a8cfc194d3</td>
  </tr>
  <tr>
    <td class="tg-0lax">riverside2012.shp</td>
    <td class="tg-0lax">tw906cb9868</td>
    <td class="tg-0lax">Important Farmland, Riverside County, California, 2012</td>
    <td class="tg-0lax">143c4eff-dc78-4bc5-987c-ab77d7689683</td>
  </tr>
  <tr>
    <td class="tg-0lax">sacramento2012.shp</td>
    <td class="tg-0lax">fz917ht4816</td>
    <td class="tg-0lax">Important Farmland, Sacramento County, California, 2012</td>
    <td class="tg-0lax">00b80462-2115-4652-9f38-c55692000d25</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanbenito2012.shp</td>
    <td class="tg-0lax">df983nx3922</td>
    <td class="tg-0lax">Important Farmland, San Benito County, California, 2012</td>
    <td class="tg-0lax">bc4a9057-0568-4474-a6b0-6ce2f00e4411</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanbernardino2012.shp</td>
    <td class="tg-0lax">st501nt1256</td>
    <td class="tg-0lax">Important Farmland, San Bernardino County, California, 2012</td>
    <td class="tg-0lax">32051782-3df6-45d3-ae4d-8553784c8c91</td>
  </tr>
  <tr>
    <td class="tg-0lax">sandiego2012.shp</td>
    <td class="tg-0lax">vs099sj0325</td>
    <td class="tg-0lax">Important Farmland, San Diego County, California, 2012</td>
    <td class="tg-0lax">4ec9f58c-e1e5-4a68-a539-3a78f89c2c0c</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanjoaquin2012.shp</td>
    <td class="tg-0lax">hb437dj8324</td>
    <td class="tg-0lax">Important Farmland, San Joaquin County, California, 2012</td>
    <td class="tg-0lax">3924daf1-6398-464a-aa6c-dc0364f00b86</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanluisobispo2012.shp</td>
    <td class="tg-0lax">vv216kg8929</td>
    <td class="tg-0lax">Important Farmland, San Luis Obispo County, California, 2012</td>
    <td class="tg-0lax">11948465-d0dd-4017-adc7-15c6da08f611</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanmateo2012.shp</td>
    <td class="tg-0lax">wq281db3359</td>
    <td class="tg-0lax">Important Farmland, San Mateo County, California, 2012</td>
    <td class="tg-0lax">2bf9c02a-c7d2-4417-a2da-ae1beed32bf4</td>
  </tr>
  <tr>
    <td class="tg-0lax">santabarbara2012.shp</td>
    <td class="tg-0lax">jj069zn7824</td>
    <td class="tg-0lax">Important Farmland, Santa Barbara County, California, 2012</td>
    <td class="tg-0lax">060f7c79-8fad-4a29-9ea1-3423488973cb</td>
  </tr>
  <tr>
    <td class="tg-0lax">santaclara2012.shp</td>
    <td class="tg-0lax">qp745bf7273</td>
    <td class="tg-0lax">Important Farmland, Santa Clara County, California, 2012</td>
    <td class="tg-0lax">2a4de43e-fdbb-4032-8204-4eeec4a397eb</td>
  </tr>
  <tr>
    <td class="tg-0lax">santacruz2012.shp</td>
    <td class="tg-0lax">vy418kq5214</td>
    <td class="tg-0lax">Important Farmland, Santa Cruz County, California, 2012</td>
    <td class="tg-0lax">377fca92-57e6-4255-a48f-c5918d26f0fb</td>
  </tr>
  <tr>
    <td class="tg-0lax">shasta2012.shp</td>
    <td class="tg-0lax">td166yy5765</td>
    <td class="tg-0lax">Important Farmland, Shasta County, California, 2012</td>
    <td class="tg-0lax">d36f6290-d795-4cf6-8e43-8a9317593d52</td>
  </tr>
  <tr>
    <td class="tg-0lax">sierravalleyarea2012.shp</td>
    <td class="tg-0lax">kb340bw7680</td>
    <td class="tg-0lax">Important Farmland, Sierra Valley, California, 2012</td>
    <td class="tg-0lax">752146b0-f5b2-4832-aa49-4378184709f7</td>
  </tr>
  <tr>
    <td class="tg-0lax">siskiyou2012.shp</td>
    <td class="tg-0lax">mm976fw5051</td>
    <td class="tg-0lax">Important Farmland, Siskiyou County, California, 2012</td>
    <td class="tg-0lax">6c55f328-a6a1-4efb-afcc-8fb091d3967f</td>
  </tr>
  <tr>
    <td class="tg-0lax">solano2012.shp</td>
    <td class="tg-0lax">pg782xg8454</td>
    <td class="tg-0lax">Important Farmland, Solano County, California, 2012</td>
    <td class="tg-0lax">35690743-d95c-4405-b825-4a58dd02410d</td>
  </tr>
  <tr>
    <td class="tg-0lax">sonoma2012.shp</td>
    <td class="tg-0lax">mm460bj7835</td>
    <td class="tg-0lax">Important Farmland, Sonoma County, California, 2012</td>
    <td class="tg-0lax">47c1c32d-25ff-420b-b210-53c90607d3ea</td>
  </tr>
  <tr>
    <td class="tg-0lax">stanislaus2012.shp</td>
    <td class="tg-0lax">vp054fy1179</td>
    <td class="tg-0lax">Important Farmland, Stanislaus County, California, 2012</td>
    <td class="tg-0lax">5643869d-6771-4dd4-80b6-525b3c004000</td>
  </tr>
  <tr>
    <td class="tg-0lax">statewide2012.shp</td>
    <td class="tg-0lax">rn450jx3747</td>
    <td class="tg-0lax">Important Farmland, California, 2012</td>
    <td class="tg-0lax">e63f2646-2c0a-432d-89ea-7daabc93328c</td>
  </tr>
  <tr>
    <td class="tg-0lax">sutter2012.shp</td>
    <td class="tg-0lax">xs855zn5792</td>
    <td class="tg-0lax">Important Farmland, Sutter County, California, 2012</td>
    <td class="tg-0lax">a56d0a69-6931-431d-befd-e7584497c367</td>
  </tr>
  <tr>
    <td class="tg-0lax">tehama2012.shp</td>
    <td class="tg-0lax">gy925pj0642</td>
    <td class="tg-0lax">Important Farmland, Tehama County, California, 2012</td>
    <td class="tg-0lax">060f7c79-8fad-4a29-9ea1-3423488973cb</td>
  </tr>
  <tr>
    <td class="tg-0lax">tulare2012.shp</td>
    <td class="tg-0lax">mk189fk3952</td>
    <td class="tg-0lax">Important Farmland, Tulare County, California, 2012</td>
    <td class="tg-0lax">061f7c79-8fad-4a29-9ea1-3423488973cb</td>
  </tr>
  <tr>
    <td class="tg-0lax">ventura2012.shp</td>
    <td class="tg-0lax">qw707pq8722</td>
    <td class="tg-0lax">Important Farmland, Ventura County, California, 2012</td>
    <td class="tg-0lax">050f7c79-8fad-4a29-9ea1-3423488973cb</td>
  </tr>
  <tr>
    <td class="tg-0lax">yolo2012.shp</td>
    <td class="tg-0lax">df739nf4899</td>
    <td class="tg-0lax">Important Farmland, Yolo County, California, 2012</td>
    <td class="tg-0lax">060f7c79-8fad-4a29-9ea1-3423488973df</td>
  </tr>
  <tr>
    <td class="tg-0lax">yuba2012.shp</td>
    <td class="tg-0lax">cm505yx7200</td>
    <td class="tg-0lax">Important Farmland, Yuba County, California, 2012</td>
    <td class="tg-0lax">060f7c89-8fad-4a39-9ea1-3423488973cb</td>
  </tr>
</table>
</details>



Save a copy of [this Python script](https://github.com/kimdurante/metadataWorkflow/blob/master/scripts/addMetadata.py) in the collection directory. 

Change the `AUTHOR` and `PUBLISHER` variables to display names for use in the citation field. 

Run:

```>>> python addMetadata.py```

The following fields will be autogenerated:

|FIELD|VALUE|
|:-----|:-----|
|Title|Important Farmland, Alameda County, California, 2012|
|Credit|California Farmland Mapping and Monitoring Program. (2012). Important Farmland, Alameda County, California, 2012. California Farmland Mapping and Monitoring Program. Available at: http://purl.stanford.edu/rp378rd3804.|
|Identifier|https://purl.stanford.edu/rp378rd3804|
|Metadata File Identifier|edu.stanford.purl:rp378rd3804|
|Dataset URI|https://purl.stanford.edu/rp378rd3804|
|Distribution Online Linkage|https://purl.stanford.edu/rp378rd3804|
|Distribution Online Name|alameda2012.shp|
|Feature Catalog Identifier|564c855e-e45a-47dc-b0c4-001839b00864|

#### Autogenerating Thumbnail Images

Currently only works for polygon data types.

[Use this Python script to autogenerate thumbnail images for polygon shapefile data](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/scripts/createThumbnails.py). This script will create a JPEG and insert the binary code into the ArcGISXML metadata.
