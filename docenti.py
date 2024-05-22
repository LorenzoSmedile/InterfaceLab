# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit ,QTableWidget,QTableWidgetItem,QHeaderView
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"C:\Users\lorenzosmedile\Documents\docenti\mainwindow.ui", self)
        self.tableWidget = QTableWidget()
        
        self.tableWidget.setColumnCount(3)  
        self.tableWidget.setRowCount(3)
 
        # find the widgets in the xml file
 
        self.button= self.findChild(QPushButton,"caricaDocenti")
        self.button.clicked.connect(self.clickedBtn)
        self.show()
 
    
 
    def clickedBtn (self):
        self.tableWidget.setItem(0,0, (str), "Ciao") 

        
        
        
 


app = QApplication(sys.argv)
window = UI()
app.exec_()