for dirs, subdirs, files in os.walk(rootdir):
    for f in files:
        if f.endswith(".shp"):
            filePath = os.path.join(dirs, f)
            print (filePath)
            print (f, "...is being projected")
            arcpy.DefineProjection_management(filePath, sr)
