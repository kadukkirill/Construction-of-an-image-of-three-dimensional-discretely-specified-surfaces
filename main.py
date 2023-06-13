#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window import *
import matplotlib.pyplot as plt
import math
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #Вызов фунции нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.buttonPress)
        self.ui.pushButton_2.clicked.connect(self.buttonPress_2)
        self.ui.pushButton_3.clicked.connect(self.buttonPress_3)

    #функция при нажатии на кнопку Побудувати
    def buttonPress(self):
        fig, axes = plt.subplots(figsize=(6*2,4*2), subplot_kw={'projection': '3d'})

        first = int(self.ui.lineEdit_2.text())
        second = int(self.ui.lineEdit_3.text())
        h = float(self.ui.lineEdit_4.text())

        x = np.arange(first, second, h)
        y = np.arange(first, second, h)
        x, y = np.meshgrid(x, y)

        z = np.array(eval( self.ui.lineEdit.text() ))

        surf = axes.plot_surface(x, y, z, cmap=cm.coolwarm)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        
        axes.set_xlabel('x', fontsize=15)
        axes.set_ylabel('y', fontsize=15)
        axes.set_zlabel('z', fontsize=15)

        plt.title("Графік", fontsize=20)
        plt.show()

    def buttonPress_2(self):
        self.ui.lineEdit.setText("x**2 + y**2")
        self.ui.lineEdit_2.setText("-10")
        self.ui.lineEdit_3.setText("10")
        self.ui.lineEdit_4.setText("0.5")

    def buttonPress_3(self):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
