#Geog 777 project 1 - Using Tkinter, Python 3.6 and using ArcGIS Pro.
#By: Sfrazier Feb 28 2019

#import all modules need for project
import os
import arcpy
from arcpy import env
from arcpy.sa import *
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

# Defining the function for the geoprocessing analysis 
def run(*args):
    try:
        
        #setup workspace
        env.workspace = r"C:\Users\sfrazier\Desktop\GEOG777\Project1"
        env.overwriteOutput = True

        #Set arcGIS Pro project location - will be used throughout script.
        aprx = arcpy.mp.ArcGISProject(r"C:\Users\sfrazier\Desktop\GEOG777\Project1\Project1\Project1.aprx")
        
        # Set local variables for the IDW tool
        inPointFeatures = r"\well_nitrate\well_nitrate_WTM.shp"
        zField = "nitr_ran"
        ##cellSize = 2000.0
        power = float(powerEntry.get())
        searchRadius = RadiusVariable(10,)
        powerText = str(power)
        messagebox.showinfo("Running", "The analysis has begun using "+powerText+" for the power\n lease"\
                            " wait for the IDW process to complete.")

        # Execute IDW
        outIDW = Idw(inPointFeatures, zField, '', power, searchRadius)
        
        ## Save the output IDW as a Tiff
        outIDW.save(r"C:\Users\sfrazier\Desktop\GEOG777\Project1\outputFiles\idwout.tif")
            
        #Set variables for building the IDW jpeg map
        idwTif = r"C:\Users\sfrazier\Desktop\GEOG777\Project1\outputFiles\idwout.tif"
        
        # Locating the first map in the project
        map1 = aprx.listMaps('IDWMap')[0]
        map1.addDataFromPath(r"C:\Users\sfrazier\Desktop\GEOG777\Project1\outputFiles\idwout.tif")

        #define the Layers
        refLay=map1.listLayers()[0]
        #print("no name: " +refLay.name)
        moveLay = map1.listLayers()[1]
        #print(moveLay.name)

        #Apply symbology to the IDW raster
        sybLyr = r"C:\Users\sfrazier\Desktop\Geog777\Project1\outputFiles\idwout.lyrx"

        #apply symbology for the output raster
        arcpy.ApplySymbologyFromLayer_management (refLay, sybLyr)
        
        #rearrange the layers in the map to move the tracts above the raster.
        map1.moveLayer(refLay, moveLay, 'BEFORE')

        #locate correct layout to export the map
        lyt = aprx.listLayouts()[1]
        lyt.exportToJPEG(r"C:\Users\sfrazier\Desktop\Geog777\Project1\Images\Idw.jpg")

        #message box to let user know process has completed the IDW
        messagebox.showinfo("Completed IDW", "Completed IDW Interpolation.\n OLS process is now running.")

        #activate display IDW map button
        idwDisplay.config(state=NORMAL)
        
        # Set local variables for zonal join
        idwTif = r"C:\Users\sfrazier\Desktop\GEOG777\Project1\outputFiles\idwout.tif"
        inZoneData = r"cancer_tracts\cancer_tracts_WTM.shp"
        zoneField = "GEOID10"
        inValueRaster = idwTif
        outTable = "zonalstat"

        # Execute ZonalStatisticsAsTable
        outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, inValueRaster, 
                                     outTable, "DATA", "MEAN")

        #set the environment setting 
        arcpy.env.qualifiedFieldNames = False
        
        # Set local variables for the zonal table to census tracts shapefile
        inFeatures = r"\cancer_tracts\cancer_tracts_WTM.shp"
        joinTable = "zonalstat"
        joinField = "GEOID10"
        outFeature = r"outputFiles\Tract_IDW"
        
        # Join the feature layer to a table
        canTract_joined_table = arcpy.AddJoin_management(inFeatures, joinField, joinTable, 
                                                joinField, "KEEP_COMMON")
        
        # Copy the layer to a new permanent feature class
        arcpy.CopyFeatures_management(canTract_joined_table, outFeature)

        print("join")

        #Location of the Tract IDW.shp
        feature = r"C:\Users\sfrazier\Desktop\Geog777\Project1\outputFiles\Tract_IDW.shp"

        #run the OLS tool
        ols = arcpy.OrdinaryLeastSquares_stats(feature, "Rowid_", r"outputFiles\olsResults.shp",
                                               "canrate", "MEAN",'','', r"outputFiles\olsTable.pdf")
        print ("we got to the OLS")

        #Load data into OLS Map
        olsRes = r"C:\Users\sfrazier\Desktop\Geog777\Project1\outputFiles\olsResults.shp"
        map2 = aprx.listMaps("OLS")[0]
        map2.addDataFromPath(olsRes)

        #call the ols layout and export the map
        lyt1 = aprx.listLayouts("olsMap")[0]
        lyt1.exportToJPEG(r"C:\Users\sfrazier\Desktop\Geog777\Project1\Images\olsMap.jpg")

        #activate the olsDisplay button and show a feedback that OLS is completed
        olsDisplay.config(state=NORMAL)
        messagebox.showinfo("Completed OLS", "Completed OLS. \nPlease wait for process to complete")

        # run morans I 
        moransI = arcpy.SpatialAutocorrelation_stats(r"C:\Users\sfrazier\Desktop\Geog777\Project1\outputFiles\olsResults.shp",
                                                 "Residual", "GENERATE_REPORT", "INVERSE_DISTANCE",
                                                 "EUCLIDEAN_DISTANCE", "NONE", "","")
        #print("completed spatial Process")

        # activate ols button
        olsDisplay.config(state=NORMAL)

        #let user know that process is complete. 
        messagebox.showinfo("Process Completed", "Process Completed")

    except:
        #an error check to let user know to enter a number.
        messagebox.showwarning("Power Error", "Enter a number greater then 1\n for the power")
        print("please enter a number value")


#command for that to do when the user selects the IDW button        
def displayIDW():
    #locate the image and load into the GUI
    idwImage = Image.open(r"C:\Users\sfrazier\Desktop\Geog777\Project1\Images\Idw.jpg")
    idwImage = idwImage.resize((600,700), resample=Image.LANCZOS)
    photo1 = ImageTk.PhotoImage(idwImage)
    mapDisplay.configure(image=photo1)
    mapDisplay.photo = photo1

#command for that to do when the user selects the OLS button 
def displayOLS():
    #locate the image and load into the GUI
    olsImage = Image.open(r"C:\Users\sfrazier\Desktop\Geog777\Project1\Images\olsMap.jpg")
    olsImage = olsImage.resize((600,700), resample=Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(olsImage)
    mapDisplay.configure(image=photo2)
    mapDisplay.photo = photo2

#command for that to do when the user selects the idw help button
def idwHelp():
        # Text for the message box
    idwText="Inverse Weighted Distance (IDW) is the most widely used interpolation."\
            "\n\nIDW uses the theory of close things are more related than distant things most explicitly."\
            "\n\nIDW assigns weights quantitatively based on distance from a known point."\
            "\n\nThe power you enter will determine how quickly locations are no longer considered close."\
             "\n\nA higher power results in less influence"\
             "from distant points. It can be any real number greater than 0,"\
             "but the most reasonable results will be obtained using values"\
             "from 0.5 to 3."
    # message box command
    messagebox.showinfo("Inverse Weighted Distance", idwText)

#command for that to do when the user selects the ols help button
def olsHelp():
    olsText="Performs global Ordinary Least Squares (OLS) linear regression to generate predictions"\
             "or to model a dependent variable in terms of its relationships to a set of explanatory variables."
    messagebox.showinfo("Ordinary Least Squares", olsText)    

## Build the GUI
root = Tk()
root.title("Nitrates in Wells: Nitrates, Cancer, and Wells in Wisconsin")
#root.geometry("1000x800") did not use in this case
root.configure(background="slate grey")

# set styles for text and frame, must be used in ttk
t=ttk.Style()
t.configure('my.TLabel', font=('Times', 11), background = 'white')
t.configure('my.TFrame', background = 'white')
t.configure('title.TLabel', font = ('Times', 13), background = 'white')
t.configure('map.TLabel', background = 'slate grey')


##Section for the map display
imagePath = Image.open(r"C:\Users\sfrazier\Desktop\Geog777\Project1\Images\basemap.jpg")
imagePath = imagePath.resize((600,700), resample=Image.LANCZOS) # resize image
photo = ImageTk.PhotoImage(imagePath)
mapDisplay = ttk.Label(root,image = photo, style='map.TLabel')
mapDisplay.grid(column=1, row=0, rowspan=5, padx=(5,20), pady=20)

# text for the about dialog. 
projectDesc = "Explore the relationship between nitrate levels found in wells and "\
              "cancer in the State of Wisconsin. The tools used to explore if there "\
              "is a relationship are: Inverse Distance Weighted Interpolation or IDW "\
              "and Ordinary Least Squares Regression or OLS. \n\nAll the completed maps, output "\
              "statistics and PDF reports will be located in the appliction folder after "\
              "the analysis has been completed.\n\nClick on the buttons below "\
              "for more about either of these tools."

# build the about frame
textframe= ttk.Frame(root, borderwidth=2, style = 'my.TFrame')
textframe.grid(column=0, row=0, padx=(20,10),pady=(3,10))
textTitle = ttk.Label(textframe, text = "Nitrates in wells?", style = 'title.TLabel')
textTitle.grid(column = 0, row=0, columnspan = 5)

# text in the about frame
textLab= ttk.Label(textframe, text = projectDesc, wraplength= 300, style='my.TLabel')
textLab.grid(column=0, row=1, columnspan = 5, padx=10, pady=10)

# help buttons for more abut IDW and OLS - results will be a message box
idwHelp = ttk.Button(textframe, text = "About IDW", command= idwHelp).grid(column=1, row=4, padx=10, pady=5)
olsHelp = ttk.Button(textframe, text = "Obout OLS", command=olsHelp).grid(column=3, row=4, padx=10, pady=5)

# create a new frame for the power entry dialog
powerFrame = ttk.Frame(root, borderwidth=2, style = 'my.TFrame')
powerFrame.grid(column=0, row=1)

powerTitle = ttk.Label(powerFrame, text = 'Run Analysis', style = 'title.TLabel')
powerTitle.grid(row=0, columnspan=5)

powerVal=ttk.Label(powerFrame, text="Enter a power or k value for the IDW tool:", style = 'my.TLabel')
powerVal.grid(row=1, columnspan=5, padx=10, pady=10)

# the entry box for the power level.
powerLevel = StringVar()
powerEntry = ttk.Entry(powerFrame, textvariable = powerLevel)
powerEntry.grid(columnspan=5, row=3, pady=10)#, sticky=W)

# button to run the whole process.
runTool=ttk.Button(powerFrame, text="Run", command=run)
runTool.grid(row=4, column=2, padx=5, pady=10)

##Create a new frame for the different map displays
displays = ttk.Frame(root, style = 'my.TFrame')
displays.grid(row=2, column=0)

##Create the buttons to determine the map display
dispText = ttk.Label(displays, text="Select a map to display", style = 'title.TLabel')
idwDisplay = ttk.Button(displays, text="IDW", command=displayIDW)
olsDisplay = ttk.Button(displays, text="Regression", command=displayOLS)
idwDisplay.state(['disabled'])
olsDisplay.state(['disabled'])
dispText.grid(row=0, columnspan=5, padx=10, pady=5)
idwDisplay.grid(row=4,column=0, padx=10, pady=10)
olsDisplay.grid(row=4,column=3, padx=10, pady = 10)

# put the focus on the power entry widget and bind the return to the run button
powerEntry.focus()
root.bind('<Return>', run)

root.mainloop()
