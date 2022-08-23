
from PIL import Image
from PIL.ImageQt import ImageQt
import fingertranslatealt
import gtts
import pygame
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QMainWindow
from PyQt5.uic import loadUi

from PyQt5.QtGui import QPixmap
import sys
import socket
import cv2
from PyQt5.QtGui import QMovie
pTime = 0


class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi(r'C:\Users\Srujan\Documents\c scripts\hackathon\projui.ui', self)


class Screen1(QDialog):
    def __init__(self):
        super(Screen1, self).__init__()
        loadUi(r'C:\Users\Srujan\Documents\c scripts\hackathon\welcomeui.ui', self)


pygame.mixer.init()
# import pyttsx3

# engine = pyttsx3.init('sapi5')
# engine.setProperty("rate",120)
# voices = engine.getProperty("voices")

# engine.setProperty("voices",voices[1].id)


def toggle():

    if screen2.textEdit.isVisible():
        screen2.textEdit.hide()
        screen2.textEdit_2.hide()
    else:
        screen2.textEdit.show()
        screen2.textEdit_2.show()


def pingc():
    # try :
    #     samp=gtts.gTTS(lang='en',text='ping')
    #     print(type(samp))
    # except:
    #     Connected= False
    #     print('yes')
    #     screen2.connect_label.setHidden(True)
    # else:
    #     Connected = True
    #     print("no")
    #     screen2.connect_label.setHidden(False)

    try:
        socket.create_connection(('Google.com', 80))
        screen2.connect_label.show()
    except OSError:
        screen2.connect_label.hide()


def action2():
    try:
        audio = screen2.textbox_2.toPlainText()

        audio = gtts.gTTS(
            lang='en', text=screen2.textbox_2.toPlainText(), slow=True)
        audio.save(r'C:\Users\Srujan\Documents\c scripts\hackathon\a2.mp3')
        pygame.mixer.music.load(
            r'C:\Users\Srujan\Documents\c scripts\hackathon\a2.mp3')
        pygame.mixer.music.play(loops=1)
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        screen2.activator_2.clicked.disconnect()

    except:
        print("Internet Connection required for TextToSpeech")


def action():
    try:
        # text=screen2.textbox.toPlainText()
        # engine.say(text)
        # engine.runAndWait()

        audio = screen2.textbox.toPlainText()
        # print(audio)

        if audio == "No Gesture detected":
            return None

        audio = gtts.gTTS(
            lang='en', text=screen2.textbox.toPlainText(), slow=True)
        audio.save(r'C:\Users\Srujan\Documents\c scripts\hackathon\a1.mp3')
        pygame.mixer.music.load(
            r'C:\Users\Srujan\Documents\c scripts\hackathon\a1.mp3')
        pygame.mixer.music.play(loops=1)
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        screen2.activator.clicked.disconnect()
        screen2.textbox.setText('No Gesture detected')
        global old
        old = 'No Gesture detected'
        global result
        del result
        # screen2.giflabel.setHidden(True)
        screen2.imageframe.setHidden(False)
    except:
        print("Internet Connection required for TextToSpeech")


def act2():

    stack.removeWidget(screen1)
    screen1.destroy()
    screen2.setWindowTitle('Capture Gestures and translate to speech -G2S')
    stack.addWidget(screen2)

    stack.show()


app = QApplication(sys.argv)
screen2 = Screen2()
screen1 = Screen1()
stack = QStackedWidget()
screen1.setWindowTitle('Instruction to use - G2S')
stack.addWidget(screen1)

stack.setFixedHeight(800)
stack.setFixedWidth(1100)
stack.show()

cap = cv2.VideoCapture(0)
movie = QMovie(r'C:\Users\Srujan\Documents\c scripts\hackathon\bg.gif')


screen1.label.setMovie(movie)
screen1.label.setScaledContents(True)
movie.start()
screen1.pushButton.clicked.connect(act2)
screen2.activator_2.clicked.connect(action2)
# screen2.giflabel.setHidden(True)

pingc()
ping_counter = 0
while True:
    ping_counter += 1
    if ping_counter == 100:
        pingc()
        ping_counter = 0
    s, numpyarray = cap.read()

    cv2.waitKey(1)
    screen2.pushButton.clicked.connect(toggle)
    result_tuple = fingertranslatealt.runner(numpyarray)

    if isinstance(result_tuple, tuple):

        numpyarray, result = result_tuple
        numpyarray = cv2.flip(numpyarray, 1)
    else:
        numpyarray = result_tuple
        numpyarray = cv2.flip(numpyarray, 1)
    try:
        if old == 'No Gesture detected':
            screen2.textbox.setText(result)
            screen2.textbox_2.setText(result)

        elif old != result:
            screen2.textbox.setText(screen2.textbox.toPlainText()+'\n'+result)
            screen2.textbox_2.setText(result)
        old = result

    except NameError:
        screen2.textbox.setText('No Gesture detected')
        old = 'No Gesture detected'
    screen2.activator.clicked.connect(action)
    screen2.activator_2.clicked.connect(action2)
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    # cv2.putText(image, f'FPS : {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
    numpyarray = cv2.cvtColor(numpyarray, cv2.COLOR_RGBA2BGRA)

    image = Image.fromarray(numpyarray)

    qimg = ImageQt(image)
    pixmap = QPixmap.fromImage(qimg)
    screen2.imageframe.setPixmap(pixmap)
    # pingc()

app.exec()
