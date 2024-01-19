# from Alexa_window import *
import os
import time
import sys
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import pyttsx3
import wikipedia
import smtplib
import datetime
from screen2 import *
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
hello = Ui_page2
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
WAKE = "activate"
print("Start")
engine.setProperty('voice', voice_id)
class Ui_Dialog(object):


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1124, 686)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1141, 691))
        self.label.setStyleSheet("background-image: url(:/newPrefix/pic.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 691, 291))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 430, 161, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 430, 161, 61))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Courier New\'; font-size:20pt; font-weight:700; color:#ffffff;\">HELLO, I AM JARVIS.</span></p><p><span style=\" font-family:\'Courier New\'; font-size:20pt; font-weight:700; color:#ffffff;\">WELCOME TO THE COLLEGE.</span></p><p><br/></p><p><span style=\" font-family:\'Courier New\'; font-size:20pt; font-weight:700; color:#ffffff;\">HOW WOULD YOU LIKE TO GIVE YOUR ATTANDANCE </span></p><p><br/></p><p><span style=\" font-family:\'Courier New\'; font-size:20pt; font-weight:700; color:#ffffff;\">WITH ME OR VIRTUAL MOUSE</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "JARVIS "))
        self.pushButton_2.setText(_translate("Dialog", "VIRTUAL MOUSE"))


    def setupUi3(self, page4):
        page4.setObjectName("page4")
        page4.resize(458, 338)

        self.retranslateUi3(page4)
        QtCore.QMetaObject.connectSlotsByName(page4)

    def retranslateUi3(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("page4", "page4"))


def talk(text):
    engine.say(text)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sethicyberzone@gmail.com', '**********')  # email & password
    server.sendmail('sethicyberzone@gmail.com', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        talk("Good Morning!")

    elif (hour >= 12) and (hour < 18):
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk("SAY ACTIVATE")

def wishMe1():

    talk("MARK YOUR ATTENDENCE AS TEACHER OR STUDENT")

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


# def virtualmouse():
#     ##########################
#     wCam, hCam = 640, 480
#     frameR = 30
#     smoothening = 10
#     ##########################
#
#     pTime = 0
#     plocX, plocY = 0, 0  # previous location of X and Y
#     clocX, clocY = 0, 0  # current location of X and Y
#
#     cap = cv2.VideoCapture(0)
#     cap.set(3, wCam)
#     cap.set(4, hCam)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#     detector = htm.handDetector(maxHands=1)
#     wScr, hScr = autopy.screen.size()
#     # print(wScr, hScr)
#
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         lmList, bbox = detector.findPosition(img)
#
#         if len(lmList) != 0:
#             x1, y1 = lmList[8][1:]
#             x2, y2 = lmList[12][1:]
#
#             # print(x1,y1,x2,y2)
#
#             fingers = detector.fingersUp()
#             # print(fingers)
#             cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 0), 2)
#
#             if fingers[1] == 1 and fingers[2] == 0:
#                 x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
#                 y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
#
#                 clocX = plocX + (x3 - plocX) / smoothening
#                 clocY = plocY + (y3 - plocY) / smoothening
#
#                 autopy.mouse.move(wScr - clocX, clocY)
#                 cv2.circle(img, (x1, y1), 7, (255, 0, 0), cv2.FILLED)
#                 plocX, plocY = clocX, clocY
#
#             if fingers[1] == 1 and fingers[2] == 1:
#                 length, img, lineInfo = detector.findDistance(8, 12, img)
#                 print(length)
#                 if length < 40:
#                     cv2.circle(img, (lineInfo[4], lineInfo[5]), 7, (0, 255, 0), cv2.FILLED)
#                     autopy.mouse.click()
#
#
#
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#         cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
#
#         cv2.imshow("Image", img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # Release handle to the webcam
#     cap.release()
#     cv2.destroyWindow(virtualmouse())
#


def run2():
    print("Hello")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    page2 = QtWidgets.QDialog()
    ui1 = Ui_page2()
    page3 = QtWidgets.QDialog()
   # ui2 = Ui_page3()
    page4 = QtWidgets.QDialog()
    # Dialog.show()
    wishMe()
    command = take_command()
    print(command)
    while True:
        if 'activate' in command:
            # Dialog.hide()
            ui1.setupUi1(page2)
            page2.show()
            #wishMe1()
           # # command = take_command()
           #  print(command)
           #  if 'teacher' in command:
           #      run2()
           #  elif 'student' in command:
           #      run2()
           #  break