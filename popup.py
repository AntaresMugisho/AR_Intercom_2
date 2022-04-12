# -*- coding: utf-8 -*-

# ============================================ POPUP RESULT BY PLYER ===================================================
import playsound
import threading, sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QFrame, QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import QTimer, Qt, QPropertyAnimation, QPoint
from PyQt5.QtGui import QColor

from popup_window import Ui_Popup_win

class Popup(QWidget):
    def __init__(self, sender):
        QWidget.__init__(self)
        self.pop = Ui_Popup_win()
        self.pop.setupUi(self)

        # SET WINDOW ICON
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/ARsoftlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # DROP SHADOW
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(255,0,0, 100))

        # Apply shadow
        self.pop.global_frame.setGraphicsEffect(shadow)

        # SET SENDER NAME
        self.sender_name = sender
        self.popup(self.sender_name)

    def play_sound(self):
        playsound.playsound('resources/3.wav')

    def popup(self, sender):
        self.show()

        # SET NOTIFICATION WINDOW POSITION
        desk = QDesktopWidget()
        qtrect = desk.screenGeometry()

        if sys.platform == "win32":
            self.move(qtrect.bottomRight().x() - 350, qtrect.bottomRight().y() - 160)
        else:
            self.move(qtrect.bottomRight().x() - 350, qtrect.topRight().y() + 40)

        self.pop.sender_name.setText(f"{self.sender_name} a à vous dire !")

        note1 = threading.Thread(target=self.play_sound)
        note1.start()

        QTimer.singleShot(3500, lambda: self.deleteLater())


# =============================================== SEE POPUP RESULT =====================================================
# Run module  -------  Just for

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    popup = Popup("Antares")
    sys.exit(app.exec())


# ===================================================== END ============================================================