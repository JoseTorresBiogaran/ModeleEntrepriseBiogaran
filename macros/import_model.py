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
f = modutils.getWorkspacePath ().getAbsolutePath () +  "/model.json"
print f
model = modutils.loadModelFromFile  ( f )
tr = modutils.createTransaction ( "loadmodel" )
modutils.instantiateModel ( elt, model, False );
modutils.closeTransaction ( tr )