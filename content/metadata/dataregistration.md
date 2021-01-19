layout: default
title: Registering Content
nav_order: 1
parent: Metadata

Registering data layers and creating Digital Repository Unique Identifiers (DRUIDs) in Argo

### Creating a Manifest

Create a spreadsheet manifest containing a SourceID and a Label for each layer in the collection. The Source ID prefix for all GIS layers is '*branner:*' plus an abbreviation for the collection name, followed by an underscore. Append the filename of the layer to the end of this prefix to create the Source ID.

Example Source ID: branner:fmmp12_alameda2012.shp

The Label is the title of the data layer. If the data already have an existing title, use it. For georeferenced maps, use the original map title plus '(Raster Image)'. Otherwise, create a title using the pattern: *What, Where, When*.

Examples:<br/> 
Topographical map of the Yosemite Valley and vicinity (Raster Image)<br/>
Roads, Congo, 2009

Format the manifest as shown below, leaving the first and third columns blank.

Example Collection: California Farmland Mapping and Monitoring Program, 2012

||SOURCEID||LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp||Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp||Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp||Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp||Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp||Important Farmland, Contra Costa County, California, 2012|

<details><summary>See All</summary>
<br/>
<table>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_eldorado2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, El Dorado County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_fresno2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Fresno County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_glenn2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Glenn County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_imperial2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Imperial County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_kern2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Kern County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_kings2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Kings County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_lake2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Lake County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_losangeles2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Los Angeles County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_madera2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Madera County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_marin2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Marin County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_mariposa2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Mariposa County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_mendocino2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Mendocino County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_merced2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Merced County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_modoc2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Modoc County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_monterey2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Monterey County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_napa2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Napa County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_nevada2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Nevada County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_orange2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Orange County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_placer2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Placer County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_riverside2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Riverside County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sacramento2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Sacramento County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanbenito2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, San Benito County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanbernardino2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, San Bernardino County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sandiego2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, San Diego County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanjoaquin2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, San Joaquin County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanluisobispo2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, San Luis Obispo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanmateo2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, San Mateo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_santabarbara2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Santa Barbara County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_santaclara2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Santa Clara County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_santacruz2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Santa Cruz County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_shasta2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Shasta County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sierravalleyarea2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Sierra Valley, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_siskiyou2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Siskiyou County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_solano2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Solano County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sonoma2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Sonoma County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_stanislaus2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Stanislaus County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_statewide2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sutter2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Sutter County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_tehama2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Tehama County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_tulare2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Tulare County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_ventura2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Ventura County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_yolo2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Yolo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_yuba2012.shp</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">Important Farmland, Yuba County, California, 2012</td>
  </tr>
</table>
</details>

### Create DRUIDs

Register the items in Argo under the appropriate APO and Collection. Use the Content Type ```File```.

||SOURCEID|DRUID|LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp|rc560ns7872|Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp|rc560ns7872|Important Farmland, Contra Costa County, California, 2012|
<details><summary>See All</summary>
<br/>
<table>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_eldorado2012.shp</td>
    <td class="tg-0lax">bd235mg0255</td>
    <td class="tg-0lax">Important Farmland, El Dorado County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_fresno2012.shp</td>
    <td class="tg-0lax">df831fg6767</td>
    <td class="tg-0lax">Important Farmland, Fresno County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_glenn2012.shp</td>
    <td class="tg-0lax">nd302nb7780</td>
    <td class="tg-0lax">Important Farmland, Glenn County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_imperial2012.shp</td>
    <td class="tg-0lax">bw755mz6720</td>
    <td class="tg-0lax">Important Farmland, Imperial County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_kern2012.shp</td>
    <td class="tg-0lax">tg135ph2124</td>
    <td class="tg-0lax">Important Farmland, Kern County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_kings2012.shp</td>
    <td class="tg-0lax">vx330xj9508</td>
    <td class="tg-0lax">Important Farmland, Kings County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_lake2012.shp</td>
    <td class="tg-0lax">vd631sr7734</td>
    <td class="tg-0lax">Important Farmland, Lake County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_losangeles2012.shp</td>
    <td class="tg-0lax">hk094xr8182</td>
    <td class="tg-0lax">Important Farmland, Los Angeles County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_madera2012.shp</td>
    <td class="tg-0lax">hc191sp2641</td>
    <td class="tg-0lax">Important Farmland, Madera County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_marin2012.shp</td>
    <td class="tg-0lax">sm826hp4918</td>
    <td class="tg-0lax">Important Farmland, Marin County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_mariposa2012.shp</td>
    <td class="tg-0lax">jw394jv6304</td>
    <td class="tg-0lax">Important Farmland, Mariposa County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_mendocino2012.shp</td>
    <td class="tg-0lax">cm997rw6211</td>
    <td class="tg-0lax">Important Farmland, Mendocino County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_merced2012.shp</td>
    <td class="tg-0lax">zq426cm9039</td>
    <td class="tg-0lax">Important Farmland, Merced County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_modoc2012.shp</td>
    <td class="tg-0lax">pr305dz0124</td>
    <td class="tg-0lax">Important Farmland, Modoc County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_monterey2012.shp</td>
    <td class="tg-0lax">xz952pd7686</td>
    <td class="tg-0lax">Important Farmland, Monterey County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_napa2012.shp</td>
    <td class="tg-0lax">ky438ry5906</td>
    <td class="tg-0lax">Important Farmland, Napa County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_nevada2012.shp</td>
    <td class="tg-0lax">ts340ts1571</td>
    <td class="tg-0lax">Important Farmland, Nevada County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_orange2012.shp</td>
    <td class="tg-0lax">vn468vq4911</td>
    <td class="tg-0lax">Important Farmland, Orange County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_placer2012.shp</td>
    <td class="tg-0lax">nt745qn0438</td>
    <td class="tg-0lax">Important Farmland, Placer County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_riverside2012.shp</td>
    <td class="tg-0lax">tw906cb9868</td>
    <td class="tg-0lax">Important Farmland, Riverside County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sacramento2012.shp</td>
    <td class="tg-0lax">fz917ht4816</td>
    <td class="tg-0lax">Important Farmland, Sacramento County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanbenito2012.shp</td>
    <td class="tg-0lax">df983nx3922</td>
    <td class="tg-0lax">Important Farmland, San Benito County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanbernardino2012.shp</td>
    <td class="tg-0lax">st501nt1256</td>
    <td class="tg-0lax">Important Farmland, San Bernardino County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sandiego2012.shp</td>
    <td class="tg-0lax">vs099sj0325</td>
    <td class="tg-0lax">Important Farmland, San Diego County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanjoaquin2012.shp</td>
    <td class="tg-0lax">hb437dj8324</td>
    <td class="tg-0lax">Important Farmland, San Joaquin County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanluisobispo2012.shp</td>
    <td class="tg-0lax">vv216kg8929</td>
    <td class="tg-0lax">Important Farmland, San Luis Obispo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sanmateo2012.shp</td>
    <td class="tg-0lax">wq281db3359</td>
    <td class="tg-0lax">Important Farmland, San Mateo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_santabarbara2012.shp</td>
    <td class="tg-0lax">jj069zn7824</td>
    <td class="tg-0lax">Important Farmland, Santa Barbara County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_santaclara2012.shp</td>
    <td class="tg-0lax">qp745bf7273</td>
    <td class="tg-0lax">Important Farmland, Santa Clara County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_santacruz2012.shp</td>
    <td class="tg-0lax">vy418kq5214</td>
    <td class="tg-0lax">Important Farmland, Santa Cruz County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_shasta2012.shp</td>
    <td class="tg-0lax">td166yy5765</td>
    <td class="tg-0lax">Important Farmland, Shasta County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sierravalleyarea2012.shp</td>
    <td class="tg-0lax">kb340bw7680</td>
    <td class="tg-0lax">Important Farmland, Sierra Valley, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_siskiyou2012.shp</td>
    <td class="tg-0lax">mm976fw5051</td>
    <td class="tg-0lax">Important Farmland, Siskiyou County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_solano2012.shp</td>
    <td class="tg-0lax">pg782xg8454</td>
    <td class="tg-0lax">Important Farmland, Solano County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sonoma2012.shp</td>
    <td class="tg-0lax">mm460bj7835</td>
    <td class="tg-0lax">Important Farmland, Sonoma County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_stanislaus2012.shp</td>
    <td class="tg-0lax">vp054fy1179</td>
    <td class="tg-0lax">Important Farmland, Stanislaus County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_statewide2012.shp</td>
    <td class="tg-0lax">rn450jx3747</td>
    <td class="tg-0lax">Important Farmland, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_sutter2012.shp</td>
    <td class="tg-0lax">xs855zn5792</td>
    <td class="tg-0lax">Important Farmland, Sutter County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_tehama2012.shp</td>
    <td class="tg-0lax">gy925pj0642</td>
    <td class="tg-0lax">Important Farmland, Tehama County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_tulare2012.shp</td>
    <td class="tg-0lax">mk189fk3952</td>
    <td class="tg-0lax">Important Farmland, Tulare County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_ventura2012.shp</td>
    <td class="tg-0lax">qw707pq8722</td>
    <td class="tg-0lax">Important Farmland, Ventura County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_yolo2012.shp</td>
    <td class="tg-0lax">df739nf4899</td>
    <td class="tg-0lax">Important Farmland, Yolo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">branner:fmmp12_yuba2012.shp</td>
    <td class="tg-0lax">cm505yx7200</td>
    <td class="tg-0lax">Important Farmland, Yuba County, California, 2012</td>
  </tr>
</table>
</details>

### Save the file

Delete the first column and remove the Source ID prefix from each filename. 

In the directory containing the data collection, save the file as: ```layers.csv``` 

|FILENAME|DRUID|LABEL|
|:----|:----|:----|
|alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|
|amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|
|butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|
|colusa2012.shp|rc560ns7872|Important Farmland, Colusa County, California, 2012|
<details>
<summary>See All</summary>
<br/>
<table>
  <tr>
    <td class="tg-0lax">﻿eldorado2012.shp</th>
    <td class="tg-0lax">bd235mg0255</th>
    <td class="tg-0lax">Important Farmland, El Dorado County, California, 2012</th>
  </tr>
  <tr>
    <td class="tg-0lax">fresno2012.shp</td>
    <td class="tg-0lax">df831fg6767</td>
    <td class="tg-0lax">Important Farmland, Fresno County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">glenn2012.shp</td>
    <td class="tg-0lax">nd302nb7780</td>
    <td class="tg-0lax">Important Farmland, Glenn County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">imperial2012.shp</td>
    <td class="tg-0lax">bw755mz6720</td>
    <td class="tg-0lax">Important Farmland, Imperial County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">kern2012.shp</td>
    <td class="tg-0lax">tg135ph2124</td>
    <td class="tg-0lax">Important Farmland, Kern County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">kings2012.shp</td>
    <td class="tg-0lax">vx330xj9508</td>
    <td class="tg-0lax">Important Farmland, Kings County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">lake2012.shp</td>
    <td class="tg-0lax">vd631sr7734</td>
    <td class="tg-0lax">Important Farmland, Lake County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">losangeles2012.shp</td>
    <td class="tg-0lax">hk094xr8182</td>
    <td class="tg-0lax">Important Farmland, Los Angeles County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">madera2012.shp</td>
    <td class="tg-0lax">hc191sp2641</td>
    <td class="tg-0lax">Important Farmland, Madera County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">marin2012.shp</td>
    <td class="tg-0lax">sm826hp4918</td>
    <td class="tg-0lax">Important Farmland, Marin County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">mariposa2012.shp</td>
    <td class="tg-0lax">jw394jv6304</td>
    <td class="tg-0lax">Important Farmland, Mariposa County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">mendocino2012.shp</td>
    <td class="tg-0lax">cm997rw6211</td>
    <td class="tg-0lax">Important Farmland, Mendocino County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">merced2012.shp</td>
    <td class="tg-0lax">zq426cm9039</td>
    <td class="tg-0lax">Important Farmland, Merced County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">modoc2012.shp</td>
    <td class="tg-0lax">pr305dz0124</td>
    <td class="tg-0lax">Important Farmland, Modoc County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">monterey2012.shp</td>
    <td class="tg-0lax">xz952pd7686</td>
    <td class="tg-0lax">Important Farmland, Monterey County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">napa2012.shp</td>
    <td class="tg-0lax">ky438ry5906</td>
    <td class="tg-0lax">Important Farmland, Napa County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">nevada2012.shp</td>
    <td class="tg-0lax">ts340ts1571</td>
    <td class="tg-0lax">Important Farmland, Nevada County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">orange2012.shp</td>
    <td class="tg-0lax">vn468vq4911</td>
    <td class="tg-0lax">Important Farmland, Orange County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">placer2012.shp</td>
    <td class="tg-0lax">nt745qn0438</td>
    <td class="tg-0lax">Important Farmland, Placer County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">riverside2012.shp</td>
    <td class="tg-0lax">tw906cb9868</td>
    <td class="tg-0lax">Important Farmland, Riverside County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sacramento2012.shp</td>
    <td class="tg-0lax">fz917ht4816</td>
    <td class="tg-0lax">Important Farmland, Sacramento County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanbenito2012.shp</td>
    <td class="tg-0lax">df983nx3922</td>
    <td class="tg-0lax">Important Farmland, San Benito County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanbernardino2012.shp</td>
    <td class="tg-0lax">st501nt1256</td>
    <td class="tg-0lax">Important Farmland, San Bernardino County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sandiego2012.shp</td>
    <td class="tg-0lax">vs099sj0325</td>
    <td class="tg-0lax">Important Farmland, San Diego County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanjoaquin2012.shp</td>
    <td class="tg-0lax">hb437dj8324</td>
    <td class="tg-0lax">Important Farmland, San Joaquin County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanluisobispo2012.shp</td>
    <td class="tg-0lax">vv216kg8929</td>
    <td class="tg-0lax">Important Farmland, San Luis Obispo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sanmateo2012.shp</td>
    <td class="tg-0lax">wq281db3359</td>
    <td class="tg-0lax">Important Farmland, San Mateo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">santabarbara2012.shp</td>
    <td class="tg-0lax">jj069zn7824</td>
    <td class="tg-0lax">Important Farmland, Santa Barbara County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">santaclara2012.shp</td>
    <td class="tg-0lax">qp745bf7273</td>
    <td class="tg-0lax">Important Farmland, Santa Clara County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">santacruz2012.shp</td>
    <td class="tg-0lax">vy418kq5214</td>
    <td class="tg-0lax">Important Farmland, Santa Cruz County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">shasta2012.shp</td>
    <td class="tg-0lax">td166yy5765</td>
    <td class="tg-0lax">Important Farmland, Shasta County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sierravalleyarea2012.shp</td>
    <td class="tg-0lax">kb340bw7680</td>
    <td class="tg-0lax">Important Farmland, Sierra Valley, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">siskiyou2012.shp</td>
    <td class="tg-0lax">mm976fw5051</td>
    <td class="tg-0lax">Important Farmland, Siskiyou County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">solano2012.shp</td>
    <td class="tg-0lax">pg782xg8454</td>
    <td class="tg-0lax">Important Farmland, Solano County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sonoma2012.shp</td>
    <td class="tg-0lax">mm460bj7835</td>
    <td class="tg-0lax">Important Farmland, Sonoma County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">stanislaus2012.shp</td>
    <td class="tg-0lax">vp054fy1179</td>
    <td class="tg-0lax">Important Farmland, Stanislaus County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">statewide2012.shp</td>
    <td class="tg-0lax">rn450jx3747</td>
    <td class="tg-0lax">Important Farmland, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">sutter2012.shp</td>
    <td class="tg-0lax">xs855zn5792</td>
    <td class="tg-0lax">Important Farmland, Sutter County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">tehama2012.shp</td>
    <td class="tg-0lax">gy925pj0642</td>
    <td class="tg-0lax">Important Farmland, Tehama County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">tulare2012.shp</td>
    <td class="tg-0lax">mk189fk3952</td>
    <td class="tg-0lax">Important Farmland, Tulare County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">ventura2012.shp</td>
    <td class="tg-0lax">qw707pq8722</td>
    <td class="tg-0lax">Important Farmland, Ventura County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">yolo2012.shp</td>
    <td class="tg-0lax">df739nf4899</td>
    <td class="tg-0lax">Important Farmland, Yolo County, California, 2012</td>
  </tr>
  <tr>
    <td class="tg-0lax">yuba2012.shp</td>
    <td class="tg-0lax">cm505yx7200</td>
    <td class="tg-0lax">Important Farmland, Yuba County, California, 2012</td>
  </tr>
</table>
</details>
