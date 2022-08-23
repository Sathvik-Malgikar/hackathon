import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi


class Wind(QDialog):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle('Welcome')

        loadUi(r"C:\Users\Srujan\Documents\c scripts\hackathon\welc2.ui", self)
        # self.show()
        # self.setFixedWidth(1100)
        # self.setFixedHeight(800)


app2 = QApplication(sys.argv)
st = QStackedWidget()
w = Wind()
w.setWindowTitle('Welcome -G2S')
st.addWidget(w)
st.setFixedWidth(1100)
st.setFixedHeight(800)
st.show()


def likhi():
    w.close()
    st.removeWidget(w)
    w.destroy()
    import Pyqt52


w.pushButton.clicked.connect(likhi)

app2.exec()
