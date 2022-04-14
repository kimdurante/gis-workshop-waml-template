#Reprojecting data (arc_project.py). Walk through a directory of shapefiles and GeoTIFFs, and reproject them to a specified projection.
import arcpy
from arcpy import env
import os

#Path to the data directory
env.workspace = "W:\Africa_Marine_Atlas"
#Path to a projection file containing the desired projection metadata
sr = "W:\Africa_Marine_Atlas\ports.prj"

for dirs, subdirs, files in os.walk(rootdir):
    for f in files:
        if f.endswith(".shp") or f.endswith(".tif":
            filePath = os.path.join(dirs, f)
            try:
                spatial_ref = arcpy.Describe(filePath).spatialReference
                print (spatial_ref.name, " is the projection for ", f)
            else:
                print (f, "...is being projected")
                arcpy.DefineProjection_management(filePath, sr)
