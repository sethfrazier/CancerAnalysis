# Name: IDW_Ex_02.py
# Description: Interpolate a series of point features onto a rectangular 
#   raster using Inverse Distance Weighting (IDW).
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = r"C:\Users\sfrazier\Desktop\GEOG777\Project1"
env.overwriteOutput = True

# Set local variables
inPointFeatures = r"\well_nitrate\well_nitrate_WTM.shp"
zField = "nitr_ran"
##cellSize = 2000.0
power = 2
searchRadius = RadiusVariable(10,)

# Execute IDW
outIDW = Idw(inPointFeatures, zField, '', power, searchRadius)
##
### Save the output 
outIDW.save(r"C:\Users\sfrazier\Desktop\GEOG777\Project1\idwout1.tif")

aprx = arcpy.mp.ArcGISProject(r"C:\Users\sfrazier\Desktop\GEOG777\Project1\Project1\Project1.aprx")

idwTif = r"C:\Users\sfrazier\Desktop\GEOG777\Project1\idwout1.tif"
map1 = aprx.listMaps('IDWMap')[0]
map1.addDataFromPath(r"C:\Users\sfrazier\Desktop\GEOG777\Project1\idwout1.tif")


for m in aprx.listMaps():
    print("in da loop")
    print("Map: " + m.name)
    for lyr in m.listLayers():
        print("  " + lyr.name)
for l in aprx.listLayouts():
    print(l.name)

refLay=map1.listLayers()[0]
print("no name: " +refLay.name)
##
idwLay = map1.listLayers()[1]
print(idwLay.name)

map1.moveLayer(refLay, idwLay, 'BEFORE')

lyt = aprx.listLayouts()[1]
##for lyt in aprx.listLayouts():
##    print("  {0} ({1} x {2} {3})".format(lyt.name, lyt.pageHeight, lyt.pageWidth, lyt.pageUnits))
lyt.exportToJPEG(r"C:\Users\sfrazier\Desktop\Geog777\Project1\Images\Idw.jpg")
#del aprx
#m.removeLayer("hello")


#aprx.save()

#-----------------------------------------------------------------
# Set environment settings
#env.workspace = "C:/sapyexamples/data"

# Set local variables
inZoneData = r"cancer_tracts\cancer_tracts_WTM.shp"
zoneField = "GEOID10"
inValueRaster = idwTif
outTable = "zonalstat"


# Execute ZonalStatisticsAsTable
outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, inValueRaster, 
                                 outTable, "DATA", "MEAN")

#------------------------------------------------------------------------------------

# Name: AttributeSelection.py
# Purpose: Join a table to a featureclass and select the desired attributes


arcpy.env.qualifiedFieldNames = False
    
# Set local variables    
inFeatures = r"\cancer_tracts\cancer_tracts_WTM.shp"
joinTable = "zonalstat"
joinField = "GEOID10"
#expression = "vegtable.HABITAT = 1"
outFeature = "Tract_IDW"
    
# Join the feature layer to a table
canTract_joined_table = arcpy.AddJoin_management(inFeatures, joinField, joinTable, 
                                            joinField, "KEEP_COMMON")
    
# Copy the layer to a new permanent feature class
arcpy.CopyFeatures_management(canTract_joined_table, outFeature)
print ("created joined features")
#-------------------------------------------------------------------------------------------
##OrdinaryLeastSquares_stats (Input_Feature_Class, Unique_ID_Field, Output_Feature_Class,
##                            Dependent_Variable, Explanatory_Variables, {Coefficient_Output_Table},
##                            {Diagnostic_Output_Table}, {Output_Report_File})

#try:
    # Set the current workspace (to avoid having to specify the full path to the feature classes each time)
    #arcpy.env.workspace = workspace

    # Growth as a function of {log of starting income, dummy for South
    # counties, interaction term for South counties, population density}
    # Process: Ordinary Least Squares...
env.overwriteOutput = True

feature = r"C:\Users\sfrazier\Desktop\Geog777\Project1\Tract_IDW.shp"

ols = arcpy.OrdinaryLeastSquares_stats(feature, "Rowid_", "olsResults1.shp","canrate", "MEAN", "olsTable")

print ("OLS completed")

olsRes = r"C:\Users\sfrazier\Desktop\Geog777\Project1\olsResults1.shp"
map2 = aprx.listMaps()[2]
map2.addDataFromPath(olsRes)

lyt = aprx.listLayouts()[2]
lyt.exportToJPEG(r"C:\Users\sfrazier\Desktop\Geog777\Project1\Images\olsMap.jpg")

    # Create Spatial Weights Matrix (Can be based off input or output FC)
    # Process: Generate Spatial Weights Matrix... 
##    swm = arcpy.GenerateSpatialWeightsMatrix_stats("USCounties.shp", "MYID",
##                        "euclidean6Neighs.swm",
##                        "K_NEAREST_NEIGHBORS",
##                        "#", "#", "#", 6) 
                        

    # Calculate Moran's Index of Spatial Autocorrelation for 
    # OLS Residuals using a SWM File.  
    # Process: Spatial Autocorrelation (Morans I)...      
##    moransI = arcpy.SpatialAutocorrelation_stats("olsResults.shp", "Residual",
##                        "NO_REPORT", "GET_SPATIAL_WEIGHTS_FROM_FILE", 
##                        "EUCLIDEAN_DISTANCE", "NONE", "#", 
##                        "euclidean6Neighs.swm")

##except:
##    # If an error occurred when running the tool, print out the error message.
##    print(arcpy.GetMessages())

#-------------------------------------------------------------------------------------------
##SpatialAutocorrelation_stats (Input_Feature_Class, Input_Field, {Generate_Report},
##                              Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization,
##                              {Distance_Band_or_Threshold_Distance}, {Weights_Matrix_File})

##
###try:
##    # Set the current workspace (to avoid having to specify the full path to the feature classes each time)
##    #arcpy.env.workspace = workspace
##
##    # Growth as a function of {log of starting income, dummy for South
##    # counties, interaction term for South counties, population density}
##    # Process: Ordinary Least Squares... 
##    ols = arcpy.OrdinaryLeastSquares_stats("USCounties.shp", "MYID", 
##                        "olsResults.shp", "GROWTH",
##                        "LOGPCR69;SOUTH;LPCR_SOUTH;PopDen69",
##                        "olsCoefTab.dbf",
##                        "olsDiagTab.dbf")
##                        
##
##    # Calculate Moran's I Index of Spatial Autocorrelation for 
##    # OLS Residuals using a SWM File.  
##    # Process: Spatial Autocorrelation (Morans I)...

moransI = arcpy.SpatialAutocorrelation_stats(r"C:\Users\sfrazier\Desktop\Geog777\Project1\olsResults1.shp",
                                             "Residual", "GENERATE_REPORT", "INVERSE_DISTANCE",
                                             "EUCLIDEAN_DISTANCE", "NONE", "","")

print ("at the bottom")
####except:
####    # If an error occurred when running the tool, print out the error message.
####    print(arcpy.GetMessages())


#-------------------------------------------------------------------------------------------    

##refLyr = m.listLayers("Points of Interest")[0]
##m.insertLayer(refLyr, insertLyr, "BEFORE")
#aprx.saveACopy(r"C:\Projects\YosemiteNP\Yosemite_updated.aprx")
#aprx.save()
del aprx
