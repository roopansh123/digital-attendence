# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString("HH:mm:ss")
        self.label_3.setText(text)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 475)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label.setStyleSheet("background-image: url(:/gui/black bg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(290, 100, 301, 150))
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(110, -16, 120, 60))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(180, 240, 481, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 100, 281, 101))
        self.label_2.setStyleSheet("background-image: url(:/gui/background2.png);\n"
"border-radius:10px;\n"
"background-position:center;\n"
"background-repeat:no-repeat;\n"
"border:5px solid white;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 110, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        timer = QtCore.QTimer(Form)
        timer.timeout.connect(self.setTime)
        timer.start(1000)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Say \"ACTIVATE\""))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:30pt;\">10:10:10</span></p></body></html>"))
import gui1_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


