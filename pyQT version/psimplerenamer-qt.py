# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psimplerenamer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import os
import urllib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QApplication, QFileDialog, QGridLayout ,QHeaderView)
from PyQt5.QtCore import QDir, QUrl, QFileInfo
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)         # Create QGridLayout
        #self.centralwidget.setLayout(self.grid_layout)   # Set this layout in central widget        
        
        # Nuevo Nombre
        self.nuevoNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.nuevoNombre.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.nuevoNombre.setObjectName("nuevoNombre")
        
        
        self.explicacion = QtWidgets.QLabel(self.centralwidget)
        self.explicacion.setGeometry(QtCore.QRect(30, 40, 211, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.explicacion.setFont(font)
        self.explicacion.setObjectName("explicacion")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 300, 83, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 310, 21, 18))
        self.label_2.setObjectName("label_2")
        
        # Boton Quitar Archivos        
        self.btnPullFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnPullFile.setGeometry(QtCore.QRect(550, 100, 31, 34))
        self.btnPullFile.setObjectName("btnPullFile")
        
        # Boton Agregar Archivos        
        self.btnPushFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnPushFile.setGeometry(QtCore.QRect(550, 60, 31, 34))
        self.btnPushFile.setObjectName("btnPushFile")
        
        
        self.btnRename = QtWidgets.QPushButton(self.centralwidget)
        self.btnRename.setGeometry(QtCore.QRect(221, 361, 85, 34))
        self.btnRename.setObjectName("btnRename")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 310, 131, 18))
        self.label.setObjectName("label")

        # Boton Cerrar        
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(312, 361, 84, 34))
        self.btnClose.setObjectName("btnClose")

        # Tabla de archivos        
        self.listaArchivos = QtWidgets.QTableWidget(self.centralwidget)
        self.listaArchivos.setGeometry(QtCore.QRect(30, 60, 500, 191))
        self.listaArchivos.setGridStyle(QtCore.Qt.DotLine)
        self.listaArchivos.setWordWrap(True)
        self.listaArchivos.setCornerButtonEnabled(True)
        self.listaArchivos.setRowCount(5)
        self.listaArchivos.setColumnCount(3)
        self.listaArchivos.setObjectName("listaArchivos")
        
        
        # Columna Ruta        
        item = QtWidgets.QTableWidgetItem()
        self.listaArchivos.setHorizontalHeaderItem(0, item)
        self.listaArchivos.setColumnWidth(0,110)
        #self.listaArchivos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
             
        # Columna Archivo
        item = QtWidgets.QTableWidgetItem()
        self.listaArchivos.setHorizontalHeaderItem(1, item)
        #self.listaArchivos.setColumnWidth(1,120)
        self.listaArchivos.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
        # Columna Resultado
        item = QtWidgets.QTableWidgetItem()
        self.listaArchivos.setHorizontalHeaderItem(2, item)
        #self.listaArchivos.setColumnWidth(2,120)
        self.listaArchivos.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        
        self.listaArchivos.verticalHeader().setVisible(False)
        
        # Secuencia
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(150, 300, 51, 32))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pretty Simple File Renamer"))
        self.nuevoNombre.setText(_translate("MainWindow", "NuevoNombre"))
        self.explicacion.setText(_translate("MainWindow", "Elija los archivos a renombrar"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Inicio"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Fin"))
        self.label_2.setText(_translate("MainWindow", "al"))
        self.btnPullFile.setText(_translate("MainWindow", "-"))
        self.btnPushFile.setText(_translate("MainWindow", "+"))
        self.btnRename.setText(_translate("MainWindow", "Renombrar"))
        self.label.setText(_translate("MainWindow", "Inicio de secuencia"))
        self.btnClose.setText(_translate("MainWindow", "Cerrar"))
        
        item = self.listaArchivos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ruta"))
        item = self.listaArchivos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre Original"))
        item = self.listaArchivos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre Final"))
        
        # Do the resize of the columns by content
        #self.listaArchivos.resizeColumnsToContents()        
        #self.grid_layout.addWidget(self.listaArchivos, 0, 0)   # Adding the table to the grid
        

class SimpleRenamer(QtWidgets.QMainWindow):
    def __init__(self):
        super(SimpleRenamer, self).__init__()        
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)        
        self.ui.btnClose.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.ui.btnPushFile.clicked.connect(self.abrirDialogo)

    def abrirDialogo(self):
        self.openFileNamesDialog()

    def openFileNamesDialog(self):
        
        global intRow
        global intSequence
        
        if intSequence == 0:
            intSequence = self.ui.spinBox.value()
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog        
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        
        if files:
#            print(files)
            for filename in files:
#                filename = os.path.normpath(filename)
                srcFile = filename.split("/")[-1]             
                srcFolder = filename.split(srcFile,1)[0]
                
#                srcFolder = filename.directory() + "/"
#                srcFile = filename.split(srcFolder,1)            
                #print ("Ruta " + srcFolder[0])
                print ("Archivo " + srcFile)
                print ("Ruta" + srcFolder)
                
                itemFolder = QtWidgets.QTableWidgetItem()
                itemSourceFile = QtWidgets.QTableWidgetItem()
                itemFolder.setText(srcFolder)
                self.ui.listaArchivos.setItem(intRow, 0, itemFolder)
                itemSourceFile.setText(srcFile)
                self.ui.listaArchivos.setItem(intRow, 1, itemSourceFile)

                strExtension = srcFile.split('.',1)
                strRenamedFile = self.ui.nuevoNombre.text()                
                if len(strExtension) < 2:
                    strDestFile = strRenamedFile + str(intSequence)
                else:
                    strDestFile = strRenamedFile + str(intSequence) + '.' + strExtension[1]
                    
                itemDestFile = QtWidgets.QTableWidgetItem()
                itemDestFile.setText(strDestFile)
                self.ui.listaArchivos.setItem(intRow, 2, itemDestFile)
                
                intRow += 1
                intSequence += 1
                            
intRow = 0
intSequence = 0

if __name__ == '__main__':
    intRow = 0
    app = QtWidgets.QApplication(sys.argv)    
    ex = SimpleRenamer()
    
    ex.show()
    sys.exit(app.exec())
