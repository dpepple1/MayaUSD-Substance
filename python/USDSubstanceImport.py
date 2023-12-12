# PySide2 Imports
from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia
from PySide2.QtGui import QIcon
from PySide2.QtCore import QObject, QSize, QCoreApplication, QRunnable, QThreadPool, Signal
from PySide2.QtWidgets import QFileDialog, QMessageBox, QListWidgetItem

# Other Imports
import maya.cmds as cmds
import sys
import importlib
import os
import glob
from pprint import pprint

# USD import
from pxr import Usd, UsdShade, Sdf

MATERIAL_PRIM = "mtl"

DIFFUSE_NAMES = ['base', 'diff']
METALLIC_NAMES = ['metal']
ROUGHNESS_NAMES = ['rough', 'specular']
NORMAL_NAMES = ['normal']
HEIGHT_NAMES = ['height']
ALL_NAMES = DIFFUSE_NAMES + METALLIC_NAMES + ROUGHNESS_NAMES + NORMAL_NAMES + HEIGHT_NAMES

print(__file__)

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, dir_path)

# Honestly I don't remember why you're supposed to do this
import UI.window as QTWindow
try:
    importlib.reload(QTWindow)
    import maya.OpenMayaUI as omui
    import shiboken2

except:
    print('Failed Imports')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = QTWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectEventHandlers()
        self.stage_detected = self.loadStages()
        self.addedItems = []
    
    def connectEventHandlers(self):
        '''
        Connects functions to event handlers
        '''
        self.ui.browseAllBtn.clicked.connect(self.browseAllFiles)
        self.ui.baseColorBtn.clicked.connect(lambda: self.browseSingle(self.ui.baseColorTxt))
        self.ui.roughnessBtn.clicked.connect(lambda: self.browseSingle(self.ui.roughnessTxt))
        self.ui.metallicBtn.clicked.connect(lambda: self.browseSingle(self.ui.metallicTxt))
        self.ui.normalBtn.clicked.connect(lambda: self.browseSingle(self.ui.normalTxt))
        self.ui.heightBtn.clicked.connect(lambda: self.browseSingle(self.ui.heightTxt))
        self.ui.addObjBtn.clicked.connect(lambda: self.addSelectedObjects(self.ui.objList))
        self.ui.clearObjBtn.clicked.connect(lambda: self.clearObjects(self.ui.objList))
        self.ui.submitNewBtn.clicked.connect(lambda: self.saveToNewLayer())

    def loadStages(self):
        stages = cmds.ls(type='mayaUsdProxyShape')
        if len(stages) == 0:
            self.alert('No Stage Found', 'No USD Stages were found in this scene.')
            return False
        else:
            for stage in stages:
                self.ui.stageCombo.addItem(stage)
            return True

    def browseSingle(self, button):
        '''
        Allows user to select a single file that will be populated into the 
        associated file category.
        '''
        dialog = QFileDialog(self)
        dialog.setNameFilter(self.tr("Images (*.png *.xpm *.jpg *.jpeg *.tx *.pix *.exr *.raw);;All Files (*.*)"))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()

        try:
            file = fileNames[0]
            button.setText(file)
        except:
            return #If no file selected

    def browseAllFiles(self):
        '''
        Allows user to select one or more files. If the user selects multiple
        files, they will be sorted into the correct categories. If the user 
        selects a single file, it will populate into the correct category and
        the other files will be grabbed automatically.
        '''
        fileNames = []

        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter(self.tr("Images (*.png *.xpm *.jpg *.jpeg *.tx *.pix *.exr *.raw);;All Files (*.*)"))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()

        alert = True
        
        if len(fileNames) == 1: #Grab Other files automatically
            #First grab the name of the file that is independent of the property type
            file = fileNames[0]
            basename = os.path.basename(file)
            dirname = os.path.dirname(file)
            _, ext = os.path.splitext(file)
            genericName = None
            for txtType in ALL_NAMES:
                try:
                    index = basename.lower().index(txtType)
                    genericName = basename[:index]
                    
                    regex = os.path.join(dirname, genericName + "*" + ext)
                    found_textures = glob.glob(regex)
                    if len(found_textures) > 1:
                        self.alert('Other Files Found', f'{len(found_textures) - 1} matching texture files were found.')
                        fileNames = found_textures
                        alert = False
                    break
                except:
                    pass

        self.populateTexts(fileNames, alert)
        

    def populateTexts(self, fileNames, alert = True):
        '''
        Places files in proper textboxes
        '''

        for file in fileNames:
            basename = os.path.basename(file)
            if any(lbl in basename.lower() for lbl in DIFFUSE_NAMES):
                self.ui.baseColorTxt.setText(file)
            elif any(lbl in basename.lower() for lbl in METALLIC_NAMES):
                self.ui.metallicTxt.setText(file)
            elif any(lbl in basename.lower() for lbl in ROUGHNESS_NAMES):
                self.ui.roughnessTxt.setText(file)
            elif any(lbl in basename.lower() for lbl in NORMAL_NAMES):
                self.ui.normalTxt.setText(file)
            elif any(lbl in basename.lower() for lbl in HEIGHT_NAMES):
                self.ui.heightTxt.setText(file)
            else:
                self.alert('Uncertain File', f'The file \"{file}\" could not be automatically matched with a texture category.')

    def tr(self, text):
        ''' No Idea what this is for '''
        return QObject.tr(self, text)
    
    def alert(self, title, msg):
        ''' Wrapper for QDialog functions '''
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(msg)
        button = dlg.exec_()

        if button == QMessageBox.Ok:
            return True
        
    def addSelectedObjects(self, listWidget):
        '''
        For reference : https://stackoverflow.com/questions/76558940/select-and-hide-multiple-usd-prims-in-maya
        '''
        selected = cmds.ls(sl=True, ufe = True)
        for item in selected:
            try:
                item_name = item.split(',')[1]
                if item_name not in self.addedItems:
                    listWidget.addItem(item_name)
                    self.addedItems.append(item_name)
            except:
                print("Error processing item:", item)

    def clearObjects(self, listWidget):
        listWidget.clear()
        self.addedItems = []

    def checkFormCompletion(self):
        '''
        Checks to see if all necessary form objects have been filled in
        '''
        incomplete_forms = []
        invalid_chars = ['/', ' ']

        if self.ui.matNameTxt.text() == '':
            incomplete_forms.append('Choose a material name')
        elif any( char in self.ui.matNameTxt.text() for char in invalid_chars):
            incomplete_forms.append('Material name cannot include any invalid characters: ("{0}")'.format('", "'.join(invalid_chars)))
        if self.ui.stageCombo.currentText() == u'Select Stage...':
            incomplete_forms.append('Select a stage to add materials to')
        
        print(self.ui.stageCombo.currentText())
        print(type(self.ui.stageCombo.currentText()))

        alert_str = "Please correct the following issues:"
        for form in incomplete_forms:
            alert_str += f'\n• {form}'
        
        incomplete = len(incomplete_forms) != 0

        if incomplete:
            self.alert('Incomplete Forms', alert_str)
            return False
        else:
            return True

    def getSelectedStage(self):
        try:
            stage_name = str(self.ui.stageCombo.currentText())
            stage_file = cmds.getAttr(stage_name + '.filePath')
            stage = Usd.Stage.Open(stage_file)
            return stage, stage_file #future calls to maya cmds require file path too

        except:
            #Likely means selected object wasn't a stage somehow
            return None
        
    def addMaterialsToLayer(self, layer):
        try:    
            # TODO: Check to see if /mat/ or /mtl/ exists already or not
            #       mtl<NUMBER>? is a scope prim. that exists directly under the root layer
            #       Might have to process this outside this function, or pass in root layer 
            #       as well. 
            # TODO: Check to make sure the name chosen for the texture doesn't already exist
    
            matname = self.ui.matNameTxt.text()

            material = UsdShade.Material.Define(layer, f'/{MATERIAL_PRIM}/{matname}') #Maybe put this in another try except blocK?
            pbrShader = UsdShade.Shader.Define(layer, f'/{MATERIAL_PRIM}/{matname}/{matname}Shader')

        except:
            self.alert('Error','There was an error adding the material to the layer.')
            

    def saveToNewLayer(self):
        stage, stage_file = self.getSelectedStage() 
        form_completed = self.checkFormCompletion()

        if not form_completed:
            return

        if stage:
            try:
                root_layer = stage.GetRootLayer()

                # We will add the new layer as an anonymous layer using a combination of Maya
                # commands and OpenUSD API calls:

                layer_txt = cmds.mayaUsdLayerEditor(stage_file, edit=True, addAnonymous="anonymousTextureLayer")
                anon_layer = Sdf.Find(layer_txt)

                self.addMaterialsToLayer(anon_layer)

                self.alert("Success!", "Materials successfully added to a new anonymous layer!")

            except Exception as e:
                self.alert("Error Building Texture", "The following error was encountered while building the textures: \n" + repr(e))
                return 

        else:
            self.alert("Stage Error", "There was an error building the stage object from the selected stage.")
            return 


# ------------------------------------ #


def getMayaWindow():
    pointer = omui.MQtUtil.mainWindow()
    if pointer is not None:
        return shiboken2.wrapInstance(int(pointer), QtWidgets.QWidget)
    
def runInMaya():
    mainWindow = MainWindow(getMayaWindow())
    if mainWindow.stage_detected:
        mainWindow.show()
