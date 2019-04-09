# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# StatsPortionOfScript.py
# Created on: 2019-02-04 20:18:06.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: StatsPortionOfScript <cancer_tracts_WTM> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
cancer_tracts_WTM = arcpy.GetParameterAsText(0)
if cancer_tracts_WTM == '#' or not cancer_tracts_WTM:
    cancer_tracts_WTM = "cancer_tracts_WTM" # provide a default value if unspecified

# Local variables:
cancer_tracts_WTM_Joined = cancer_tracts_WTM
well_nitrate_WTM = "well_nitrate_WTM"
Power = "2"
nitrate_IDW = "C:\\Users\\sfrazier\\Desktop\\Geog777\\Project1\\nitrate_IDW"
Zonal_Tracts_IDW = "C:\\Users\\sfrazier\\Desktop\\Geog777\\Project1\\Zonal_Tracts_IDW"
CancerTractsCalc_shp = "C:\\Users\\sfrazier\\Desktop\\Geog777\\Project1\\CancerTractsCalc.shp"
Coefficient_Output_Table = ""
Diagnostic_Output_Table = ""
olsTable_pdf = "C:\\Users\\sfrazier\\Desktop\\Geog777\\Project1\\olsTable.pdf"
OLSResults_shp = "C:\\Users\\sfrazier\\Desktop\\Geog777\\Project1\\OLSResults.shp"
Index = "0.208216"
ZScore = "29.938188"
PValue = "0"
MoransI_Result_3708_452__html = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\MoransI_Result_10556_10100_0.html"

# Process: IDW
tempEnvironment0 = arcpy.env.newPrecision
arcpy.env.newPrecision = "SINGLE"
tempEnvironment1 = arcpy.env.autoCommit
arcpy.env.autoCommit = "1000"
tempEnvironment2 = arcpy.env.XYResolution
arcpy.env.XYResolution = ""
tempEnvironment3 = arcpy.env.processingServerUser
arcpy.env.processingServerUser = ""
tempEnvironment4 = arcpy.env.XYDomain
arcpy.env.XYDomain = ""
tempEnvironment5 = arcpy.env.processingServerPassword
arcpy.env.processingServerPassword = ""
tempEnvironment6 = arcpy.env.scratchWorkspace
arcpy.env.scratchWorkspace = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment7 = arcpy.env.cartographicPartitions
arcpy.env.cartographicPartitions = ""
tempEnvironment8 = arcpy.env.terrainMemoryUsage
arcpy.env.terrainMemoryUsage = "false"
tempEnvironment9 = arcpy.env.MTolerance
arcpy.env.MTolerance = ""
tempEnvironment10 = arcpy.env.compression
arcpy.env.compression = "LZ77"
tempEnvironment11 = arcpy.env.coincidentPoints
arcpy.env.coincidentPoints = "MEAN"
tempEnvironment12 = arcpy.env.randomGenerator
arcpy.env.randomGenerator = "0 ACM599"
tempEnvironment13 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = ""
tempEnvironment14 = arcpy.env.rasterStatistics
arcpy.env.rasterStatistics = "STATISTICS 1 1"
tempEnvironment15 = arcpy.env.ZDomain
arcpy.env.ZDomain = ""
tempEnvironment16 = arcpy.env.transferDomains
arcpy.env.transferDomains = "false"
tempEnvironment17 = arcpy.env.maintainAttachments
arcpy.env.maintainAttachments = "true"
tempEnvironment18 = arcpy.env.resamplingMethod
arcpy.env.resamplingMethod = "NEAREST"
tempEnvironment19 = arcpy.env.snapRaster
arcpy.env.snapRaster = ""
tempEnvironment20 = arcpy.env.projectCompare
arcpy.env.projectCompare = "NONE"
tempEnvironment21 = arcpy.env.cartographicCoordinateSystem
arcpy.env.cartographicCoordinateSystem = ""
tempEnvironment22 = arcpy.env.configKeyword
arcpy.env.configKeyword = ""
tempEnvironment23 = arcpy.env.outputZFlag
arcpy.env.outputZFlag = "Same As Input"
tempEnvironment24 = arcpy.env.qualifiedFieldNames
arcpy.env.qualifiedFieldNames = "true"
tempEnvironment25 = arcpy.env.tileSize
arcpy.env.tileSize = "128 128"
tempEnvironment26 = arcpy.env.parallelProcessingFactor
arcpy.env.parallelProcessingFactor = ""
tempEnvironment27 = arcpy.env.pyramid
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP"
tempEnvironment28 = arcpy.env.referenceScale
arcpy.env.referenceScale = ""
tempEnvironment29 = arcpy.env.processingServer
arcpy.env.processingServer = ""
tempEnvironment30 = arcpy.env.extent
arcpy.env.extent = "DEFAULT"
tempEnvironment31 = arcpy.env.XYTolerance
arcpy.env.XYTolerance = ""
tempEnvironment32 = arcpy.env.tinSaveVersion
arcpy.env.tinSaveVersion = "CURRENT"
tempEnvironment33 = arcpy.env.nodata
arcpy.env.nodata = "NONE"
tempEnvironment34 = arcpy.env.MDomain
arcpy.env.MDomain = ""
tempEnvironment35 = arcpy.env.spatialGrid1
arcpy.env.spatialGrid1 = "0"
tempEnvironment36 = arcpy.env.cellSize
arcpy.env.cellSize = "MAXOF"
tempEnvironment37 = arcpy.env.outputZValue
arcpy.env.outputZValue = ""
tempEnvironment38 = arcpy.env.outputMFlag
arcpy.env.outputMFlag = "Same As Input"
tempEnvironment39 = arcpy.env.geographicTransformations
arcpy.env.geographicTransformations = ""
tempEnvironment40 = arcpy.env.spatialGrid2
arcpy.env.spatialGrid2 = "0"
tempEnvironment41 = arcpy.env.ZResolution
arcpy.env.ZResolution = ""
tempEnvironment42 = arcpy.env.mask
arcpy.env.mask = ""
tempEnvironment43 = arcpy.env.spatialGrid3
arcpy.env.spatialGrid3 = "0"
tempEnvironment44 = arcpy.env.maintainSpatialIndex
arcpy.env.maintainSpatialIndex = "false"
tempEnvironment45 = arcpy.env.workspace
arcpy.env.workspace = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment46 = arcpy.env.MResolution
arcpy.env.MResolution = ""
tempEnvironment47 = arcpy.env.derivedPrecision
arcpy.env.derivedPrecision = "HIGHEST"
tempEnvironment48 = arcpy.env.ZTolerance
arcpy.env.ZTolerance = ""
arcpy.gp.Idw_sa(well_nitrate_WTM, "nitr_ran", nitrate_IDW, "1850.21307268721", Power, "VARIABLE 12", "")
arcpy.env.newPrecision = tempEnvironment0
arcpy.env.autoCommit = tempEnvironment1
arcpy.env.XYResolution = tempEnvironment2
arcpy.env.processingServerUser = tempEnvironment3
arcpy.env.XYDomain = tempEnvironment4
arcpy.env.processingServerPassword = tempEnvironment5
arcpy.env.scratchWorkspace = tempEnvironment6
arcpy.env.cartographicPartitions = tempEnvironment7
arcpy.env.terrainMemoryUsage = tempEnvironment8
arcpy.env.MTolerance = tempEnvironment9
arcpy.env.compression = tempEnvironment10
arcpy.env.coincidentPoints = tempEnvironment11
arcpy.env.randomGenerator = tempEnvironment12
arcpy.env.outputCoordinateSystem = tempEnvironment13
arcpy.env.rasterStatistics = tempEnvironment14
arcpy.env.ZDomain = tempEnvironment15
arcpy.env.transferDomains = tempEnvironment16
arcpy.env.maintainAttachments = tempEnvironment17
arcpy.env.resamplingMethod = tempEnvironment18
arcpy.env.snapRaster = tempEnvironment19
arcpy.env.projectCompare = tempEnvironment20
arcpy.env.cartographicCoordinateSystem = tempEnvironment21
arcpy.env.configKeyword = tempEnvironment22
arcpy.env.outputZFlag = tempEnvironment23
arcpy.env.qualifiedFieldNames = tempEnvironment24
arcpy.env.tileSize = tempEnvironment25
arcpy.env.parallelProcessingFactor = tempEnvironment26
arcpy.env.pyramid = tempEnvironment27
arcpy.env.referenceScale = tempEnvironment28
arcpy.env.processingServer = tempEnvironment29
arcpy.env.extent = tempEnvironment30
arcpy.env.XYTolerance = tempEnvironment31
arcpy.env.tinSaveVersion = tempEnvironment32
arcpy.env.nodata = tempEnvironment33
arcpy.env.MDomain = tempEnvironment34
arcpy.env.spatialGrid1 = tempEnvironment35
arcpy.env.cellSize = tempEnvironment36
arcpy.env.outputZValue = tempEnvironment37
arcpy.env.outputMFlag = tempEnvironment38
arcpy.env.geographicTransformations = tempEnvironment39
arcpy.env.spatialGrid2 = tempEnvironment40
arcpy.env.ZResolution = tempEnvironment41
arcpy.env.mask = tempEnvironment42
arcpy.env.spatialGrid3 = tempEnvironment43
arcpy.env.maintainSpatialIndex = tempEnvironment44
arcpy.env.workspace = tempEnvironment45
arcpy.env.MResolution = tempEnvironment46
arcpy.env.derivedPrecision = tempEnvironment47
arcpy.env.ZTolerance = tempEnvironment48

# Process: Zonal Statistics as Table
tempEnvironment0 = arcpy.env.newPrecision
arcpy.env.newPrecision = "SINGLE"
tempEnvironment1 = arcpy.env.autoCommit
arcpy.env.autoCommit = "1000"
tempEnvironment2 = arcpy.env.XYResolution
arcpy.env.XYResolution = ""
tempEnvironment3 = arcpy.env.processingServerUser
arcpy.env.processingServerUser = ""
tempEnvironment4 = arcpy.env.XYDomain
arcpy.env.XYDomain = ""
tempEnvironment5 = arcpy.env.processingServerPassword
arcpy.env.processingServerPassword = ""
tempEnvironment6 = arcpy.env.scratchWorkspace
arcpy.env.scratchWorkspace = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment7 = arcpy.env.cartographicPartitions
arcpy.env.cartographicPartitions = ""
tempEnvironment8 = arcpy.env.terrainMemoryUsage
arcpy.env.terrainMemoryUsage = "false"
tempEnvironment9 = arcpy.env.MTolerance
arcpy.env.MTolerance = ""
tempEnvironment10 = arcpy.env.compression
arcpy.env.compression = "LZ77"
tempEnvironment11 = arcpy.env.coincidentPoints
arcpy.env.coincidentPoints = "MEAN"
tempEnvironment12 = arcpy.env.randomGenerator
arcpy.env.randomGenerator = "0 ACM599"
tempEnvironment13 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = ""
tempEnvironment14 = arcpy.env.rasterStatistics
arcpy.env.rasterStatistics = "STATISTICS 1 1"
tempEnvironment15 = arcpy.env.ZDomain
arcpy.env.ZDomain = ""
tempEnvironment16 = arcpy.env.transferDomains
arcpy.env.transferDomains = "false"
tempEnvironment17 = arcpy.env.maintainAttachments
arcpy.env.maintainAttachments = "true"
tempEnvironment18 = arcpy.env.resamplingMethod
arcpy.env.resamplingMethod = "NEAREST"
tempEnvironment19 = arcpy.env.snapRaster
arcpy.env.snapRaster = ""
tempEnvironment20 = arcpy.env.projectCompare
arcpy.env.projectCompare = "NONE"
tempEnvironment21 = arcpy.env.cartographicCoordinateSystem
arcpy.env.cartographicCoordinateSystem = ""
tempEnvironment22 = arcpy.env.configKeyword
arcpy.env.configKeyword = ""
tempEnvironment23 = arcpy.env.outputZFlag
arcpy.env.outputZFlag = "Same As Input"
tempEnvironment24 = arcpy.env.qualifiedFieldNames
arcpy.env.qualifiedFieldNames = "true"
tempEnvironment25 = arcpy.env.tileSize
arcpy.env.tileSize = "128 128"
tempEnvironment26 = arcpy.env.parallelProcessingFactor
arcpy.env.parallelProcessingFactor = ""
tempEnvironment27 = arcpy.env.pyramid
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP"
tempEnvironment28 = arcpy.env.referenceScale
arcpy.env.referenceScale = ""
tempEnvironment29 = arcpy.env.processingServer
arcpy.env.processingServer = ""
tempEnvironment30 = arcpy.env.extent
arcpy.env.extent = "DEFAULT"
tempEnvironment31 = arcpy.env.XYTolerance
arcpy.env.XYTolerance = ""
tempEnvironment32 = arcpy.env.tinSaveVersion
arcpy.env.tinSaveVersion = "CURRENT"
tempEnvironment33 = arcpy.env.nodata
arcpy.env.nodata = "NONE"
tempEnvironment34 = arcpy.env.MDomain
arcpy.env.MDomain = ""
tempEnvironment35 = arcpy.env.spatialGrid1
arcpy.env.spatialGrid1 = "0"
tempEnvironment36 = arcpy.env.cellSize
arcpy.env.cellSize = "MAXOF"
tempEnvironment37 = arcpy.env.outputZValue
arcpy.env.outputZValue = ""
tempEnvironment38 = arcpy.env.outputMFlag
arcpy.env.outputMFlag = "Same As Input"
tempEnvironment39 = arcpy.env.geographicTransformations
arcpy.env.geographicTransformations = ""
tempEnvironment40 = arcpy.env.spatialGrid2
arcpy.env.spatialGrid2 = "0"
tempEnvironment41 = arcpy.env.ZResolution
arcpy.env.ZResolution = ""
tempEnvironment42 = arcpy.env.mask
arcpy.env.mask = ""
tempEnvironment43 = arcpy.env.spatialGrid3
arcpy.env.spatialGrid3 = "0"
tempEnvironment44 = arcpy.env.maintainSpatialIndex
arcpy.env.maintainSpatialIndex = "false"
tempEnvironment45 = arcpy.env.workspace
arcpy.env.workspace = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment46 = arcpy.env.MResolution
arcpy.env.MResolution = ""
tempEnvironment47 = arcpy.env.derivedPrecision
arcpy.env.derivedPrecision = "HIGHEST"
tempEnvironment48 = arcpy.env.ZTolerance
arcpy.env.ZTolerance = ""
arcpy.gp.ZonalStatisticsAsTable_sa(cancer_tracts_WTM, "GEOID10", nitrate_IDW, Zonal_Tracts_IDW, "DATA", "MEAN")
arcpy.env.newPrecision = tempEnvironment0
arcpy.env.autoCommit = tempEnvironment1
arcpy.env.XYResolution = tempEnvironment2
arcpy.env.processingServerUser = tempEnvironment3
arcpy.env.XYDomain = tempEnvironment4
arcpy.env.processingServerPassword = tempEnvironment5
arcpy.env.scratchWorkspace = tempEnvironment6
arcpy.env.cartographicPartitions = tempEnvironment7
arcpy.env.terrainMemoryUsage = tempEnvironment8
arcpy.env.MTolerance = tempEnvironment9
arcpy.env.compression = tempEnvironment10
arcpy.env.coincidentPoints = tempEnvironment11
arcpy.env.randomGenerator = tempEnvironment12
arcpy.env.outputCoordinateSystem = tempEnvironment13
arcpy.env.rasterStatistics = tempEnvironment14
arcpy.env.ZDomain = tempEnvironment15
arcpy.env.transferDomains = tempEnvironment16
arcpy.env.maintainAttachments = tempEnvironment17
arcpy.env.resamplingMethod = tempEnvironment18
arcpy.env.snapRaster = tempEnvironment19
arcpy.env.projectCompare = tempEnvironment20
arcpy.env.cartographicCoordinateSystem = tempEnvironment21
arcpy.env.configKeyword = tempEnvironment22
arcpy.env.outputZFlag = tempEnvironment23
arcpy.env.qualifiedFieldNames = tempEnvironment24
arcpy.env.tileSize = tempEnvironment25
arcpy.env.parallelProcessingFactor = tempEnvironment26
arcpy.env.pyramid = tempEnvironment27
arcpy.env.referenceScale = tempEnvironment28
arcpy.env.processingServer = tempEnvironment29
arcpy.env.extent = tempEnvironment30
arcpy.env.XYTolerance = tempEnvironment31
arcpy.env.tinSaveVersion = tempEnvironment32
arcpy.env.nodata = tempEnvironment33
arcpy.env.MDomain = tempEnvironment34
arcpy.env.spatialGrid1 = tempEnvironment35
arcpy.env.cellSize = tempEnvironment36
arcpy.env.outputZValue = tempEnvironment37
arcpy.env.outputMFlag = tempEnvironment38
arcpy.env.geographicTransformations = tempEnvironment39
arcpy.env.spatialGrid2 = tempEnvironment40
arcpy.env.ZResolution = tempEnvironment41
arcpy.env.mask = tempEnvironment42
arcpy.env.spatialGrid3 = tempEnvironment43
arcpy.env.maintainSpatialIndex = tempEnvironment44
arcpy.env.workspace = tempEnvironment45
arcpy.env.MResolution = tempEnvironment46
arcpy.env.derivedPrecision = tempEnvironment47
arcpy.env.ZTolerance = tempEnvironment48

# Process: Add Join
arcpy.AddJoin_management(cancer_tracts_WTM, "GEOID10", Zonal_Tracts_IDW, "GEOID10", "KEEP_COMMON")

# Process: Copy Features
arcpy.CopyFeatures_management(cancer_tracts_WTM_Joined, CancerTractsCalc_shp, "", "0", "0", "0")

# Process: Ordinary Least Squares
tempEnvironment0 = arcpy.env.newPrecision
arcpy.env.newPrecision = "SINGLE"
tempEnvironment1 = arcpy.env.autoCommit
arcpy.env.autoCommit = "1000"
tempEnvironment2 = arcpy.env.XYResolution
arcpy.env.XYResolution = ""
tempEnvironment3 = arcpy.env.processingServerUser
arcpy.env.processingServerUser = ""
tempEnvironment4 = arcpy.env.XYDomain
arcpy.env.XYDomain = ""
tempEnvironment5 = arcpy.env.processingServerPassword
arcpy.env.processingServerPassword = ""
tempEnvironment6 = arcpy.env.scratchWorkspace
arcpy.env.scratchWorkspace = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment7 = arcpy.env.cartographicPartitions
arcpy.env.cartographicPartitions = ""
tempEnvironment8 = arcpy.env.terrainMemoryUsage
arcpy.env.terrainMemoryUsage = "false"
tempEnvironment9 = arcpy.env.MTolerance
arcpy.env.MTolerance = ""
tempEnvironment10 = arcpy.env.compression
arcpy.env.compression = "LZ77"
tempEnvironment11 = arcpy.env.coincidentPoints
arcpy.env.coincidentPoints = "MEAN"
tempEnvironment12 = arcpy.env.randomGenerator
arcpy.env.randomGenerator = "0 ACM599"
tempEnvironment13 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = ""
tempEnvironment14 = arcpy.env.rasterStatistics
arcpy.env.rasterStatistics = "STATISTICS 1 1"
tempEnvironment15 = arcpy.env.ZDomain
arcpy.env.ZDomain = ""
tempEnvironment16 = arcpy.env.transferDomains
arcpy.env.transferDomains = "false"
tempEnvironment17 = arcpy.env.maintainAttachments
arcpy.env.maintainAttachments = "true"
tempEnvironment18 = arcpy.env.resamplingMethod
arcpy.env.resamplingMethod = "NEAREST"
tempEnvironment19 = arcpy.env.snapRaster
arcpy.env.snapRaster = ""
tempEnvironment20 = arcpy.env.projectCompare
arcpy.env.projectCompare = "NONE"
tempEnvironment21 = arcpy.env.cartographicCoordinateSystem
arcpy.env.cartographicCoordinateSystem = ""
tempEnvironment22 = arcpy.env.configKeyword
arcpy.env.configKeyword = ""
tempEnvironment23 = arcpy.env.outputZFlag
arcpy.env.outputZFlag = "Same As Input"
tempEnvironment24 = arcpy.env.qualifiedFieldNames
arcpy.env.qualifiedFieldNames = "true"
tempEnvironment25 = arcpy.env.tileSize
arcpy.env.tileSize = "128 128"
tempEnvironment26 = arcpy.env.parallelProcessingFactor
arcpy.env.parallelProcessingFactor = ""
tempEnvironment27 = arcpy.env.pyramid
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP"
tempEnvironment28 = arcpy.env.referenceScale
arcpy.env.referenceScale = ""
tempEnvironment29 = arcpy.env.processingServer
arcpy.env.processingServer = ""
tempEnvironment30 = arcpy.env.extent
arcpy.env.extent = "DEFAULT"
tempEnvironment31 = arcpy.env.XYTolerance
arcpy.env.XYTolerance = ""
tempEnvironment32 = arcpy.env.tinSaveVersion
arcpy.env.tinSaveVersion = "CURRENT"
tempEnvironment33 = arcpy.env.nodata
arcpy.env.nodata = "NONE"
tempEnvironment34 = arcpy.env.MDomain
arcpy.env.MDomain = ""
tempEnvironment35 = arcpy.env.spatialGrid1
arcpy.env.spatialGrid1 = "0"
tempEnvironment36 = arcpy.env.cellSize
arcpy.env.cellSize = "MAXOF"
tempEnvironment37 = arcpy.env.outputZValue
arcpy.env.outputZValue = ""
tempEnvironment38 = arcpy.env.outputMFlag
arcpy.env.outputMFlag = "Same As Input"
tempEnvironment39 = arcpy.env.geographicTransformations
arcpy.env.geographicTransformations = ""
tempEnvironment40 = arcpy.env.spatialGrid2
arcpy.env.spatialGrid2 = "0"
tempEnvironment41 = arcpy.env.ZResolution
arcpy.env.ZResolution = ""
tempEnvironment42 = arcpy.env.mask
arcpy.env.mask = ""
tempEnvironment43 = arcpy.env.spatialGrid3
arcpy.env.spatialGrid3 = "0"
tempEnvironment44 = arcpy.env.maintainSpatialIndex
arcpy.env.maintainSpatialIndex = "false"
tempEnvironment45 = arcpy.env.workspace
arcpy.env.workspace = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment46 = arcpy.env.MResolution
arcpy.env.MResolution = ""
tempEnvironment47 = arcpy.env.derivedPrecision
arcpy.env.derivedPrecision = "HIGHEST"
tempEnvironment48 = arcpy.env.ZTolerance
arcpy.env.ZTolerance = ""
arcpy.OrdinaryLeastSquares_stats(CancerTractsCalc_shp, "zonal_trac", OLSResults_shp, "cancer_t_2", "zonal_tr_5", Coefficient_Output_Table, Diagnostic_Output_Table, olsTable_pdf)
arcpy.env.newPrecision = tempEnvironment0
arcpy.env.autoCommit = tempEnvironment1
arcpy.env.XYResolution = tempEnvironment2
arcpy.env.processingServerUser = tempEnvironment3
arcpy.env.XYDomain = tempEnvironment4
arcpy.env.processingServerPassword = tempEnvironment5
arcpy.env.scratchWorkspace = tempEnvironment6
arcpy.env.cartographicPartitions = tempEnvironment7
arcpy.env.terrainMemoryUsage = tempEnvironment8
arcpy.env.MTolerance = tempEnvironment9
arcpy.env.compression = tempEnvironment10
arcpy.env.coincidentPoints = tempEnvironment11
arcpy.env.randomGenerator = tempEnvironment12
arcpy.env.outputCoordinateSystem = tempEnvironment13
arcpy.env.rasterStatistics = tempEnvironment14
arcpy.env.ZDomain = tempEnvironment15
arcpy.env.transferDomains = tempEnvironment16
arcpy.env.maintainAttachments = tempEnvironment17
arcpy.env.resamplingMethod = tempEnvironment18
arcpy.env.snapRaster = tempEnvironment19
arcpy.env.projectCompare = tempEnvironment20
arcpy.env.cartographicCoordinateSystem = tempEnvironment21
arcpy.env.configKeyword = tempEnvironment22
arcpy.env.outputZFlag = tempEnvironment23
arcpy.env.qualifiedFieldNames = tempEnvironment24
arcpy.env.tileSize = tempEnvironment25
arcpy.env.parallelProcessingFactor = tempEnvironment26
arcpy.env.pyramid = tempEnvironment27
arcpy.env.referenceScale = tempEnvironment28
arcpy.env.processingServer = tempEnvironment29
arcpy.env.extent = tempEnvironment30
arcpy.env.XYTolerance = tempEnvironment31
arcpy.env.tinSaveVersion = tempEnvironment32
arcpy.env.nodata = tempEnvironment33
arcpy.env.MDomain = tempEnvironment34
arcpy.env.spatialGrid1 = tempEnvironment35
arcpy.env.cellSize = tempEnvironment36
arcpy.env.outputZValue = tempEnvironment37
arcpy.env.outputMFlag = tempEnvironment38
arcpy.env.geographicTransformations = tempEnvironment39
arcpy.env.spatialGrid2 = tempEnvironment40
arcpy.env.ZResolution = tempEnvironment41
arcpy.env.mask = tempEnvironment42
arcpy.env.spatialGrid3 = tempEnvironment43
arcpy.env.maintainSpatialIndex = tempEnvironment44
arcpy.env.workspace = tempEnvironment45
arcpy.env.MResolution = tempEnvironment46
arcpy.env.derivedPrecision = tempEnvironment47
arcpy.env.ZTolerance = tempEnvironment48

# Process: Spatial Autocorrelation (Morans I)
tempEnvironment0 = arcpy.env.newPrecision
arcpy.env.newPrecision = "SINGLE"
tempEnvironment1 = arcpy.env.autoCommit
arcpy.env.autoCommit = "1000"
tempEnvironment2 = arcpy.env.XYResolution
arcpy.env.XYResolution = ""
tempEnvironment3 = arcpy.env.processingServerUser
arcpy.env.processingServerUser = ""
tempEnvironment4 = arcpy.env.XYDomain
arcpy.env.XYDomain = ""
tempEnvironment5 = arcpy.env.processingServerPassword
arcpy.env.processingServerPassword = ""
tempEnvironment6 = arcpy.env.scratchWorkspace
arcpy.env.scratchWorkspace = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment7 = arcpy.env.cartographicPartitions
arcpy.env.cartographicPartitions = ""
tempEnvironment8 = arcpy.env.terrainMemoryUsage
arcpy.env.terrainMemoryUsage = "false"
tempEnvironment9 = arcpy.env.MTolerance
arcpy.env.MTolerance = ""
tempEnvironment10 = arcpy.env.compression
arcpy.env.compression = "LZ77"
tempEnvironment11 = arcpy.env.coincidentPoints
arcpy.env.coincidentPoints = "MEAN"
tempEnvironment12 = arcpy.env.randomGenerator
arcpy.env.randomGenerator = "0 ACM599"
tempEnvironment13 = arcpy.env.outputCoordinateSystem
arcpy.env.outputCoordinateSystem = ""
tempEnvironment14 = arcpy.env.rasterStatistics
arcpy.env.rasterStatistics = "STATISTICS 1 1"
tempEnvironment15 = arcpy.env.ZDomain
arcpy.env.ZDomain = ""
tempEnvironment16 = arcpy.env.transferDomains
arcpy.env.transferDomains = "false"
tempEnvironment17 = arcpy.env.maintainAttachments
arcpy.env.maintainAttachments = "true"
tempEnvironment18 = arcpy.env.resamplingMethod
arcpy.env.resamplingMethod = "NEAREST"
tempEnvironment19 = arcpy.env.snapRaster
arcpy.env.snapRaster = ""
tempEnvironment20 = arcpy.env.projectCompare
arcpy.env.projectCompare = "NONE"
tempEnvironment21 = arcpy.env.cartographicCoordinateSystem
arcpy.env.cartographicCoordinateSystem = ""
tempEnvironment22 = arcpy.env.configKeyword
arcpy.env.configKeyword = ""
tempEnvironment23 = arcpy.env.outputZFlag
arcpy.env.outputZFlag = "Same As Input"
tempEnvironment24 = arcpy.env.qualifiedFieldNames
arcpy.env.qualifiedFieldNames = "true"
tempEnvironment25 = arcpy.env.tileSize
arcpy.env.tileSize = "128 128"
tempEnvironment26 = arcpy.env.parallelProcessingFactor
arcpy.env.parallelProcessingFactor = ""
tempEnvironment27 = arcpy.env.pyramid
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP"
tempEnvironment28 = arcpy.env.referenceScale
arcpy.env.referenceScale = ""
tempEnvironment29 = arcpy.env.processingServer
arcpy.env.processingServer = ""
tempEnvironment30 = arcpy.env.extent
arcpy.env.extent = "DEFAULT"
tempEnvironment31 = arcpy.env.XYTolerance
arcpy.env.XYTolerance = ""
tempEnvironment32 = arcpy.env.tinSaveVersion
arcpy.env.tinSaveVersion = "CURRENT"
tempEnvironment33 = arcpy.env.nodata
arcpy.env.nodata = "NONE"
tempEnvironment34 = arcpy.env.MDomain
arcpy.env.MDomain = ""
tempEnvironment35 = arcpy.env.spatialGrid1
arcpy.env.spatialGrid1 = "0"
tempEnvironment36 = arcpy.env.cellSize
arcpy.env.cellSize = "MAXOF"
tempEnvironment37 = arcpy.env.outputZValue
arcpy.env.outputZValue = ""
tempEnvironment38 = arcpy.env.outputMFlag
arcpy.env.outputMFlag = "Same As Input"
tempEnvironment39 = arcpy.env.geographicTransformations
arcpy.env.geographicTransformations = ""
tempEnvironment40 = arcpy.env.spatialGrid2
arcpy.env.spatialGrid2 = "0"
tempEnvironment41 = arcpy.env.ZResolution
arcpy.env.ZResolution = ""
tempEnvironment42 = arcpy.env.mask
arcpy.env.mask = ""
tempEnvironment43 = arcpy.env.spatialGrid3
arcpy.env.spatialGrid3 = "0"
tempEnvironment44 = arcpy.env.maintainSpatialIndex
arcpy.env.maintainSpatialIndex = "false"
tempEnvironment45 = arcpy.env.workspace
arcpy.env.workspace = "C:\\Users\\sfrazier\\Documents\\ArcGIS\\Default.gdb"
tempEnvironment46 = arcpy.env.MResolution
arcpy.env.MResolution = ""
tempEnvironment47 = arcpy.env.derivedPrecision
arcpy.env.derivedPrecision = "HIGHEST"
tempEnvironment48 = arcpy.env.ZTolerance
arcpy.env.ZTolerance = ""
arcpy.SpatialAutocorrelation_stats(OLSResults_shp, "Residual", "GENERATE_REPORT", "INVERSE_DISTANCE", "EUCLIDEAN_DISTANCE", "NONE", "", "")
arcpy.env.newPrecision = tempEnvironment0
arcpy.env.autoCommit = tempEnvironment1
arcpy.env.XYResolution = tempEnvironment2
arcpy.env.processingServerUser = tempEnvironment3
arcpy.env.XYDomain = tempEnvironment4
arcpy.env.processingServerPassword = tempEnvironment5
arcpy.env.scratchWorkspace = tempEnvironment6
arcpy.env.cartographicPartitions = tempEnvironment7
arcpy.env.terrainMemoryUsage = tempEnvironment8
arcpy.env.MTolerance = tempEnvironment9
arcpy.env.compression = tempEnvironment10
arcpy.env.coincidentPoints = tempEnvironment11
arcpy.env.randomGenerator = tempEnvironment12
arcpy.env.outputCoordinateSystem = tempEnvironment13
arcpy.env.rasterStatistics = tempEnvironment14
arcpy.env.ZDomain = tempEnvironment15
arcpy.env.transferDomains = tempEnvironment16
arcpy.env.maintainAttachments = tempEnvironment17
arcpy.env.resamplingMethod = tempEnvironment18
arcpy.env.snapRaster = tempEnvironment19
arcpy.env.projectCompare = tempEnvironment20
arcpy.env.cartographicCoordinateSystem = tempEnvironment21
arcpy.env.configKeyword = tempEnvironment22
arcpy.env.outputZFlag = tempEnvironment23
arcpy.env.qualifiedFieldNames = tempEnvironment24
arcpy.env.tileSize = tempEnvironment25
arcpy.env.parallelProcessingFactor = tempEnvironment26
arcpy.env.pyramid = tempEnvironment27
arcpy.env.referenceScale = tempEnvironment28
arcpy.env.processingServer = tempEnvironment29
arcpy.env.extent = tempEnvironment30
arcpy.env.XYTolerance = tempEnvironment31
arcpy.env.tinSaveVersion = tempEnvironment32
arcpy.env.nodata = tempEnvironment33
arcpy.env.MDomain = tempEnvironment34
arcpy.env.spatialGrid1 = tempEnvironment35
arcpy.env.cellSize = tempEnvironment36
arcpy.env.outputZValue = tempEnvironment37
arcpy.env.outputMFlag = tempEnvironment38
arcpy.env.geographicTransformations = tempEnvironment39
arcpy.env.spatialGrid2 = tempEnvironment40
arcpy.env.ZResolution = tempEnvironment41
arcpy.env.mask = tempEnvironment42
arcpy.env.spatialGrid3 = tempEnvironment43
arcpy.env.maintainSpatialIndex = tempEnvironment44
arcpy.env.workspace = tempEnvironment45
arcpy.env.MResolution = tempEnvironment46
arcpy.env.derivedPrecision = tempEnvironment47
arcpy.env.ZTolerance = tempEnvironment48

