from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 400, 400)
    win.setWindowTitle("Let him Cook!")
    body(win)
    win.show()
    sys.exit(app.exec())

def body(win):
    label = QtWidgets.QLabel(win)
    label.setText("Hello world")
    label.move(50, 50)

    button = QtWidgets.QPushButton(win)
    button.setText("Click me?")
    button.clicked.connect(action)

def action():
    print("Clicked")

window()