from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

application = QApplication([])
main_frame = QWidget()

box = QHBoxLayout()

box.addWidget(QTextEdit())

main_frame.setLayout(box)
main_frame.show()

application.exec_()
