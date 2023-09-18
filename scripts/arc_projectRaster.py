#Reprojecting data (arc_project.py). Walk through a directory of shapefiles and GeoTIFFs, and reproject them to a specified projection.
import arcpy
from arcpy import env
import os

#path to the data directory (Ex. "W:\Africa_Marine_Atlas")
env.workspace = "PATH_TO_DIRECTORY"

#add EPSG code
outCS = arcpy.SpatialReference()
outCS.factoryCode = 4326
outCS.create()

#path to the output directory (Ex. "W:\Africa_Marine_Atlas\WGS84\")
outDir = "PATH_TO_DIRECTORY"

for dirs, subdirs, files in os.walk(env.workspace):
    for f in files:
        filePath = os.path.join(dirs, f)
        print (f)
        arcpy.management.ProjectRaster(filePath, outDir + f, outCS)
