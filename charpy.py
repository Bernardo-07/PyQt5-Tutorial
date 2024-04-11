# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charpy.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import tempfile
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(150, 10, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Solid Edge ANSI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(20, 300, 101, 41))
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.attach_file)  
        
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(440, 300, 101, 41))
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.export_to_pdf)
        
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(170, 80, 221, 221))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("temperatura_maxima.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "TEMPERATURE TRANSITION CURVE"))
        self.button1.setText(_translate("MainWindow", "Anexar"))
        self.button2.setText(_translate("MainWindow", "Exportar"))

    def attach_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(None, "Anexar Arquivo", "", "All Files (*);;Text Files (*.txt)", options=options)
        if filename:
            print("Arquivo anexado:", filename)
            data = np.loadtxt(filename)
            
            # Extrair primeira coluna como variável x e segunda coluna como variável y
            x = data[:, 0]
            y = data[:, 1]
            
            # Plotar os dados
            plt.plot(x, y)
            plt.xlabel('X Label')
            plt.ylabel('Y Label')
            plt.title('Plot dos Dados do Arquivo TXT')
            
            # Salvar o plot em um arquivo temporário
            temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
            plt.savefig(temp_file.name)
            temp_file.close()
            
            # Carregar a imagem do arquivo temporário em uma variável
            image = QtGui.QPixmap(temp_file.name)
            self.img.setPixmap(image)
            self.temp_file_path = temp_file.name 

    def export_to_pdf(self):
        if hasattr(self, 'temp_file_path'):
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getSaveFileName(None, "Exportar para PDF", "", "PDF Files (*.pdf)", options=options)
            if filename:
                c = canvas.Canvas(filename, pagesize=letter)
                c.drawImage(ImageReader(self.temp_file_path), 0, 0, width=letter[0], height=letter[1])
                c.showPage()
                c.save()
                print("Imagem exportada para PDF com sucesso!")
        else:
            print("Por favor, gere a imagem antes de exportar para PDF.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

