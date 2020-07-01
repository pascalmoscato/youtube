from pyfbsdk import *
import os
# Create the popup and set necessary initial values.
lFp = FBFilePopup()
lFp.Style = FBFilePopupStyle.kFBFilePopupSave
# Options
lOptions = FBFbxOptions(False)
#  --- YOU HAVE TO EDIT THIS PART BELOW ---
# Save only the selected models, in ASCII format so we can have a look at the file.
lOptions.SaveSelectedModelsOnly = True
lOptions.UseASCIIFormat = True
# Not saving system information; only focus on the selected models.
lOptions.BaseCameras = False
lOptions.CameraSwitcherSettings = False
lOptions.CurrentCameraSettings = False
lOptions.GlobalLightingSettings = False
lOptions.TransportSettings = False
# --- TO HERE ---
# BUG: If we do not set the filter, we will have an exception.
lFp.Filter = "*.fbx"
# Get the GUI to show.
lRes = lFp.Execute()
if lRes:
    lFilePath = os.path.join( lFp.Path, lFp.FileName )

