# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri Apr 15 18:49:52 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(506, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(506, 150))
        MainWindow.setMaximumSize(QtCore.QSize(506, 150))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 121))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Get = QtGui.QPushButton(self.layoutWidget)
        self.Get.setObjectName(_fromUtf8("Get"))
        self.gridLayout.addWidget(self.Get, 1, 2, 1, 1)
        self.LimitInput = QtGui.QLineEdit(self.layoutWidget)
        self.LimitInput.setMaxLength(999999999)
        self.LimitInput.setObjectName(_fromUtf8("LimitInput"))
        self.gridLayout.addWidget(self.LimitInput, 3, 1, 1, 1)
        self.Lmit = QtGui.QLabel(self.layoutWidget)
        self.Lmit.setObjectName(_fromUtf8("Lmit"))
        self.gridLayout.addWidget(self.Lmit, 3, 2, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty(_fromUtf8("value"), 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 3)
        self.Board = QtGui.QComboBox(self.layoutWidget)
        self.Board.setObjectName(_fromUtf8("Board"))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.Board.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.Board, 1, 1, 1, 1)
        self.TagInput = QtGui.QLineEdit(self.layoutWidget)
        self.TagInput.setObjectName(_fromUtf8("TagInput"))
        self.gridLayout.addWidget(self.TagInput, 2, 1, 1, 1)
        self.Tag = QtGui.QLabel(self.layoutWidget)
        self.Tag.setObjectName(_fromUtf8("Tag"))
        self.gridLayout.addWidget(self.Tag, 2, 2, 1, 1)
        self.PathEdit = QtGui.QLineEdit(self.layoutWidget)
        self.PathEdit.setObjectName(_fromUtf8("PathEdit"))
        self.gridLayout.addWidget(self.PathEdit, 0, 1, 1, 1)
        self.PathButton = QtGui.QPushButton(self.layoutWidget)
        self.PathButton.setObjectName(_fromUtf8("PathButton"))
        self.gridLayout.addWidget(self.PathButton, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ImgGrabber", None, QtGui.QApplication.UnicodeUTF8))
        self.Get.setText(QtGui.QApplication.translate("MainWindow", "Get", None, QtGui.QApplication.UnicodeUTF8))
        self.LimitInput.setText(QtGui.QApplication.translate("MainWindow", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.Lmit.setText(QtGui.QApplication.translate("MainWindow", "Limit", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(0, QtGui.QApplication.translate("MainWindow", "konachan.com", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(1, QtGui.QApplication.translate("MainWindow", "oreno.imouto.org", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(2, QtGui.QApplication.translate("MainWindow", "danbooru.donmai.us", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(3, QtGui.QApplication.translate("MainWindow", "behoimi.org", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(4, QtGui.QApplication.translate("MainWindow", "nekobooru.net", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(5, QtGui.QApplication.translate("MainWindow", "genso.ws", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(6, QtGui.QApplication.translate("MainWindow", "chan.sankakucomplex.com", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(7, QtGui.QApplication.translate("MainWindow", "idol.sankakucomplex.com", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(8, QtGui.QApplication.translate("MainWindow", "gelbooru.com", None, QtGui.QApplication.UnicodeUTF8))
        self.Board.setItemText(9, QtGui.QApplication.translate("MainWindow", "animemahou.com", None, QtGui.QApplication.UnicodeUTF8))
        self.TagInput.setText(QtGui.QApplication.translate("MainWindow", "bakemonogatari", None, QtGui.QApplication.UnicodeUTF8))
        self.Tag.setText(QtGui.QApplication.translate("MainWindow", "Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.PathButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

