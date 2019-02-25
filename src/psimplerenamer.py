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
import time

from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
# from PyQt5.QtCore import QDir, QUrl, QFileInfo
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QCheckBox,
                             QApplication, QFileDialog, QGridLayout, QHeaderView, QHBoxLayout, QVBoxLayout, QDesktopWidget)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        MainWindow.setFixedSize(750, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)

        # File Table Definition
        self.listFiles = QtWidgets.QTableWidget(self.centralwidget)
        self.listFiles.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listFiles.setMaximumSize(QtCore.QSize(700, 16777215))
        self.listFiles.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.listFiles.setGridStyle(QtCore.Qt.DotLine)
        self.listFiles.setWordWrap(True)
        self.listFiles.setCornerButtonEnabled(True)
        self.listFiles.setColumnCount(3)
        self.listFiles.setObjectName("listFiles")
        self.listFiles.setMouseTracking(True)

        # "Simplified Path" Column
        item = QtWidgets.QTableWidgetItem()
        self.listFiles.setHorizontalHeaderItem(0, item)
        self.listFiles.setColumnWidth(0, 110)

        # "Original Name" Column
        item = QtWidgets.QTableWidgetItem()
        self.listFiles.setHorizontalHeaderItem(1, item)
        # self.listFiles.setColumnWidth(1,120)
        self.listFiles.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        # "New Name" Column
        item = QtWidgets.QTableWidgetItem()
        self.listFiles.setHorizontalHeaderItem(2, item)
        # self.listFiles.setColumnWidth(2,120)
        self.listFiles.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.listFiles.verticalHeader().setVisible(False)

        # Columna Ruta
        # item = QtWidgets.QTableWidgetItem()
        # self.listFiles.setHorizontalHeaderItem(3, item)
        # self.listFiles.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # "Add Files" Button
        self.btnPushFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnPushFile.setObjectName("btnPushFile")
        self.btnPushFile.setMaximumWidth(34)
        self.btnPushFile.setIcon(QtGui.QIcon(os.path.join(dirname, "icons/list-add.svg")))
        self.btnPushFile.setToolTip("Add files")

        # "Remove Files" Button
        self.btnPullFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnPullFile.setObjectName("btnPullFile")
        self.btnPullFile.setMaximumWidth(34)
        self.btnPullFile.setIcon(QtGui.QIcon(os.path.join(dirname, "icons/list-remove.svg")))
        self.btnPullFile.setToolTip("Remove seleted file(s)")

        # "Move Up" Button
        self.btnMoveUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnMoveUp.setObjectName("btnMoveUp")
        self.btnMoveUp.setMaximumWidth(34)
        self.btnMoveUp.setIcon(QtGui.QIcon(os.path.join(dirname, "icons/go-up.svg")))
        self.btnMoveUp.setToolTip("Move up selected file(s)")

        # "Move Down" Button
        self.btnMoveDown = QtWidgets.QPushButton(self.centralwidget)
        self.btnMoveDown.setObjectName("btnMoveDown")
        self.btnMoveDown.setMaximumWidth(34)
        self.btnMoveDown.setIcon(QtGui.QIcon(os.path.join(dirname, "icons/go-down.svg")))
        self.btnMoveDown.setToolTip("Move down selected file(s)")

        # "Clear all" Button
        self.btnClean = QtWidgets.QPushButton(self.centralwidget)
        self.btnClean.setObjectName("btnClean")
        self.btnClean.setMaximumWidth(34)
        self.btnClean.setIcon(QtGui.QIcon(os.path.join(dirname, "icons/edit-delete.svg")))
        self.btnClean.setToolTip("Clear all")

        # "New name" Label
        self.nuevoNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.nuevoNombre.setObjectName("nuevoNombre")
        self.nuevoNombre.setToolTip("This text will replace your original file name")
        self.nuevoNombre.setText("New_Name")

        # "Insert" Label
        self.labelInsert = QtWidgets.QLabel(self.centralwidget)
        self.labelInsert.setObjectName("labelInsert")
        self.labelInsert.setText("Insert")

        # Number Sequence Spinbox
        self.spinSequence = QtWidgets.QSpinBox(self.centralwidget)
        self.spinSequence.setMinimum(1)
        self.spinSequence.setMaximum(100)
        self.spinSequence.setObjectName("spinSequence")
        self.spinSequence.setToolTip("Sequence will start from this number")

        # "Start/End" Combo box
        self.comboStartEnd = QtWidgets.QComboBox(self.centralwidget)
        self.comboStartEnd.setObjectName("comboStartEnd")
        self.comboStartEnd.addItem("Start", "S")
        self.comboStartEnd.addItem("End", "E")
        self.comboStartEnd.setCurrentIndex(1)

        # "Uppercase" Combo box
        self.comboCase = QtWidgets.QComboBox(self.centralwidget)
        self.comboCase.setObjectName("comboCase")
        self.comboCase.addItem("Preserve case", "N")
        self.comboCase.addItem("UPPERCASE", "U")
        self.comboCase.addItem("lowercase", "L")
        self.comboCase.setCurrentIndex(0)

        # "Add date" checkbox
        self.checkAddDt = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAddDt.setObjectName("checkAddDate")
        self.checkAddDt.setText("Add Date")

        # Rename Button
        self.btnRename = QtWidgets.QPushButton(self.centralwidget)
        self.btnRename.setObjectName("btnRename")
        self.btnRename.setText("Apply")

        # Close Button
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setObjectName("btnClose")
        self.btnClose.setText("Close")


# ================       LAYOUT       ================

        # Upper left layout
        hboxTopLeft = QHBoxLayout()
        hboxTopLeft.setObjectName("hboxTopLeft")
        hboxTopLeft.addWidget(self.listFiles)

        # Upper right layout
        vboxTopRight = QVBoxLayout()
        vboxTopRight.setAlignment(Qt.AlignTop)
        vboxTopRight.setContentsMargins(0, -1, -1, 10)
        vboxTopRight.addWidget(self.btnPushFile)
        vboxTopRight.addWidget(self.btnPullFile)
        vboxTopRight.addWidget(self.btnMoveUp)
        vboxTopRight.addWidget(self.btnMoveDown)
        vboxTopRight.addWidget(self.btnClean)

        # Layout that contains top layout boxes
        vboxFirst = QHBoxLayout()
        vboxFirst.addLayout(hboxTopLeft)
        vboxFirst.addLayout(vboxTopRight)

        # Middle layout
        hboxMiddle = QHBoxLayout()
        hboxMiddle.addWidget(self.nuevoNombre)
        hboxMiddle.addWidget(self.comboCase)
        hboxMiddle.addWidget(self.checkAddDt)

        # Spin sequence layout
        hboxSpinSequence = QHBoxLayout()
        hboxSpinSequence.addWidget(self.labelInsert)
        hboxSpinSequence.addWidget(self.spinSequence)
        hboxSpinSequence.addWidget(self.comboStartEnd)

        vboxLeft = QVBoxLayout()
        vboxLeft.addStretch(1)
        vboxLeft.addLayout(hboxSpinSequence)

        # Bottom right layout
        hboxBottomRight = QHBoxLayout()
        hboxBottomRight.addStretch(1)
        hboxBottomRight.addWidget(self.btnRename)
        hboxBottomRight.addWidget(self.btnClose)

        vboxRight = QVBoxLayout()
        vboxRight.addStretch(1)
        vboxRight.addLayout(hboxBottomRight)

        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 700, 250))
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout1.addLayout(vboxFirst, 0, 0)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 285, 700, 85))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.gridLayout.addLayout(hboxMiddle, 1, 0)
        self.gridLayout.addLayout(vboxLeft, 2, 0)
        self.gridLayout.addLayout(vboxRight, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Object labels
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pretty Simple File Renamer"))

        # Table's column texts
        item = self.listFiles.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Path"))

        item = self.listFiles.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.listFiles.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Name"))


class SimpleRenamer(QtWidgets.QMainWindow):
    def __init__(self):
        super(SimpleRenamer, self).__init__()
        self.ui = Ui_MainWindow()
        self.setWindowIcon(QtGui.QIcon(os.path.join(dirname, "icons/application.svg")))
        self.ui.setupUi(self)

        # Buttons events
        self.ui.btnPushFile.clicked.connect(self.callOpenDialog)
        self.ui.btnPullFile.clicked.connect(self.removeFiles)
        self.ui.spinSequence.valueChanged.connect(self.synchNumbers)
        self.ui.comboCase.currentIndexChanged.connect(self.synchNumbers)
        self.ui.comboStartEnd.currentIndexChanged.connect(self.synchNumbers)
        self.ui.nuevoNombre.textChanged.connect(self.synchNumbers)
        self.ui.checkAddDt.stateChanged.connect(self.synchNumbers)
        self.ui.btnMoveUp.clicked.connect(self.moveUp)
        self.ui.btnMoveDown.clicked.connect(self.moveDown)
        self.ui.btnClean.clicked.connect(self.cleanList)
        self.ui.btnRename.clicked.connect(self.applyRenaming)
        self.ui.btnClose.clicked.connect(QtWidgets.QApplication.instance().quit)

    # Rename files logic considering input parameters
    def renameFiles(self, inSrcFile, inSequence):

        global strPosition

        strExtension = inSrcFile.split('.', 1)
        strRenamedFile = self.ui.nuevoNombre.text()

        # Case
        strCase = self.ui.comboCase.currentData()

        if strCase == "U": # uppercase
            strRenamedFile = strRenamedFile.upper()
        elif strCase == "L":
            strRenamedFile = strRenamedFile.lower()
            pass

        # Date
        if self.ui.checkAddDt.isChecked() == True:
            dtToday = time.strftime('%Y%m%d')
            strRenamedFile = strRenamedFile + "_" + dtToday

        # Get position
        strPosition = self.ui.comboStartEnd.currentData()

        if inSequence < 10:
            strSequence = "0" + str(inSequence)
        else:
            strSequence = str(inSequence)

        if len(strExtension) < 2:
            if strPosition == "S":
                outDestFile = strSequence + "_" + strRenamedFile
            else:
                outDestFile = strRenamedFile + "_" + strSequence
        else:
            if strPosition == "S":
                outDestFile = strSequence + "_" + strRenamedFile + '.' + strExtension[1]
            else:
                outDestFile = strRenamedFile + "_" + strSequence + '.' + strExtension[1]

        return outDestFile

    # Resynchronize files based on changed parameters: sequence, position, name
    def synchNumbers(self):
        # Get number sequence
        intResynch = self.ui.spinSequence.value()

        # Move through table
        for nbrIndex in range(self.ui.listFiles.rowCount()):
            srcFile = self.ui.listFiles.item(nbrIndex, 1)

            # debug print ("source"+ srcFile.text())
            # Call Rename file function
            strDestFile = self.renameFiles(srcFile.text(), intResynch)
            itemDestFile = QtWidgets.QTableWidgetItem()
            itemDestFile.setText(strDestFile)
            self.ui.listFiles.setItem(nbrIndex, 2, itemDestFile)

            nbrIndex += 1
            intResynch += 1

    # Move selected files
    def moveFiles(self, direction):

        indexes = self.ui.listFiles.selectionModel().selectedRows()

        if not indexes:
            return

        if direction == "UP":
            for index in sorted(indexes):
                intRow = index.row()
                # debug only - print('Row %d is selected' % intRow)
                if intRow > 0:
                    self.ui.listFiles.insertRow(intRow - 1)
                    for i in range(self.ui.listFiles.columnCount()):
                        self.ui.listFiles.setItem(
                            intRow - 1, i, self.ui.listFiles.takeItem(intRow + 1, i))
                    self.ui.listFiles.removeRow(intRow + 1)

                    # Change focus to moved file
                    newIndex = self.ui.listFiles.selectionModel().model().index(intRow - 1, 0)
                    self.ui.listFiles.selectionModel().select(newIndex, QItemSelectionModel.Select)
                    self.ui.listFiles.setCurrentIndex(newIndex)
        else:
            for index in sorted(indexes, reverse=True):
                intRow = index.row()
                # debug only - print('Row %d is selected' % intRow)
                if intRow < int(self.ui.listFiles.rowCount()-1):
                    self.ui.listFiles.insertRow(intRow + 2)
                    for i in range(self.ui.listFiles.columnCount()):
                        self.ui.listFiles.setItem(
                            intRow + 2, i, self.ui.listFiles.takeItem(intRow, i))
                        # self.ui.listFiles.setCurrentCell(intRow + 2,column)
                    self.ui.listFiles.removeRow(intRow)

                    # Change row focus to moved file
                    newIndex = self.ui.listFiles.selectionModel().model().index(intRow + 1, 0)
                    self.ui.listFiles.selectionModel().select(newIndex, QItemSelectionModel.Select)
                    self.ui.listFiles.setCurrentIndex(newIndex)

            self.ui.listFiles.setFocus()

    # Move up
    def moveUp(self):
        self.moveFiles("UP")
        self.synchNumbers()

    # Move down
    def moveDown(self):
        self.moveFiles("DOWN")
        self.synchNumbers()

    # Remove files
    def removeFiles(self):
        global intSequence
        indexes = self.ui.listFiles.selectionModel().selectedRows()
        for index in sorted(indexes):
            self.ui.listFiles.removeRow(index.row())
        self.synchNumbers()
        intSequence = intSequence - 1

    # Clear table
    def cleanList(self):
        global intSequence
        self.ui.listFiles.selectionModel().model().removeRows(0, self.ui.listFiles.rowCount())
        intSequence = self.ui.spinSequence.value()

    # Rename files phisically
    def applyRenaming(self):

        # debug only - print("Renombrado de archivos")
        # Move through table
        for nbrIndex in range(self.ui.listFiles.rowCount()):
            srcFolder = self.ui.listFiles.item(nbrIndex, 0).toolTip()
            srcFile = self.ui.listFiles.item(nbrIndex, 1)
            dstFile = self.ui.listFiles.item(nbrIndex, 2)

            src = srcFolder + srcFile.text()
            dst = srcFolder + dstFile.text()

            # debug only - print(src + " >>> " + dst)

            os.rename(src, dst)
        # debug only - print("Renombrado finalizado")
        self.cleanList()

    def itemAlreadyExists(self, inSrcFile):

        itemList = self.ui.listFiles.findItems(inSrcFile, QtCore.Qt.MatchExactly)
        if len(itemList) > 0:
            return True
        else:
            return False

    def callOpenDialog(self):
        self.openFileNamesDialog()

    def openFileNamesDialog(self):

        global intSequence
        global strPosition

        # Get number sequence
        if intSequence == 0:
            intSequence = self.ui.spinSequence.value()

        # Get position
        strPosition = self.ui.comboStartEnd.currentData()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            self, "Add archivos", "", "All Files (*)", options=options)

        if files:

            for filename in files:
                #                filename = os.path.normpath(filename)
                srcFile = filename.split("/")[-1]
                srcFolder = filename.split(srcFile, 1)[0]
                lenSplit = len(srcFolder.split("/")) - 2
                srcFolderSplit = "../" + srcFolder.split("/")[lenSplit] + "/"

                # debug only - print ("File " + srcFile)
                # debug only - print ("Path " + srcFolder)

                if self.itemAlreadyExists(srcFile) == False:

                    intRow = int(self.ui.listFiles.rowCount())
                    itemFolderSplit = QtWidgets.QTableWidgetItem()
                    itemFolderSplit.setText(srcFolderSplit)
                    itemFolderSplit.setToolTip(srcFolder)

                    self.ui.listFiles.insertRow(intRow)
                    self.ui.listFiles.setItem(intRow, 0, itemFolderSplit)

                    itemSourceFile = QtWidgets.QTableWidgetItem()
                    itemSourceFile.setText(srcFile)
                    self.ui.listFiles.setItem(intRow, 1, itemSourceFile)

                    # Call file renaming function (just name, not phisically)
                    strDestFile = self.renameFiles(srcFile, intSequence)

                    itemDestFile = QtWidgets.QTableWidgetItem()
                    itemDestFile.setText(strDestFile)
                    self.ui.listFiles.setItem(intRow, 2, itemDestFile)

                intSequence += 1

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = ag.height() - sg.height() - widget.height()
        self.move(x, y)


intSequence = 0
strPosition = ""
file = sys.argv[0]
dirname = os.path.dirname(file)

if __name__ == '__main__':
    intRow = 0
    app = QtWidgets.QApplication(sys.argv)
    ex = SimpleRenamer()
    ex.show()
    sys.exit(app.exec())
