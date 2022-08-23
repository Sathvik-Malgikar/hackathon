import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap


# image=QPixmap(fileName='mspaint.jpg')



class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("untitled.ui", self)


app = QApplication(sys.argv)
welcome = WelcomeScreen()
stack = QStackedWidget()
stack.addWidget(welcome)
stack.setFixedHeight(800)
stack.setFixedWidth(1200)
stack.show()

def action ():

    # text="gooWHOOAA!!!d"
    text = welcome.tdc.toPlainText()
    # print(welcome.textbox.text())
    print(text)
    b=welcome.labelforme.isVisible()
    print(b)
    if (welcome.labelforme.isVisible()):
        welcome.labelforme.setVisible(0)
    else:
        welcome.labelforme.setVisible(1)
    # welcome.labelforme.setPixmap(image)

text="good"
welcome.tdc.setText(text)
welcome.activator.clicked.connect(action)



try:
    sys.exit(app.exec_())
except:
    print("exiting")
