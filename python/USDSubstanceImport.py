# PySide2 Imports
from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia
from PySide2.QtGui import QIcon
from PySide2.QtCore import QObject, QSize, QCoreApplication, QRunnable, QThreadPool, Signal
from PySide2.QtWidgets import QFileDialog, QMessageBox

# Other Imports
import sys
import importlib
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, dir_path)

# Honestly I don't remember why you're supposed to do this
import UI.window as QTWindow
try:
    importlib.reload(QTWindow)
    import maya.OpenMayaUI as omui
    import shiboken2

except:
    pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.ui = QTWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectEventHandlers()
    
    def connectEventHandlers(self):
        '''
        Connects functions to event handlers
        '''
        self.ui.browseAllBtn.clicked.connect(self.browseAllFiles)
        

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
        
        self.populateTexts(fileNames)
        print(fileNames)
        

    def populateTexts(self, fileNames):
        '''
        Places files in proper textboxes
        '''
        
        diffuseNames = ['base', 'diff']
        metallicNames = ['metal']
        roughnessNames = ['rough', 'specular']
        normalNames = ['normal']
        heightNames = ['height']

        for file in fileNames:
            basename = os.path.basename(file)
            if any(lbl in basename.lower() for lbl in diffuseNames):
                self.ui.baseColorTxt.setText(file)
            elif any(lbl in basename.lower() for lbl in metallicNames):
                self.ui.metallicTxt.setText(file)
            elif any(lbl in basename.lower() for lbl in roughnessNames):
                self.ui.roughnessTxt.setText(file)
            elif any(lbl in basename.lower() for lbl in normalNames):
                self.ui.normalTxt.setText(file)
            elif any(lbl in basename.lower() for lbl in heightNames):
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


def getMayaWindow():
    pointer = omui.MQtUtil.mainWindow()
    if pointer is not None:
        return shiboken2.wrapInstance(int(pointer), QtWidgets.QWidget)
    
def runInMaya():
    mainWindow = MainWindow(getMayaWindow())
    mainWindow.show()

def runStandAlone():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    runStandAlone()