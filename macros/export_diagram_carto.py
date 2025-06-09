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

diag = elt
mas = diagcol.getArtefactsForDiagram ( diag )
el = modutils.createEList ()
el.add ( modutils.getStereotypeInProject ( "Gouvernance") )
el.add ( modutils.getStereotypeInProject ( "CartographieDataHub") )
el.add ( modutils.getStereotypeInProject ( "FluxSource") )
workbook = excelutils.createExcelWorkbook ()
xlsheetinfo = cartomgr.prepareExcelSheetForClasses ( workbook, cartomgr.SHEET_OBJETSMETIER, cartomgr.createExcelStereotypeInfoFromStereotypes ( el ), True )
cartomgr.generateExcelSheetLinesForSelectedClasses ( xlsheetinfo, excelutils.getExcelStyleEditWrap(workbook), True, mas.getAllClasses () )
xlsheetinfo = cartomgr.prepareExcelSheetForAttributes ( workbook, cartomgr.SHEET_DICTIONNAIRE, cartomgr.createExcelStereotypeInfoFromStereotypes ( el ), True )
cartomgr.generateExcelSheetLinesForSelectedAttributes ( xlsheetinfo, excelutils.getExcelStyleEditWrap(workbook), True, mas.getAllAttributes () )
filename = modutils.markFileNameDate( cartomgr.getConfigCartographyFilePath() + "Cartographie_Gouv_Flux_Datahub_Diagram_" + diag.getName () + ".xlsx" );
excelutils.closeAndWriteWorkbook ( workbook, filename );	
print filename	

