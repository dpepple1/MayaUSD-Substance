# PySide2 Imports
from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, QCoreApplication, QRunnable, QThreadPool, Signal

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
        
    def connectEventHandlers(self):
        '''
        Connects functions to event handlers
        '''
        pass


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