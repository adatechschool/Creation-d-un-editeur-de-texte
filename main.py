from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QPushButton
import sys 

app = QApplication([]) 
fen = QWidget()

bouton_fayal = QPushButton("Fayal")
bouton_adriel = QPushButton("Adriel")

layout = QVBoxLayout()
layout.addWidget(bouton_fayal)
layout.addWidget(bouton_adriel)
fen.setLayout(layout)

fen.show()
app.exec_()
