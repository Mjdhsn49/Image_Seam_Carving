# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'designFull.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnMark = QtWidgets.QPushButton(self.centralwidget)
        self.btnMark.setGeometry(QtCore.QRect(580, 320, 71, 27))
        self.btnMark.setStyleSheet("QPushButton{background-color:rgb(0, 170, 255); color:rgb(255, 255, 255)}")
        self.btnMark.setObjectName("btnMark")
        self.btnResize = QtWidgets.QPushButton(self.centralwidget)
        self.btnResize.setGeometry(QtCore.QRect(580, 250, 71, 27))
        self.btnResize.setStyleSheet("QPushButton{background-color:rgb(0, 170, 255); color:rgb(255, 255, 255)}")
        self.btnResize.setObjectName("btnResize")
        self.percentRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.percentRadio.setGeometry(QtCore.QRect(600, 110, 81, 22))
        self.percentRadio.setChecked(True)
        self.percentRadio.setObjectName("percentRadio")
        self.sizeRadioGroup = QtWidgets.QButtonGroup(MainWindow)
        self.sizeRadioGroup.setObjectName("sizeRadioGroup")
        self.sizeRadioGroup.addButton(self.percentRadio)
        self.pixelRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.pixelRadio.setGeometry(QtCore.QRect(710, 110, 61, 22))
        self.pixelRadio.setObjectName("pixelRadio")
        self.sizeRadioGroup.addButton(self.pixelRadio)
        self.positiveRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.positiveRadio.setGeometry(QtCore.QRect(690, 320, 81, 22))
        self.positiveRadio.setChecked(True)
        self.positiveRadio.setObjectName("positiveRadio")
        self.energyRadioGroup = QtWidgets.QButtonGroup(MainWindow)
        self.energyRadioGroup.setObjectName("energyRadioGroup")
        self.energyRadioGroup.addButton(self.positiveRadio)
        self.negetiveRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.negetiveRadio.setGeometry(QtCore.QRect(690, 350, 91, 22))
        self.negetiveRadio.setObjectName("negetiveRadio")
        self.energyRadioGroup.addButton(self.negetiveRadio)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 541, 561))
        self.tabWidget.setMinimumSize(QtCore.QSize(541, 561))
        self.tabWidget.setMaximumSize(QtCore.QSize(541, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setMinimumSize(QtCore.QSize(550, 550))
        self.tab.setMaximumSize(QtCore.QSize(550, 550))
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, -20, 550, 550))
        self.widget.setMinimumSize(QtCore.QSize(550, 550))
        self.widget.setMaximumSize(QtCore.QSize(550, 550))
        self.widget.setObjectName("widget")
        self.imageView = QtWidgets.QLabel(self.widget)
        self.imageView.setGeometry(QtCore.QRect(0, 0, 550, 550))
        self.imageView.setMinimumSize(QtCore.QSize(550, 550))
        self.imageView.setMaximumSize(QtCore.QSize(550, 550))
        self.imageView.setText("")
        self.imageView.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView.setObjectName("imageView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.imageView_3 = QtWidgets.QLabel(self.tab_3)
        self.imageView_3.setGeometry(QtCore.QRect(0, -20, 550, 550))
        self.imageView_3.setMinimumSize(QtCore.QSize(550, 550))
        self.imageView_3.setMaximumSize(QtCore.QSize(550, 550))
        self.imageView_3.setText("")
        self.imageView_3.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView_3.setObjectName("imageView_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMinimumSize(QtCore.QSize(550, 550))
        self.tab_2.setMaximumSize(QtCore.QSize(550, 550))
        self.tab_2.setObjectName("tab_2")
        self.imageView_2 = QtWidgets.QLabel(self.tab_2)
        self.imageView_2.setGeometry(QtCore.QRect(0, -20, 550, 550))
        self.imageView_2.setMinimumSize(QtCore.QSize(550, 550))
        self.imageView_2.setMaximumSize(QtCore.QSize(550, 550))
        self.imageView_2.setText("")
        self.imageView_2.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView_2.setObjectName("imageView_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.imageView_4 = QtWidgets.QLabel(self.tab_4)
        self.imageView_4.setGeometry(QtCore.QRect(0, -20, 550, 550))
        self.imageView_4.setMinimumSize(QtCore.QSize(550, 550))
        self.imageView_4.setMaximumSize(QtCore.QSize(550, 550))
        self.imageView_4.setText("")
        self.imageView_4.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView_4.setObjectName("imageView_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.oSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.oSizeLabel.setGeometry(QtCore.QRect(640, 20, 91, 20))
        self.oSizeLabel.setObjectName("oSizeLabel")
        self.sizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.sizeLabel.setGeometry(QtCore.QRect(620, 50, 121, 20))
        self.sizeLabel.setStyleSheet("QLabel { background-color : rgb(0, 170, 255); color: rgb(255, 255, 255)}")
        self.sizeLabel.setText("")
        self.sizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeLabel.setObjectName("sizeLabel")
        self.widthInput = QtWidgets.QSpinBox(self.centralwidget)
        self.widthInput.setGeometry(QtCore.QRect(600, 150, 61, 27))
        self.widthInput.setMaximum(2000)
        self.widthInput.setProperty("value", 100)
        self.widthInput.setObjectName("widthInput")
        self.hightInput = QtWidgets.QSpinBox(self.centralwidget)
        self.hightInput.setGeometry(QtCore.QRect(700, 150, 61, 27))
        self.hightInput.setMaximum(2000)
        self.hightInput.setProperty("value", 100)
        self.hightInput.setObjectName("hightInput")
        self.dSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.dSizeLabel.setGeometry(QtCore.QRect(640, 90, 91, 20))
        self.dSizeLabel.setObjectName("dSizeLabel")
        self.xLabel = QtWidgets.QLabel(self.centralwidget)
        self.xLabel.setGeometry(QtCore.QRect(670, 146, 20, 31))
        self.xLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xLabel.setObjectName("xLabel")
        self.markLabel = QtWidgets.QLabel(self.centralwidget)
        self.markLabel.setGeometry(QtCore.QRect(660, 290, 61, 17))
        self.markLabel.setObjectName("markLabel")
        self.energyBox = QtWidgets.QComboBox(self.centralwidget)
        self.energyBox.setGeometry(QtCore.QRect(650, 200, 111, 27))
        self.energyBox.setObjectName("energyBox")
        self.energyBox.addItem("")
        self.energyBox.addItem("")
        self.endrgyLabel = QtWidgets.QLabel(self.centralwidget)
        self.endrgyLabel.setGeometry(QtCore.QRect(590, 196, 51, 31))
        self.endrgyLabel.setObjectName("endrgyLabel")
        self.btnErase = QtWidgets.QPushButton(self.centralwidget)
        self.btnErase.setGeometry(QtCore.QRect(580, 360, 71, 27))
        self.btnErase.setStyleSheet("QPushButton{background-color:rgb(0, 170, 255); color:rgb(255, 255, 255)}")
        self.btnErase.setObjectName("btnErase")
        self.btnMark.raise_()
        self.btnResize.raise_()
        self.percentRadio.raise_()
        self.pixelRadio.raise_()
        self.positiveRadio.raise_()
        self.negetiveRadio.raise_()
        self.oSizeLabel.raise_()
        self.sizeLabel.raise_()
        self.widthInput.raise_()
        self.hightInput.raise_()
        self.dSizeLabel.raise_()
        self.xLabel.raise_()
        self.markLabel.raise_()
        self.energyBox.raise_()
        self.endrgyLabel.raise_()
        self.tabWidget.raise_()
        self.btnErase.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seam Carving"))
        self.btnMark.setText(_translate("MainWindow", "Mark"))
        self.btnResize.setText(_translate("MainWindow", "Resize"))
        self.percentRadio.setText(_translate("MainWindow", "Percent"))
        self.pixelRadio.setText(_translate("MainWindow", "Pixel"))
        self.positiveRadio.setText(_translate("MainWindow", "Positive"))
        self.negetiveRadio.setText(_translate("MainWindow", "Negetive"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Original"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Energy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Seams"))
        self.oSizeLabel.setText(_translate("MainWindow", "Original Size"))
        self.dSizeLabel.setText(_translate("MainWindow", "Desired Size"))
        self.xLabel.setText(_translate("MainWindow", "x"))
        self.markLabel.setText(_translate("MainWindow", "Marking"))
        self.energyBox.setItemText(0, _translate("MainWindow", "Sobel"))
        self.energyBox.setItemText(1, _translate("MainWindow", "Laplacian"))
        self.endrgyLabel.setText(_translate("MainWindow", "Energy:"))
        self.btnErase.setText(_translate("MainWindow", "Erase"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

