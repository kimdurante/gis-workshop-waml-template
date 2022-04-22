#Reprojecting data (arc_project.py). Walk through a directory of shapefiles and GeoTIFFs, and reproject them to a specified projection.
import arcpy
from arcpy import env
import os

#path to the data directory
env.workspace = "W:\Africa_Marine_Atlas"

#add EPSG code
outCS = arcpy.SpatialReference()
outCS.factoryCode = 4326
outCS.create()

#path to the output directory
outDir = "W:\Africa_Marine_Atlas\WGS84\"

for dirs, subdirs, files in os.walk(env.workspace):
    for f in files:
        if f.startswith("MCE") and f.endswith(".3G_2020.tif"):
            filePath = os.path.join(dirs, f)
            print (f)
            arcpy.management.ProjectRaster(filePath, outDir + f, outCS)
