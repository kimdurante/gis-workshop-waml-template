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
            src_item_md = md.Metadata(filePath)
            print (src_item_md)
            src_item_md.synchronize("ALWAYS")
