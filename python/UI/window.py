# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 534)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 55, 55);\n"
"color: rgb(239,239,239);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 659, 460))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.optionsGroup = QGroupBox(self.scrollAreaWidgetContents)
        self.optionsGroup.setObjectName(u"optionsGroup")
        self.verticalLayout_5 = QVBoxLayout(self.optionsGroup)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.optionsGroup)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.matTypePrompt = QLabel(self.widget_2)
        self.matTypePrompt.setObjectName(u"matTypePrompt")

        self.horizontalLayout_2.addWidget(self.matTypePrompt)

        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.optionsGroup)

        self.mat1Group = QGroupBox(self.scrollAreaWidgetContents)
        self.mat1Group.setObjectName(u"mat1Group")
        self.mat1Group.setStyleSheet(u"")
        self.mat1Group.setFlat(False)
        self.mat1Group.setCheckable(False)
        self.horizontalLayout_4 = QHBoxLayout(self.mat1Group)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.mat1Group)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.matNameLbl = QLabel(self.widget)
        self.matNameLbl.setObjectName(u"matNameLbl")

        self.horizontalLayout_7.addWidget(self.matNameLbl)

        self.matNameTxt = QLineEdit(self.widget)
        self.matNameTxt.setObjectName(u"matNameTxt")

        self.horizontalLayout_7.addWidget(self.matNameTxt)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.baseColorLbl = QLabel(self.widget)
        self.baseColorLbl.setObjectName(u"baseColorLbl")

        self.horizontalLayout_6.addWidget(self.baseColorLbl)

        self.baseColorTxt = QLineEdit(self.widget)
        self.baseColorTxt.setObjectName(u"baseColorTxt")

        self.horizontalLayout_6.addWidget(self.baseColorTxt)

        self.baseColorBtn = QPushButton(self.widget)
        self.baseColorBtn.setObjectName(u"baseColorBtn")
        self.baseColorBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.horizontalLayout_6.addWidget(self.baseColorBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.roughnessLbl = QLabel(self.widget)
        self.roughnessLbl.setObjectName(u"roughnessLbl")

        self.horizontalLayout_8.addWidget(self.roughnessLbl)

        self.roughnessTxt = QLineEdit(self.widget)
        self.roughnessTxt.setObjectName(u"roughnessTxt")

        self.horizontalLayout_8.addWidget(self.roughnessTxt)

        self.roughnessBtn = QPushButton(self.widget)
        self.roughnessBtn.setObjectName(u"roughnessBtn")
        self.roughnessBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.horizontalLayout_8.addWidget(self.roughnessBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.metallicLbl = QLabel(self.widget)
        self.metallicLbl.setObjectName(u"metallicLbl")

        self.horizontalLayout_9.addWidget(self.metallicLbl)

        self.metallicTxt = QLineEdit(self.widget)
        self.metallicTxt.setObjectName(u"metallicTxt")

        self.horizontalLayout_9.addWidget(self.metallicTxt)

        self.metallicBtn = QPushButton(self.widget)
        self.metallicBtn.setObjectName(u"metallicBtn")
        self.metallicBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.horizontalLayout_9.addWidget(self.metallicBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.normalLbl = QLabel(self.widget)
        self.normalLbl.setObjectName(u"normalLbl")

        self.horizontalLayout_10.addWidget(self.normalLbl)

        self.normalTxt = QLineEdit(self.widget)
        self.normalTxt.setObjectName(u"normalTxt")

        self.horizontalLayout_10.addWidget(self.normalTxt)

        self.normalBtn = QPushButton(self.widget)
        self.normalBtn.setObjectName(u"normalBtn")
        self.normalBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.horizontalLayout_10.addWidget(self.normalBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.heightLbl = QLabel(self.widget)
        self.heightLbl.setObjectName(u"heightLbl")

        self.horizontalLayout_11.addWidget(self.heightLbl)

        self.heightTxt = QLineEdit(self.widget)
        self.heightTxt.setObjectName(u"heightTxt")

        self.horizontalLayout_11.addWidget(self.heightTxt)

        self.heightBtn = QPushButton(self.widget)
        self.heightBtn.setObjectName(u"heightBtn")
        self.heightBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.horizontalLayout_11.addWidget(self.heightBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.browseAllBtn = QPushButton(self.widget)
        self.browseAllBtn.setObjectName(u"browseAllBtn")
        self.browseAllBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.verticalLayout_4.addWidget(self.browseAllBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.objPromptLbl = QLabel(self.widget)
        self.objPromptLbl.setObjectName(u"objPromptLbl")
        self.objPromptLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.objPromptLbl)

        self.objList = QListWidget(self.widget)
        self.objList.setObjectName(u"objList")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objList.sizePolicy().hasHeightForWidth())
        self.objList.setSizePolicy(sizePolicy)
        self.objList.setMaximumSize(QSize(150, 16777215))
        self.objList.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"")
        self.objList.setFrameShape(QFrame.Box)

        self.verticalLayout_6.addWidget(self.objList)

        self.addObjBtn = QPushButton(self.widget)
        self.addObjBtn.setObjectName(u"addObjBtn")
        self.addObjBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.verticalLayout_6.addWidget(self.addObjBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.mat1Group)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.submitNewBtn = QPushButton(self.scrollAreaWidgetContents)
        self.submitNewBtn.setObjectName(u"submitNewBtn")
        self.submitNewBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.horizontalLayout.addWidget(self.submitNewBtn)

        self.submitExistBtn = QPushButton(self.scrollAreaWidgetContents)
        self.submitExistBtn.setObjectName(u"submitExistBtn")
        self.submitExistBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.horizontalLayout.addWidget(self.submitExistBtn)

        self.addMatBtn = QPushButton(self.scrollAreaWidgetContents)
        self.addMatBtn.setObjectName(u"addMatBtn")
        self.addMatBtn.setStyleSheet(u"background-color: rgb(93, 93, 93);")

        self.horizontalLayout.addWidget(self.addMatBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 704, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Maya USD Substance Import", None))
        self.optionsGroup.setTitle(QCoreApplication.translate("MainWindow", u"General Options", None))
        self.matTypePrompt.setText(QCoreApplication.translate("MainWindow", u"Select USD Compatible Material Type:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"USDPreviewSurface", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MaterialX", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Arnold Standard Surface", None))

        self.mat1Group.setTitle(QCoreApplication.translate("MainWindow", u"Material 1", None))
        self.matNameLbl.setText(QCoreApplication.translate("MainWindow", u"Material Name:", None))
        self.baseColorLbl.setText(QCoreApplication.translate("MainWindow", u"Base Color:", None))
        self.baseColorBtn.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.roughnessLbl.setText(QCoreApplication.translate("MainWindow", u"Roughness:", None))
        self.roughnessBtn.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.metallicLbl.setText(QCoreApplication.translate("MainWindow", u"Metallic:", None))
        self.metallicBtn.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.normalLbl.setText(QCoreApplication.translate("MainWindow", u"Normal:", None))
        self.normalBtn.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.heightLbl.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.heightBtn.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.browseAllBtn.setText(QCoreApplication.translate("MainWindow", u"Browse All", None))
        self.objPromptLbl.setText(QCoreApplication.translate("MainWindow", u"Objects To \n"
"Receive Material", None))
        self.addObjBtn.setText(QCoreApplication.translate("MainWindow", u"Add Selected Object", None))
        self.submitNewBtn.setText(QCoreApplication.translate("MainWindow", u"Save to New Layer", None))
        self.submitExistBtn.setText(QCoreApplication.translate("MainWindow", u"Save to Active Layer", None))
        self.addMatBtn.setText(QCoreApplication.translate("MainWindow", u"Add Material", None))
    # retranslateUi

