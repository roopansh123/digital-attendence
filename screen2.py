from PyQt5 import QtCore, QtGui, QtWidgets
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import RPi.GPIO as GPIO
import smtplib
from mfrc522 import SimpleMFRC522
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel)
class Ui_page2(object):
    def window3(self):
        def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('sethicyberzone@gmail.com', 'Roop@1234')
            server.sendmail('sethicyberzone@gmail.com', to, content)
            server.close()

        reader = SimpleMFRC522()

        try:
            id, text = reader.read()
            print(id)
            print(text)
            content = "Hello"
            to = "krishchadha888@gmail.com"
            sendEmail(to, content)
            print("Email has been sent!")
        finally:
            GPIO.cleanup()

    def window2(self):

        # Initialize 'currentname' to trigger only when a new person is identified.
        currentname = "unknown"
        # Determine faces from encodings.pickle file model created from train_model.py
        encodingsP = "encodings.pickle"
        # use this xml file
        # https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
        cascade = "haarcascade_frontalface_default.xml"

        # load the known faces and embeddings along with OpenCV's Haar
        # cascade for face detection
        print("[INFO] loading encodings + face detector…")
        data = pickle.loads(open(encodingsP, "rb").read())
        detector = cv2.CascadeClassifier(cascade)

        # initialize the video stream and allow the camera sensor to warm up
        print("[INFO] starting video stream…")
        vs = VideoStream(src=0).start()
        # vs = VideoStream(usePiCamera=True).start()
        time.sleep(2.0)

        # start the FPS counter
        fps = FPS().start()

        # loop over frames from the video file stream
        while True:
            # grab the frame from the threaded video stream and resize it
            # to 500px (to speedup processing)
            frame = vs.read()
            frame = imutils.resize(frame, width=500)

            # convert the input frame from (1) BGR to grayscale (for face
            # detection) and (2) from BGR to RGB (for face recognition)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # detect faces in the grayscale frame
            rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                              minNeighbors=5, minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

            # OpenCV returns bounding box coordinates in (x, y, w, h) order
            # but we need them in (top, right, bottom, left) order, so we
            # need to do a bit of reordering
            boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

            # compute the facial embeddings for each face bounding box
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            # loop over the facial embeddings
            for encoding in encodings:
                # attempt to match each face in the input image to our known
                # encodings
                matches = face_recognition.compare_faces(data["encodings"],
                                                         encoding)
                name = "Unknown"  # if face is not recognized, then print Unknown

                # check to see if we have found a match
                if True in matches:
                    # find the indexes of all matched faces then initialize a
                    # dictionary to count the total number of times each face
                    # was matched
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    # determine the recognized face with the largest number
                    # of votes (note: in the event of an unlikely tie Python
                    # will select first entry in the dictionary)
                    name = max(counts, key=counts.get)

                    # If someone in your dataset is identified, print their name on the screen
                    if currentname != name:
                        currentname = name
                        print(currentname)

                # update the list of names
                names.append(name)

            # loop over the recognized faces
            for ((top, right, bottom, left), name) in zip(boxes, names):
                # draw the predicted face name on the image – color is in BGR
                cv2.rectangle(frame, (left, top), (right, bottom),
                              (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            .8, (255, 0, 0), 2)

            # display the image to our screen
            cv2.imshow("Facial Recognition is Running", frame)
            key = cv2.waitKey(1) & 0xFF

            # quit when 'q' key is pressed
            if key == ord("q"):
                break

            # update the FPS counter
            fps.update()

        # stop the timer and display FPS information
        fps.stop()
        print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()



    def setupUi1(self, page2):
        page2.setObjectName("page2")
        page2.resize(800, 480)
        self.label = QtWidgets.QLabel(page2)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.label.setStyleSheet("background-image: url(:/screen2img/new copy.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(page2)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 221, 251))
        self.label_2.setStyleSheet("background-image: url(:/screen2img/user.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(page2)
        self.label_3.setGeometry(QtCore.QRect(450, 100, 221, 221))
        self.label_3.setStyleSheet("background-image: url(:/screen2img/reports.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(page2)
        self.pushButton.setGeometry(QtCore.QRect(110, 350, 181, 31))
        self.pushButton.clicked.connect(self.window2
                                        )
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 26, 54);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(page2)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 350, 251, 31))
        self.pushButton_2.clicked.connect(self.window3)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(33, 14, 47);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(page2)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 781, 41))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi1(page2)
        QtCore.QMetaObject.connectSlotsByName(page2)

    def retranslateUi1(self, page2):
        _translate = QtCore.QCoreApplication.translate
        page2.setWindowTitle(_translate("page2", "page2"))
        self.pushButton.setText(_translate("page2", "Mark Attendance"))
        self.pushButton_2.setText(_translate("page2", "Check Attendance Reports"))
        self.label_4.setText(_translate("page2", "<html><head/><body><p><span style=\" font-weight:600;\">* Hello! Do you want to Mark Attendance or Check Attendance Reports ? * </span></p></body></html>"))
import screen2_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page2 = QtWidgets.QWidget()
    ui = Ui_page2()
    ui.setupUi1(page2)
    page2.show()
    sys.exit(app.exec_())
