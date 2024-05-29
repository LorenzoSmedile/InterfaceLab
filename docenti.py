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
        lista= [{"Matteo","Picciolini",18},{"Daniele","Morelli",9},{"Samuele","Maranghi",18}]
        
        riga=0
        colonna=0
        
        variabile=-1
        
        for element in lista:
            
            variabile=variabile+1
            print(lista[variabile])
            self.table.setItem(riga,colonna, lista[variabile])
            riga=riga+1
            colonna=colonna+1
            
            
            
            
        
        
        
        
        
        
       
        


       

        
        
        
 


app = QApplication(sys.argv)
window = UI()
app.exec_()