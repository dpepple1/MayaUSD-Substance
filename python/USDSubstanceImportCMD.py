import maya.api.OpenMaya as om
import maya.cmds as cmds
import USDSubstanceImport

# Not sure if this is necessary
def maya_useNewAPI():
    pass

def initializePlugin(plugin):
    vendor = "Derek Pepple"
    version = "1.0.0"

    pluging_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        pluging_fn.registerCommand(USDSubstanceCmd.COMMAND_NAME, USDSubstanceCmd.creator)
    except:
        om.MGlobal.displayError("Failed to register command {0}".format(USDSubstanceCmd))


def uninitializePlugin(plugin):
    plugin_fn = om.MFnPlugin(plugin)

    try:
        plugin_fn.deregisterCommand(USDSubstanceCmd.COMMAND_NAME)
    except:
        om.MGlobal.displayError("Failed to deregister command: {0}".format(USDSubstanceCmd))


class USDSubstanceCmd(om.MPxCommand):

    COMMAND_NAME = "usdSubstanceImport"

    def __init__(self):
        super(USDSubstanceCmd, self).__init__()
    

    def doIt(self, args):
        print("command executed")
        USDSubstanceImport.runInMaya()
        
    @staticmethod
    def creator():
        return USDSubstanceCmd()