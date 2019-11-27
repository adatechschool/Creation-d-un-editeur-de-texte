from PyQt5.QtWidgets import QApplication, QLabel
with open ("ipsum", "r") as fichier:
    pass
app = QApplication([])
label = QLabel("Hello world!")
label.show()
app.exec_()
