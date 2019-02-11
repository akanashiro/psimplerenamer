#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'psimplerenamer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import os
import urllib
import sys

from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
#from PyQt5.QtCore import QDir, QUrl, QFileInfo
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QApplication, QFileDialog, QGridLayout , QHeaderView, QHBoxLayout, QVBoxLayout, QDesktopWidget)




class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(Qt.WindowMaximizeButtonHint|Qt.WindowCloseButtonHint)
        MainWindow.setFixedSize(750,400)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        
        #self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)         # Create QGridLayout
        #self.centralwidget.setLayout(self.grid_layout)   # Set this layout in central widget        
    
               
        # Definición de Tabla de Archivos
        self.listaArchivos = QtWidgets.QTableWidget(self.centralwidget)
        self.listaArchivos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #self.listaArchivos.setGeometry(QtCore.QRect(30, 60, 500, 191))
        self.listaArchivos.setMaximumSize(QtCore.QSize(700, 16777215))
        self.listaArchivos.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        #self.listaArchivos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listaArchivos.setGridStyle(QtCore.Qt.DotLine)
        self.listaArchivos.setWordWrap(True)
        self.listaArchivos.setCornerButtonEnabled(True)
        #self.listaArchivos.setRowCount(7)
        self.listaArchivos.setColumnCount(3)
        self.listaArchivos.setObjectName("listaArchivos")
        self.listaArchivos.setMouseTracking(True)
        
       
        # Columna Ruta Resumida
        item = QtWidgets.QTableWidgetItem()
        self.listaArchivos.setHorizontalHeaderItem(0, item)
        self.listaArchivos.setColumnWidth(0,110)
        
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

        # Columna Ruta        
        # item = QtWidgets.QTableWidgetItem()
        # self.listaArchivos.setHorizontalHeaderItem(3, item)
        # self.listaArchivos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

       # Botón Agregar Archivos        
        self.btnPushFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        #self.btnPushFile.setGeometry(QtCore.QRect(550, 60, 31, 34))
        self.btnPushFile.setObjectName("btnPushFile")
        self.btnPushFile.setMaximumWidth(34)
        self.btnPushFile.setIcon(QtGui.QIcon("icons/list-add.svg"))
        self.btnPushFile.setToolTip("Agregar archivos") 

        # Boton Quitar Archivos        
        self.btnPullFile = QtWidgets.QPushButton(self.centralwidget)
        #self.btnPullFile.setGeometry(QtCore.QRect(550, 100, 31, 34))
        self.btnPullFile.setObjectName("btnPullFile")
        self.btnPullFile.setMaximumWidth(34)
        self.btnPullFile.setIcon(QtGui.QIcon("icons/list-remove.svg"))
        self.btnPullFile.setToolTip("Quitar el/los archivo(s) seleccionado(s)")
        
        # Botón Subir
        self.btnMoveUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnMoveUp.setObjectName("btnMoveUp")
        self.btnMoveUp.setMaximumWidth(34)    
        self.btnMoveUp.setIcon(QtGui.QIcon("icons/go-up.svg"))
        self.btnMoveUp.setToolTip("Subir el/los archivo(s) seleccionado(s)")
        
        # Botón Bajar
        self.btnMoveDown = QtWidgets.QPushButton(self.centralwidget)
        self.btnMoveDown.setObjectName("btnMoveDown")
        self.btnMoveDown.setMaximumWidth(34)        
        self.btnMoveDown.setIcon(QtGui.QIcon("icons/go-down.svg"))
        self.btnMoveDown.setToolTip("Bajar el/los archivo(s) seleccionado(s)")        

        # Botón Limpiar
        self.btnClean = QtWidgets.QPushButton(self.centralwidget)
        self.btnClean.setObjectName("btnClean")
        self.btnClean.setMaximumWidth(34)        
        self.btnClean.setIcon(QtGui.QIcon("icons/edit-delete.svg"))
        self.btnClean.setToolTip("Eliminar todos")     
        
        # Nuevo Nombre
        self.nuevoNombre = QtWidgets.QLineEdit(self.centralwidget)
        #self.nuevoNombre.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.nuevoNombre.setObjectName("nuevoNombre")
        self.nuevoNombre.setToolTip("Cambiará el nombre de los archivos por el que escriba aquí")
        self.nuevoNombre.setText("NuevoNombre")              


        # Etiqueta "Insertar"
        self.labelInsert = QtWidgets.QLabel(self.centralwidget)
        #self.labelInsert.setGeometry(QtCore.QRect(30, 310, 131, 18))
        self.labelInsert.setObjectName("labelInsert")
        self.labelInsert.setText("Insertar")       
                
        # Spinbox Secuencia
        self.spinSequence = QtWidgets.QSpinBox(self.centralwidget)
        #self.spinSequence.setGeometry(QtCore.QRect(150, 300, 51, 32))
        self.spinSequence.setMinimum(1)
        self.spinSequence.setMaximum(100)
        self.spinSequence.setObjectName("spinSequence")
        self.spinSequence.setToolTip("La secuencia comenzará a partir del número que ingrese")

        # ComboBox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        #self.comboBox.setGeometry(QtCore.QRect(230, 300, 83, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Inicio", "S")
        self.comboBox.addItem("Fin", "E")
        self.comboBox.setCurrentIndex(1)

        # Botón Renombrar
        self.btnRename = QtWidgets.QPushButton(self.centralwidget)
        #self.btnRename.setGeometry(QtCore.QRect(221, 361, 85, 34))
        self.btnRename.setObjectName("btnRename")
        self.btnRename.setText("Aplicar")

        # Boton Cerrar        
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        #self.btnClose.setGeometry(QtCore.QRect(312, 361, 84, 34))
        self.btnClose.setObjectName("btnClose")                
        self.btnClose.setText("Cerrar")
        # self.btnClose.clicked.connect(QtWidgets.QApplication.instance().quit)                

#================       LAYOUT       ================

        # Layout arriba izquierda
        hboxTopLeft = QHBoxLayout()
        hboxTopLeft.setObjectName("hboxTopLeft")
        hboxTopLeft.addWidget(self.listaArchivos)
        
        # Layout arriba derecha
        vboxTopRight = QVBoxLayout()
        vboxTopRight.setAlignment(Qt.AlignTop)
        vboxTopRight.setContentsMargins(0, -1, -1, 10)
        vboxTopRight.addWidget(self.btnPushFile)
        vboxTopRight.addWidget(self.btnPullFile)
        vboxTopRight.addWidget(self.btnMoveUp)
        vboxTopRight.addWidget(self.btnMoveDown)
        vboxTopRight.addWidget(self.btnClean)
        
        # Layout que contiene los dos layouts Top
        vboxFirst = QHBoxLayout()
        vboxFirst.addLayout(hboxTopLeft)
        vboxFirst.addLayout(vboxTopRight)


        # Layout horizontal del medio
        hboxMiddle = QHBoxLayout()
        hboxMiddle.addWidget(self.nuevoNombre)
        

        # Layout fondo izquierda 
        hboxBottomLeft =  QHBoxLayout()
        #hboxBottomLeft.addStretch(1)
        #hboxBottomLeft.setAlignment(Qt.AlignLeft)
        #hboxBottomLeft.setAlignment(Qt.AlignTop)
        hboxBottomLeft.addWidget(self.labelInsert)
        hboxBottomLeft.addWidget(self.spinSequence)
        hboxBottomLeft.addWidget(self.comboBox)
        
        vboxLeft = QVBoxLayout()
        vboxLeft.addStretch(1)
        #vboxLeft.setAlignment(Qt.AlignLeft)
        vboxLeft.addLayout(hboxBottomLeft)

        # Layout fondo derecha
        hboxBottomRight = QHBoxLayout()
        hboxBottomRight.addStretch(1)
        #hboxBottomRight.setAlignment(Qt.AlignTop)
        hboxBottomRight.addWidget(self.btnRename)
        hboxBottomRight.addWidget(self.btnClose)
  
               
        vboxRight = QVBoxLayout()
        vboxRight.addStretch(1)
        vboxRight.addLayout(hboxBottomRight)

    
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 700, 250))
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout1.addLayout(vboxFirst,0,0)
        #self.gridLayout1.addLayout(vboxTopRight,0,1)        

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 285, 700, 85))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")   

        
        self.gridLayout.addLayout(hboxMiddle,1,0)
        self.gridLayout.addLayout(vboxLeft, 2, 0)
        self.gridLayout.addLayout(vboxRight, 2, 1)
           
        
        MainWindow.setCentralWidget(self.centralwidget)
#        self.statusbar = QtWidgets.QStatusBar(MainWindow)
#        self.statusbar.setObjectName("statusbar")
#        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Etiquetas de los objetos
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pretty Simple File Renamer"))
        #self.nuevoNombre.setText(_translate("MainWindow", "NuevoNombre"))
                
        # Texto de las columnas de la tabla de Archivos
        item = self.listaArchivos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ruta"))
        
        item = self.listaArchivos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.listaArchivos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nuevo Nombre"))
        
     #   item = self.listaArchivos.horizontalHeaderItem(3)
      #  item.setText(_translate("MainWindow", "Ruta"))
        
        
        # Do the resize of the columns by content
        #self.listaArchivos.resizeColumnsToContents()        
        #self.grid_layout.addWidget(self.listaArchivos, 0, 0)   # Adding the table to the grid        

class SimpleRenamer(QtWidgets.QMainWindow):
    def __init__(self):
        super(SimpleRenamer, self).__init__()        
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        
        # Eventos de botones

        self.ui.btnPushFile.clicked.connect(self.callOpenDialog)
        self.ui.btnPullFile.clicked.connect(self.removeFiles)
        self.ui.spinSequence.valueChanged.connect(self.synchNumbers)
        self.ui.comboBox.currentIndexChanged.connect(self.synchNumbers)
        self.ui.nuevoNombre.textChanged.connect(self.synchNumbers)
        self.ui.btnMoveUp.clicked.connect(self.moveUp)
        self.ui.btnMoveDown.clicked.connect(self.moveDown)
        self.ui.btnClean.clicked.connect(self.cleanList)
        self.ui.btnRename.clicked.connect(self.applyRenaming)
        self.ui.btnClose.clicked.connect(QtWidgets.QApplication.instance().quit)
        
    # Lógica para renombrar los archivos según los parámetros elegidos en pantalla
    def renameFiles(self, inSrcFile, inSequence):
    
        global strPosition
                
        strExtension = inSrcFile.split('.',1)
        strRenamedFile = self.ui.nuevoNombre.text()   

        # Obtiene la posición
        strPosition = self.ui.comboBox.currentData()         
        
        if len(strExtension) < 2:
            if strPosition == "S":
                outDestFile = str(inSequence) + "_" + strRenamedFile
            else:
                outDestFile = strRenamedFile + "_" + str(inSequence)
        else:
            if strPosition == "S":
                outDestFile = str(inSequence) + "_" + strRenamedFile + '.' + strExtension[1]
            else:
                outDestFile = strRenamedFile + "_" + str(inSequence) + '.' + strExtension[1]
          
        return outDestFile

    # Re-sincroniza los archivos a partir de los cambios hechos: secuencia, posición, nombre
    def synchNumbers(self):
    
        #global intSequence
        # Obtiene secuencia nueva
        intResynch = self.ui.spinSequence.value()
    
        # Recorre la tabla de archivos
        for nbrIndex in range(self.ui.listaArchivos.rowCount()):
            srcFile = self.ui.listaArchivos.item(nbrIndex,1)

            # debug print ("source"+ srcFile.text())
            # Función de renombrado de archivos
            strDestFile = self.renameFiles(srcFile.text(), intResynch)
            itemDestFile = QtWidgets.QTableWidgetItem()
            itemDestFile.setText(strDestFile)            
            self.ui.listaArchivos.setItem(nbrIndex,2, itemDestFile)

            nbrIndex += 1
            intResynch += 1

    # Mueve los archivos elegidos
    def moveFiles(self, direction):
        
            indexes = self.ui.listaArchivos.selectionModel().selectedRows()
            
            if not indexes:
                return
                 
            if direction == "UP":
                for index in sorted(indexes):
                    intRow = index.row()
                    print('Row %d is selected' % intRow)                     
                    if intRow > 0:
                        self.ui.listaArchivos.insertRow(intRow - 1)
                        for i in range(self.ui.listaArchivos.columnCount()):
                            self.ui.listaArchivos.setItem(intRow - 1,i,self.ui.listaArchivos.takeItem(intRow + 1,i))
                            #self.ui.listaArchivos.setCurrentCell(index.row()-1,column)          
                        self.ui.listaArchivos.removeRow(intRow + 1)
                        
                        # Mueve el foco a la fila movida 
                        newIndex = self.ui.listaArchivos.selectionModel().model().index(intRow - 1,0)
                        self.ui.listaArchivos.selectionModel().select(newIndex,QItemSelectionModel.Select)
                        self.ui.listaArchivos.setCurrentIndex(newIndex)
            else:
                for index in sorted(indexes, reverse=True):
                    intRow = index.row()
                    print('Row %d is selected' % intRow)     
                    if intRow < int(self.ui.listaArchivos.rowCount()-1):
                        self.ui.listaArchivos.insertRow(intRow + 2)
                        for i in range(self.ui.listaArchivos.columnCount()):
                            self.ui.listaArchivos.setItem(intRow + 2, i,self.ui.listaArchivos.takeItem(intRow,i))
                            #self.ui.listaArchivos.setCurrentCell(intRow + 2,column)
                        self.ui.listaArchivos.removeRow(intRow)
                        
                        # Mueve el foco a la fila movida 
                        newIndex = self.ui.listaArchivos.selectionModel().model().index(intRow + 1,0)
                        self.ui.listaArchivos.selectionModel().select(newIndex,QItemSelectionModel.Select)
                        self.ui.listaArchivos.setCurrentIndex(newIndex)
                
                self.ui.listaArchivos.setFocus()
        
    # Mover arriba
    def moveUp(self):
        self.moveFiles("UP")
        self.synchNumbers()

    # Mover abajo
    def moveDown(self):
        self.moveFiles("DOWN")
        self.synchNumbers()
        
    # Quitar archivos
    def removeFiles(self):
        global intSequence
        indexes = self.ui.listaArchivos.selectionModel().selectedRows()
        for index in sorted(indexes):
            self.ui.listaArchivos.removeRow(index.row())
        self.synchNumbers()
        intSequence = intSequence - 1
 
    # Limpia la tabla
    def cleanList(self):
        global intSequence        
        self.ui.listaArchivos.selectionModel().model().removeRows(0, self.ui.listaArchivos.rowCount())
        intSequence = self.ui.spinSequence.value()
        
    # Renombra físicamente los archivos
    def applyRenaming(self):
        
        print ("Renombrado de archivos")
        # Recorre la tabla de archivos
        for nbrIndex in range(self.ui.listaArchivos.rowCount()):
            srcFolder = self.ui.listaArchivos.item(nbrIndex,0).toolTip()
            srcFile = self.ui.listaArchivos.item(nbrIndex,1)
            dstFile = self.ui.listaArchivos.item(nbrIndex,2)
        
            src = srcFolder + srcFile.text()
            dst = srcFolder + dstFile.text()
            
            print (src + " >>> " + dst)

            os.rename(src,dst)
        print ("Renombrado finalizado")
        self.cleanList()

    def itemAlreadyExists(self, inSrcFile):
        
        itemList = self.ui.listaArchivos.findItems(inSrcFile, QtCore.Qt.MatchExactly)
        if len(itemList) > 0:
            return True
        else:
            return False

    def callOpenDialog(self):
        self.openFileNamesDialog()

    def openFileNamesDialog(self):
        
        global intSequence
        global strPosition
        
        # Obtiene la secuencia
        if intSequence == 0:
            intSequence = self.ui.spinSequence.value()
        
        # Obtiene la posición
        strPosition = self.ui.comboBox.currentData() 
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog        
        files, _ = QFileDialog.getOpenFileNames(self,"Agregar archivos", "","All Files (*);;Python Files (*.py)", options=options)
        
        if files:

            for filename in files:
#                filename = os.path.normpath(filename)
                srcFile = filename.split("/")[-1]             
                srcFolder = filename.split(srcFile,1)[0]
                lenSplit = len(srcFolder.split("/")) - 2
                srcFolderSplit = "../" + srcFolder.split("/")[lenSplit] + "/" 
                
                       
#                srcFolder = filename.directory() + "/"
#                srcFile = filename.split(srcFolder,1)            
                # debug print ("File " + srcFile)
                # debug print ("Path " + srcFolder)
                
                if self.itemAlreadyExists(srcFile) == False:
                    
                    intRow = int(self.ui.listaArchivos.rowCount())
                    
                    itemFolderSplit = QtWidgets.QTableWidgetItem()
                    itemFolderSplit.setText(srcFolderSplit)
                    itemFolderSplit.setToolTip(srcFolder)
                    
                    #itemFolder = QtWidgets.QTableWidgetItem()
                    #itemFolder.setText(srcFolder)
                    
                    self.ui.listaArchivos.insertRow(intRow)
                    self.ui.listaArchivos.setItem(intRow, 0, itemFolderSplit)
                    # self.ui.listaArchivos.setItem(intRow, 3, itemFolder)
                    
                    itemSourceFile = QtWidgets.QTableWidgetItem()                    
                    itemSourceFile.setText(srcFile)
                    self.ui.listaArchivos.setItem(intRow, 1, itemSourceFile)

                    # Función de renombrado de archivos
                    strDestFile = self.renameFiles(srcFile, intSequence)

                    itemDestFile = QtWidgets.QTableWidgetItem()
                    itemDestFile.setText(strDestFile)
                    self.ui.listaArchivos.setItem(intRow, 2, itemDestFile)
                    
                intSequence += 1

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = ag.height() - sg.height() - widget.height()
        self.move(x, y)

                            
intSequence = 0
strPosition =""

if __name__ == '__main__':
    intRow = 0
    app = QtWidgets.QApplication(sys.argv)    
    ex = SimpleRenamer()
    ex.show()
    sys.exit(app.exec())
