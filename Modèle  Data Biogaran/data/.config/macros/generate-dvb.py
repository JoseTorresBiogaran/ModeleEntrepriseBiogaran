

def notifyMessage ( module, method, severity, message ):
    print ( module + " - " + method + " - " + repr(severity) + " - " + message )
    return

#Starting point
modutils = Modelio.getInstance().getModuleService().getPeerModule("ModelioUtils")
excelutils = Modelio.getInstance().getModuleService().getPeerModule("ExcelUtils")
cartomgr = Modelio.getInstance().getModuleService().getPeerModule("CartographyManager")
diagcol = Modelio.getInstance().getModuleService().getPeerModule("DiagramColorizer")
ormgen = Modelio.getInstance().getModuleService().getPeerModule("JavaOrmGenerator")
dvbgen = Modelio.getInstance().getModuleService().getPeerModule("DatavaultBuilderGenerator")
mn = modutils.getMessageNotifier ()
mn.subscribeListener ( notifyMessage )

tr = modutils.createTransaction ( "gendvb" )
dvbgen.setConfigDatavaultBuilderVersion ( "8.2.1" )
dvbgen.setConfigTargetDatabase ( dvbgen.convertTargetDatabase ( "BigQuery" ) )
dvbgen.setConfigGenerationVersion ( dvbgen.convertGenerationVersion ( "Version2" ) )
dvbgen.setConfigGenerateDimensionSatellite ( dvbgen.convertConfigGenerateDimensionSatellite ( "GenerateObjectAttribute" ) )
dvbgen.setConfigGenerateColumnNamesSnake ( True )
dvbgen.setConfigGenerateZIPFile ( True )
#clean the model from any DVB information
dvbgen.removeAllUmlArtefactsDVB ()
#deploy DVB selection information from 
useCases = modutils.createPairList ()
useCases.add ( modutils.createPair ( "DispoMax", "Sprint1") )
dvbgen.selectUmlArtefactsDVBFromUseCases ( useCases )
#now deploy sprint names into the stallite names so that the incremental DVB config will happen smoothly
#so this will support federal enterprise model down to the DVB instance or data mesh (per usage) instances
#cartomgr.iterateModelAtRoot ( None, None, callbackattribute, None, None, None )
#set the target path
oldpath=dvbgen.getConfigDatavaultBuilderPath  ()  
newpath = modutils.getFullPathFromPrefixedPath( "$(Workspace)\\DatavaultBuilder\\SAPDemoSprint1" )
dvbgen.setConfigDatavaultBuilderPath  ( newpath )  
#generate the DVB json files on disk
dvbgen.deployDVBConfiguration ()
#reset the path
dvbgen.setConfigDatavaultBuilderPath  ( oldpath )  
#dont memorize the selection
modutils.rollbackTransaction ( tr )
#modutils.closeTransaction ( tr )
