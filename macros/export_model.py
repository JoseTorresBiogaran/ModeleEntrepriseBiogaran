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
print modutils.getWorkspacePath ().getAbsolutePath ()
model = cartomgr.getModelForAllModel ();
txt = modutils.getTextFromModel ( model )
modutils.writeTextFile ( modutils.createFile ( modutils.getWorkspacePath ().getAbsolutePath () +  "/model.json" ), txt )