from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QPushButton
import sys 

app = QApplication.instance() 
if not app: 
    app = QApplication(sys.argv)
fen = QWidget ()

bouton1= QPushButton("Fayal")
bouton2= QPushButton("Adriel")

layout = QVBoxLayout()
layout.addWidget(bouton1)
layout.addWidget(bouton2)
fen.setLayout(layout)

fen.show()
app.exec_()

    
    
    #with open ("ipsum", "r") as fichier:
    #    app = QApplication([])
    #   label = QLabel(fichier.read())
    #  label.show()
    # app.exec_()
