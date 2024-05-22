# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton ,QTableWidget,QTableWidgetItem
from PyQt5 import uic
import sys
 
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"C:\Users\lorenzosmedile\Documents\docenti\mainwindow.ui", self)
        self.tableWidget = QTableWidget()
        

        
       
 
        # find the widgets in the xml file
 
        self.button= self.findChild(QPushButton,"caricaDocenti")
        self.button.clicked.connect(self.clickedBtn)
        self.show()
        
        self.table = self.findChild(QTableWidget, "tabella")
        self.table.setColumnCount(3)
        self.table.setRowCount(3)
        self.table.setHorizontalHeaderLabels(["Nome", "Cognome","Ore"])
        
        
        
    
 
    def clickedBtn (self):
        lista= [{"nome":"pippo","cognome":"baudo","ore":"4"}]
        lista2= [{"nome":"lorenzo","cognome":"smedile","ore":"10"}]
        lista3= [{"nome":"matteo","cognome":"picciolini","ore":"6"}]
        
        
        item_name = QTableWidgetItem("matteo")
        self.table.setItem(0,0,item_name)
        item_name = QTableWidgetItem("picciolini")
        self.table.setItem(0,1,item_name)
        item_name = QTableWidgetItem("18")
        self.table.setItem(0,2,item_name)
            
        


       

        
        
        
 


app = QApplication(sys.argv)
window = UI()
app.exec_()