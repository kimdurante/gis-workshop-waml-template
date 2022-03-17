import arcpy
from arcpy import env
import os

#
env.workspace = "W:\Africa_Marine_Atlas"
sr = "W:\Africa_Marine_Atlas\ports.prj"

for dirs, subdirs, files in os.walk(rootdir):
    for f in files:
        if f.endswith(".shp"):
            filePath = os.path.join(dirs, f)
            try:
                spatial_ref = arcpy.Describe(filePath).spatialReference
                print (spatial_ref.name, " is the projection for ", f)
            else:
                print (f, "...is being projected")
                arcpy.DefineProjection_management(filePath, sr)
