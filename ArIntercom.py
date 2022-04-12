# -*- coding:utf-8 -*-

                                ######################################
                                ###   AR INTERCOM                  ###
                                ###   VERSION : 2.0                ###
                                ###   UPDATE  : 31-10-2021         ###
                                ###   LICENCE : FREE               ###
                                ###   DESIGNED AND EDITED BY       ###
                                ###   ===== ANTARES MUGISHO ====== ###
                                ###   COPYRIGHT 2021               ###
                                ######################################

# ============================================== MAIN PROGRAM FILE =====================================================
import sys, sqlite3

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFrame, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import *

from splash import Ui_SplashScreen
from FunctionsSL import SignIn
from Functions import ChatWin
from resources import img_rc

# GLOBALS
counter = 0

class SplashScreen(QWidget):
    """Shows splashscreen before launching app."""
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowTitle("AR Intercom 2.0")

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # DROP SHADOW
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 200))

        # Apply shadow
        self.ui.line.setGraphicsEffect(shadow)

        # PROGRESS START AT ZERO
        self.progressValue(0)

        # TIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # Timer in milliseconds
        self.timer.start(10)

        # CHANGE LOADING LABEL TEXT
        QtCore.QTimer.singleShot(1400, lambda: self.ui.loading.setText("Checking Network"))
        QtCore.QTimer.singleShot(2500, lambda: self.ui.loading.setText("Locating Database"))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.loading.setText("Preparing Server"))
        QtCore.QTimer.singleShot(4050, lambda: self.ui.loading.setText("Loading User Interface"))
        QtCore.QTimer.singleShot(4500, lambda: self.ui.loading.setText("Launching"))

        self.show()

    def connect_database(self):

        # CONNECT TO DATA BASE
        try:
            connection = sqlite3.connect("ui.db")
            cursor = connection.cursor()

            i = str(1)
            cursor.execute("SELECT * FROM uidb WHERE id = ?", i)

            cursor.close()
            connection.close()

        except Exception as e:
            print(f"User registration required.")
            self.main = SignIn()

        else:
            self.main = ChatWin()


    def progressValue(self, value):
        style = """
        QFrame{
            border-radius:132px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} 
            rgba(250, 249, 251, 255), stop:{STOP_2} rgba(255, 0, 0, 255));}"""

        # GET PROGRESS BAR VALUE AND CONVERT TO FLOAT
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # GET NEW STYLESHEET
        stylesheet = style.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLE SHEET TO PROGRESS BAR
        self.ui.circular_progress.setStyleSheet(stylesheet)

    def progress(self):
        global counter
        value = counter

        # SET VALUE TO PROGRESS BAR

        # Fix value error if > 1.000
        if value >= 100 : value = 1.000
        self.progressValue(value)

        # CLOSE SPLASHSCREEN AND OPEN APP
        if counter > 100:
            # Stop timer
            self.timer.stop()

            # CLOSE SPLASH SCREEN
            self.close()

            # SHOW SIGN IN WINDOW OR LOGIN WINDOW
            self.connect_database()

        # INCREASE COUNTER
        counter += 0.2

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Comfortaa-Light.ttf')
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Comfortaa-Regular.ttf')
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Comfortaa-Bold.ttf')
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Kirvy-Light.otf')
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Kirvy-Regular.otf')
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Kirvy-Bold.otf')
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Montserrat-Light.otf')
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Montserrat-Regular.otf')
    QtGui.QFontDatabase.addApplicationFont('resources/fonts/Montserrat-Bold.otf')

    run = SplashScreen()
    sys.exit(app.exec())

# =========================================== ALL THANKS TO MY GOD =====================================================