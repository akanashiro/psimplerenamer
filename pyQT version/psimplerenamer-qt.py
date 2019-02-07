#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QApplication, QListWidget,QVBoxLayout)
#from PyQt5.QtCore import QVBoxLayout
import sys

class SimpleRenamer(QWidget):
    
    def __init__(self):
        super().__init__()        
        self.initUI()
        
        
    def initUI(self):

# Lista de archivos
        listFiles = QListWidget(self)
        items = ['Item %s' % (i + 1) for i in range(4)]
        listFiles.addItems(items)
        listFiles.Height(100)
        listFiles.

# Botones de Agregar/Quitar
        btnAddFile = QPushButton('+', self)
        btnAddFile.setToolTip('Agregar archivos a la lista')
        btnAddFile.resize(20,20)
        btnAddFile.move(430, 20)    

        btnPullFile = QPushButton('-', self)
        btnPullFile.setToolTip('Quitararchivos a la lista')
        btnPullFile.resize(20,20)
        btnPullFile.move(430, 45)


# Texto
        lblText = QLabel("Cambiar el nombre por:", self)
        lblText.move(10,90)

        lnNombre = QLineEdit(self)
        lnNombre.insert('Nuevo Nombre#');
        lnNombre.move(150, 85)


# Secuencia
        self.lblTip = QLabel("Secuencia ascendente", self)
        self.lblTip.move(10,140)

        self.spinNumber = QSpinBox(self)
        self.spinNumber.move(140, 135)

        self.combo = QComboBox(self)
        self.combo.addItem("Inicio")
        self.combo.addItem("Fin")
        self.combo.move(200, 135)


# Botones
        self.btnRename = QPushButton('Renombrar', self)
#        btnRename.setToolTip('This is a <b>QPushButton</b> widget')
        self.btnRename.resize(self.btnRename.sizeHint())
        self.btnRename.move(50, 190)    

        self.btnClose = QPushButton('Cerrar', self)
        self.btnClose.clicked.connect(QApplication.instance().quit)
        self.btnClose.resize(self.btnClose.sizeHint())
        self.btnClose.move(150, 190)   

# Ventana Principal
        self.setGeometry(300, 300, 500, 270)
        self.setWindowTitle('Pretty Simple Renamer')
        self.show()
        
       
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = SimpleRenamer()
    sys.exit(app.exec_())
