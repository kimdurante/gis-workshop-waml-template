#Synchronize Metadata (arc_sync_md.py). Walk through a directory of shapefiles and GeoTIFFs, and update the metadata.
import arcpy
from arcpy import env
import os

#Enter the path to the data directory
env.workspace = "W:\Africa_Marine_Atlas"

for dirs, subdirs, files in os.walk('.'):
    for f in files:
        if f.endswith(".shp") of f.endswith(".tif"):
            filePath = os.path.join(dirs, f)
            src_item_md = md.Metadata(filePath)
            print (src_item_md)
            src_item_md.synchronize("ALWAYS")
