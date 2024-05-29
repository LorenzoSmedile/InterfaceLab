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
        lista=[{"nomeP":"Matteo","nomeS":"Picciolini","nOre":"5"},{"nomeP":"Andrea","nomeS":"Ricci","nOre":"10"},{"nomeP":"Samuele","nomeS":"Maranghi","nOre":"18"}]

        
        riga=0
        colonna=0
      
        
        for element in lista:
            item_name = QTableWidgetItem(element["nomeP"])
            self.table.setItem(riga,0, item_name)
          
            
            item_name2 = QTableWidgetItem(element["nomeS"])
            self.table.setItem(riga,1, item_name2)
           
            item_name3 = QTableWidgetItem(element["nOre"])
            self.table.setItem(riga,2, item_name3)
            riga=riga+1
            
            
            
            
            
 
app = QApplication(sys.argv)
window = UI()
app.exec_()