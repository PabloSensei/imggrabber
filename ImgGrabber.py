#coding: utf-8
import sys, MainWindow, os
from PyQt4 import QtCore, QtGui

class Main(QtGui.QMainWindow):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self ,parent)
		self.ui = MainWindow.Ui_MainWindow()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.fileDialogBtn, QtCore.SIGNAL('clicked()'), self.fileDialog)
		QtCore.QObject.connect(self.ui.downloadBtn, QtCore.SIGNAL('clicked()'), self.get)
		file = open('Settings.ini')
		

	def fileDialog(self):
		fd = QtGui.QFileDialog(self)
		self.ui.path_line.setText(fd.getExistingDirectory())
	
	def get(self):
		ProgressBar = [
			self.ui.PB_behomini,
			self.ui.PB_chan,
			self.ui.PB_danboru,
			self.ui.PB_gelbooru,
			self.ui.PB_idol,
			self.ui.PB_konachan,
			self.ui.PB_nekobooru,
			self.ui.PB_yande
		]
		CheckBox = [
			self.ui.CB_behomini,
			self.ui.CB_chan,
			self.ui.CB_danboru,
			self.ui.CB_gelbooru,
			self.ui.CB_idol,
			self.ui.CB_konachan,
			self.ui.CB_nekobooru,
			self.ui.CB_yande
		]
		for i in ProgressBar: i.reset()
		board = []
		self.ui.downloadBtn.setEnabled(False)
		for i in CheckBox:			
			if i.isChecked(): board.append(str(i.text()))


def main():
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	app, window = QtGui.QApplication(sys.argv), Main()
	main()