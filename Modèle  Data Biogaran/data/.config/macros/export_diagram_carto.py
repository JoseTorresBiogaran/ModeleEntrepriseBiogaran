def notifyMessage ( module, method, severity, message ):
    print ( module + " - " + method + " - " + repr(severity) + " - " + message )
    return

#Starting point
modutils = Modelio.getInstance().getModuleService().getPeerModule("ModelioUtils")
excelutils = Modelio.getInstance().getModuleService().getPeerModule("ExcelUtils")
cartomgr = Modelio.getInstance().getModuleService().getPeerModule("CartographyManager")
diagcol = Modelio.getInstance().getModuleService().getPeerModule("DiagramColorizer")
mn = modutils.getMessageNotifier ()
mn.subscribeListener ( notifyMessage )

diag = excelutils
mas = diagcol.getArtefactsForDiagram ( diag )
el = modutils.createEList ()
el.add ( modutils.getStereotypeInProject ( "Gouvernance") )
el.add ( modutils.getStereotypeInProject ( "CartographieDataHub") )
el.add ( modutils.getStereotypeInProject ( "FluxSource") )
workbook = excelutils.createExcelWorkbook ()
xlsheetinfo = cartomgr.prepareExcelSheetForPackages ( workbook, cartomgr.SHEET_DICTIONNAIRE, cartomgr.createExcelStereotypeInfoFromStereotypes ( el ), False )
cartomgr.generateExcelSheetLinesForSelectedAttributes ( xlsheetinfo, modutils.getExcelStyleEditWrap(workbook), False, mas.getAllAttributes () )
filename = modutils.markFileNameDate( cartomgr.getConfigCartographyFilePath() + "Cartographie_Gouv_Flux_Datahub_Diagram_" + diag.getName () + ".xlsx" );
pexcelutils.closeAndWriteWorkbook ( workbook, filename );		

for c in mas.getClasses ():
    for a in c.attributes:
            c