from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

application = QApplication([])
main_window = QWidget()

boite = QVBoxLayout()

action_ouvrir = QAction("Ouvrir…")

menu_gestion = QMenuBar()
menu_édition = QMenuBar()
text_édition = QTextEdit()

fichier_ouvrir = menu_gestion.addMenu("Fichier")
fichier_ouvrir.addAction(action_ouvrir)

boite.addWidget(menu_gestion)
boite.addWidget(text_édition)
boite.addWidget(menu_édition)

main_window.setLayout(boite)
main_window.show()

application.exec_()
