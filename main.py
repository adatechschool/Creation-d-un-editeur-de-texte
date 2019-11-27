from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

with open ("ipsum", "r") as fichier:
    app = QApplication([])
    label = QLabel(fichier.read())
    label.show()
    app.exec_()
