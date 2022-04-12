# -*- coding:utf-8 -*-

# RESSOURCES FILE
from resources import img_rc

# Users list
from users import Users

import sys, os
from functools import partial

from PyQt5 import QtCore, QtGui, QtMultimedia
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *   # import of all widgets (QApplication, QLabel ...)
from PyQt5 import *
from PyQt5.QtGui import QColor
from PyQt5.QtMultimedia import *


#STYLES
from styles import *

#GUI FILES
from signinwindow import Ui_SigninWindow
from loginwindow import Ui_LoginWindow

#####################################################################

# SIGN IN WINDOW (from gui file)
# -------------------------------------------------------------

class SigninWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_SigninWindow()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 50))
        # Apply shadow
        self.setGraphicsEffect(self.shadow)

        # MOVE THE WINDOW
        self.ui.main_title.mouseMoveEvent = self.move_window

        # CONNECT CHOOSE PROFILE
        self.ui.choose_profilepicture.setToolTip("Définir une photo de profil (PRO)")
        # self.ui.choose_profilepicture.mousePressEvent = self.chooseProfile

        # CONNECT "NEXT" ADN "VALIDATE" BUTTON
        self.ui.next.clicked.connect(self.check_data)
        self.ui.validate.clicked.connect(self.confirm_subscription)

        # HIDE "BACK" BUTTON
        self.ui.return_button.clicked.connect(self.go_back)
        self.ui.return_button.hide()

        # INDICATE CURRENT FEATURE INDEX (0)
        self.ui.prev_feature.hide()
        self.ui.feature_0.setStyleSheet(Features.style_active)

        # CONNECT FEATURE BUTTONS AND HIDE THEM
        self.ui.next_feature.clicked.connect(partial(self.features, "Next"))
        self.ui.prev_feature.clicked.connect(partial(self.features, "Previous"))

        # Connect small indicators
        self.ui.feature_0.clicked.connect(partial(self.features, 0))
        self.ui.feature_1.clicked.connect(partial(self.features, 1))
        self.ui.feature_2.clicked.connect(partial(self.features, 2))
        self.ui.feature_3.clicked.connect(partial(self.features, 3))
        self.ui.feature_4.clicked.connect(partial(self.features, 4))
        self.ui.feature_5.clicked.connect(partial(self.features, 5))

        # CONNECT "TERMINATE" BUTTON
        self.ui.terminate.clicked.connect(self.terminate)

        # SHOW SIGNIN WINDOW
        self.show()

# LOG IN WINDOW (from gui file)
# -------------------------------------------------------------
class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # HIDE WARNINGS
        self.ui.name_warning.hide()
        self.ui.psw_warning.hide()

        self.ui.log_username.leaveEvent = self.check_username
        self.ui.log_password.leaveEvent = self.check_password

        self.ui.connect_log.clicked.connect(self.check_data)
        self.ui.connect_log.keyPressEvent = self.check_data

        # CHANGE ECHOMODE TO PREVIEW PASSWORD
        self.ui.toogle_button.enterEvent = lambda event: self.ui.log_password.setEchoMode(QLineEdit.Normal)
        self.ui.toogle_button.leaveEvent = lambda event: self.ui.log_password.setEchoMode(QLineEdit.Password)

        # SHOW LOGIN WINDOW
        #self.show()

# CHAT WINDOW (Main Window)
# -------------------------------------------------------------
class ChatWindow(LoginWindow):
    def __init__(self):

        # MAIN WINDOW
        self.MainWindow = QMainWindow()
        self.MainWindow.resize(690, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/ARsoftlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setWindowTitle("AR Intercom")

        # SHOW MAINWINDOW
        self.MainWindow.show()

        # DISPLAY THE MENU BAR
        self.menubar()

        # DISPLAY THE LOGIN WINDOW
        self.show_login_window()

    def menubar(self):
        """# STATUS BAR
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setStyleSheet("background-color: #000000; color:#ffffff;")
        self.MainWindow.setStatusBar(self.statusbar)"""

        # MENU BAR
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 26))
        #self.menubar.setStyleSheet("background:rgba(24, 53, 72, 250); color:white;")
        self.MainWindow.setMenuBar(self.menubar)

        # 1 MENU 'MENU'
        self.menuMenu = QtWidgets.QMenu("Menu")

        # ACTIONS
        self.actionAide = QtWidgets.QAction("Aide")
        self.actionAide.triggered.connect(lambda:self.help())
        self.actionQuitter = QtWidgets.QAction("Quitter")
        self.actionQuitter.triggered.connect(lambda:self._close())

        # ADD ACTIONS
        self.menuMenu.addAction(self.actionAide)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuitter)

        # ADD MENUS TO THE MENU BAR
        self.menubar.addAction(self.menuMenu.menuAction())

    def help(self):
        try:
            if sys.platform == "win32":
                os.startfile(f"{os.getcwd()}/resources/Help.pdf")
            else:
                os.system(f"open {os.getcwd()}/resources/Help.pdf")

        except Exception as e:
            print("Erreur 178INT: ", e)

    def _close(self):
        try:
            self.client.disconnect()
            self.server.close_server()
            self.player.stop()

        except Exception as e:
            print("Erreur 184GUI: ", e)

        finally:
            self.MainWindow.close()

    def show_login_window(self):
        self.MainWindow.setCentralWidget(self.ui.central_log)
        if sys.platform == "darwin":
            self.MainWindow.resize(690, 436)

    def show_chat_window(self):
        # SHOW CHAT WINDOW

        # Create a layout
        self.mainlay = QHBoxLayout()
        self.mainlay.setSpacing(0)
        self.mainlay.setContentsMargins(0, 0, 0, 0)

        # Create and set the central widget
        self.central_chat = QtWidgets.QWidget(self.MainWindow)
        self.central_chat.setLayout(self.mainlay)
        self.MainWindow.setCentralWidget(self.central_chat)

        # Create widgets
        self.show_left_side()
        self.show_right_side()

        # Layout widgets
        self.mainlay.addWidget(self.left_container)
        self.mainlay.addWidget(self.right_container)

    def show_left_side(self):

        # CONTAINER
        self.left_container = QtWidgets.QWidget(self.central_chat)
        self.left_container.setMinimumSize(QtCore.QSize(150, 250))
        self.left_container.setMaximumWidth(236)

        # Layout inside container
        self.layleft = QtWidgets.QVBoxLayout(self.left_container)
        self.layleft.setSpacing(3)
        self.layleft.setContentsMargins(0, 0, 0, 0)

        # WIDGETS______________________________

        # HEADER
        self.chatlist = QtWidgets.QLabel(self.left_container)
        self.chatlist.setMinimumSize(236, 41)
        self.chatlist.setStyleSheet("QLabel{color: rgb(255, 255, 255); background-color: rgb(0, 0, 59);"
                                    "font-size:20px; font-weight:bold; padding-left:10px;}")
        self.chatlist.setText("<p align='left'>Chat list</p>")

        # SCROLL REGION
        # Layout
        self.left_scroll_layout = QtWidgets.QVBoxLayout()
        self.left_scroll_layout.setSpacing(2)
        self.left_scroll_layout.setContentsMargins(0, 0, 0, 0)

        # Scroll widget
        self.left_scroll = QtWidgets.QWidget()
        self.left_scroll.setStyleSheet("QWidget{background-color:rgba(24, 53, 72, 250)}")
        self.left_scroll.setLayout(self.left_scroll_layout)

        # Scroll area
        self.clients_field = QtWidgets.QScrollArea(self.left_container)
        self.clients_field.setMinimumSize(236, 100)
        self.clients_field.setWidgetResizable(True)
        self.clients_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.clients_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.clients_field.setWidget(self.left_scroll)
        self.clients_field.setStyleSheet(ScrollBar.orange_style)

        # CLIENTS LIST
        self.load_client()

        # LAYOUT LEFT SIDE
        self.layleft.addWidget(self.chatlist)
        self.layleft.addWidget(self.clients_field)
       # ---------------------------------------client_frame

    def load_client(self):
        for client in Users.ulist:
            name = client

            # FRAME FOR ONE CLIENT
            self.client_info = QtWidgets.QFrame(self.left_scroll)
            self.client_info.setGeometry(QtCore.QRect(0, 0, 236, 60))
            self.client_info.setMinimumSize(QtCore.QSize(236, 60))
            self.client_info.setMaximumSize(QtCore.QSize(236, 60))
            self.client_info.setStyleSheet(Clients.frame_normal)
            self.client_info.setLineWidth(1)
            self.left_scroll_layout.addWidget(self.client_info, Qt.AlignCenter, Qt.AlignTop)

            # PROFILE PICTURE
            self.client_picture = QtWidgets.QLabel(self.client_info)
            self.client_picture.setGeometry(QtCore.QRect(3, 0, 60, 60))
            self.client_picture.setStyleSheet("image:url(:/icons/icons/1.png); border:none;background:none;")
            self.client_picture.setPixmap(QtGui.QPixmap(":/icons/icons/1.png"))
            self.client_picture.setScaledContents(True)

            # ONLINE TOAST
            self.online_toast = QtWidgets.QLabel(self.client_info)
            self.online_toast.setGeometry(QtCore.QRect(45, 11, 16, 16))
            self.online_toast.setStyleSheet("""QLabel{
                                            border:none;
                                            border-radius:8px;
                                            background-color: #00ff00;}""")
            self.online_toast.hide()
            self.online_toast.setObjectName(f"{name}_toast")

            # NAME
            self.client_name = QtWidgets.QPushButton(self.client_info)
            self.client_name.setGeometry(QtCore.QRect(56, 0, 175, 60))
            self.client_name.setStyleSheet("QPushButton{color:#FFF;font-size:20px; text-align:left; padding-left:10px;"
                                           "border:none;background:none;}")
            self.client_name.setText(name)
            self.client_name.clicked.connect(self.ask_connection)
            self.client_name.setObjectName(f"{name}_name")

            # MESSAGE COUNTER
            self.msg_counter = QtWidgets.QLabel(self.client_info)
            self.msg_counter.setGeometry(QtCore.QRect(184, 18, 22, 22))
            self.msg_counter.setStyleSheet("QLabel{border-radius:11px; font-weight:bold; text-align:right; color:#ffAa00;"
                                            "border:none; background-color: rgb(0, 0, 59);}")
            self.msg_counter.setText("0")
            self.msg_counter.setAlignment(Qt.AlignCenter)
            self.msg_counter.setFrameShadow(QtWidgets.QFrame.Raised)
            self.msg_counter.setObjectName(f"{name}_counter")
            self.msg_counter.hide()

####################################################################################
# THE LEFT SIDE IS DONE,
# LET'S DESIGN THE RIGHT SIDE NOW

    def show_right_side(self):

        # CONTAINER
        self.right_container = QtWidgets.QWidget()
        self.right_container.setMinimumSize(285, 200)

        # Layout inside container
        self.layright = QVBoxLayout(self.right_container)
        self.layright.setSpacing(0)
        self.layright.setContentsMargins(0, 0, 0, 0)

        # WIDGETS______________________________________________________________________
        # HEAD
        self.active_client_bg = QtWidgets.QFrame(self.right_container)
        self.active_client_bg.setMinimumSize(200, 51)
        self.active_client_bg.setMaximumHeight(51)
        self.active_client_bg.setStyleSheet("QFrame{background-color: rgba(0,0,0, 25);"
                                            "background-image: url(:/icons/icons/multilogo.png);"
                                            "background-repeat:repeat-x;}")
        self.layright.addWidget(self.active_client_bg)

        # MASSAGES CONTAINER
        self.create_chat_field()

        # ACTIVE CLIENT NAME
        self.active_client = QtWidgets.QLabel(self.right_container)
        self.active_client.setMinimumSize(80, 41)
        self.active_client.setMaximumHeight(41)
        self.active_client.setStyleSheet("QLabel{color: rgb(255, 255, 255);background: rgb(0, 0, 59);"
                                         "border-radius:20px; border:5px solid;border-color:rgb(0, 0, 59);"
                                         "border-bottom-color: rgb(255, 170, 0);font-size:20px; font-weight:Bold;"
                                         "image:none;}")
        self.active_client.setAlignment(Qt.AlignCenter)
        self.active_client.hide()

        # DELETE MESSAGES BUTTON
        self.delete_button = QtWidgets.QPushButton(self.right_container)
        self.delete_button.setFixedSize(31, 31)
        self.delete_button.setStyleSheet("QPushButton{image: url(:/icons/icons/24778-200.png);background:transparent;}"
                                 "QPushButton::hover{background-color:#55FFFFFF;")
        self.delete_button.clicked.connect(self.delete_message)
        self.delete_button.hide()

        tophlayout = QtWidgets.QHBoxLayout(self.active_client_bg)
        tophlayout.setContentsMargins(5, 10, 5, 0)

        tophlayout.addWidget(self.active_client)
        tophlayout.addStretch()
        tophlayout.addWidget(self.delete_button)

        # MESSAGE TYPING FIELD
        self.create_typing_zone()

    def create_chat_field(self):
        # WIDGET CONTAINING MESSAGES (SCROLL AREA)

        # Layout bubbles's frames
        self.layout_bubble = QtWidgets.QVBoxLayout()
        self.layout_bubble.setSpacing(10)
        self.layout_bubble.setContentsMargins(10, 15, 15, 10)

        # Widget for the scroll area object
        self.right_scroll = QtWidgets.QWidget()
        self.right_scroll.setLayout(self.layout_bubble)

        # Scroll area
        self.chat_field = QtWidgets.QScrollArea(self.right_container)
        self.chat_field.setMinimumSize(200, 30)
        self.chat_field.setWidgetResizable(True)
        self.chat_field.setStyleSheet(ScrollBar.blue_style)
        self.chat_field.setWidget(self.right_scroll)

        self.layright.addWidget(self.chat_field)

    def create_typing_zone(self):

        # CHOOSE MEDIA BUTTON (+) #######################################################

        def verify_style():
            if self.send_button.styleSheet() == SendButton.style_send:
                self.send_message()
                self.send_button.setStyleSheet(SendButton.style_record)

            elif self.send_button.styleSheet() == SendButton.style_record:
                self.record_voice()

        def change_media_style():
            # CONTROL MEDIA BUTTON STYLE
            if self.media_button.styleSheet() == MediaButton.style_more:
                self.show_media_buttons()

            else:
                self.media_button.setStyleSheet(MediaButton.style_more)
                self.media_bg.deleteLater()

        def change_send_style():
            if self.entry_field.text():
                # Change send button style
                self.send_button.setStyleSheet(SendButton.style_send)
                # Disable media button
                self.media_button.setEnabled(False)

            else:
                self.send_button.setStyleSheet(SendButton.style_record)
                self.media_button.setEnabled(True)

        # button
        self.media_button = QtWidgets.QPushButton(self.right_container)
        self.media_button.setFixedSize(40, 40)
        self.media_button.setStyleSheet(MediaButton.style_more)
        self.media_button.setToolTip("Envoyer un fichier (PRO)")
        self.media_button.clicked.connect(change_media_style)

        ##################################################################

        # TYPE TEXT MESSAGE FIELD
        self.entry_field = QtWidgets.QLineEdit(self.right_container)
        self.entry_field.setMinimumSize(225, 40)
        self.entry_field.setMaximumHeight(40)
        self.entry_field.setStyleSheet("QLineEdit{border:1px solid;padding-left:10px; padding-right:10px;"
                                       "border-color: rgb(0, 85, 255);border-radius:20px; font-size:20px;}"
                                       "QLineEdit:hover{border:2px solid #3385CC;}")
        self.entry_field.setFrame(True)
        self.entry_field.setPlaceholderText("Saisissez votre message ici !")
        self.entry_field.textEdited.connect(change_send_style)
        self.entry_field.returnPressed.connect(verify_style)

        # SEND MESSAGE BUTTON
        self.send_button = QtWidgets.QPushButton(self.right_container)
        self.send_button.setFixedSize(40, 40)
        self.send_button.setStyleSheet(SendButton.style_record)
        self.send_button.clicked.connect(verify_style)

        # Layout bottom widgets
        bottomhlayout = QtWidgets.QHBoxLayout()
        bottomhlayout.setSpacing(5)
        bottomhlayout.setContentsMargins(10, 5, 10, 5)

        bottomhlayout.addWidget(self.media_button)
        bottomhlayout.addWidget(self.entry_field)
        bottomhlayout.addWidget(self.send_button)

        self.layright.addLayout(bottomhlayout)

    def show_media_buttons(self):
        # LAYOUT
        self.media_layout = QtWidgets.QHBoxLayout()
        self.media_layout.setSpacing(2)
        self.media_layout.setContentsMargins(0, 0, 0, 0)

        # BACKGROUND
        self.media_bg = QtWidgets.QWidget(self.right_container)
        self.media_bg.setMinimumSize(168, 41)
        self.media_bg.move(self.media_button.x(), self.media_button.y() - 50)
        self.media_bg.setStyleSheet("QWidget{border-radius:20px; background-color: rgba(90, 162, 255, 90);}")
        self.media_bg.setLayout(self.media_layout)
        self.media_bg.show()

        # IMAGE BUTTON
        self.media_image = QtWidgets.QPushButton(self.media_bg)
        self.media_image.setMinimumSize(QtCore.QSize(40, 40))
        self.media_image.setStyleSheet("QPushButton{image: url(:/icons/icons/photo.png);border-radius:20px;}"
                                       "QPushButton:hover{border:1px solid #3385CC;}")
        self.media_image.setToolTip("Envoyer une image (PRO)")
        self.media_layout.addWidget(self.media_image)

        # MUSIC BUTTON
        self.media_music = QtWidgets.QPushButton(self.media_bg)
        self.media_music.setMinimumSize(QtCore.QSize(40, 40))
        self.media_music.setStyleSheet("QPushButton{image: url(:/icons/icons/song.png);border-radius:20px;}"
                                       "QPushButton:hover{border:1px solid #3385CC;}")
        self.media_music.setToolTip("Envoyer une musique (PRO)")
        self.media_layout.addWidget(self.media_music)

        # VIDEO BUTTON
        self.media_video = QtWidgets.QPushButton(self.media_bg)
        self.media_video.setMinimumSize(QtCore.QSize(40, 40))
        self.media_video.setStyleSheet("QPushButton{image: url(:/icons/icons/video.png);border-radius:20px;}"
                                       "QPushButton:hover{border:1px solid #3385CC;}")
        self.media_video.setToolTip("Envoyer une vidéo (PRO)")
        self.media_layout.addWidget(self.media_video)

        # DOCUMENT BUTTON
        self.media_doc = QtWidgets.QPushButton(self.media_bg)
        self.media_doc.setMinimumSize(QtCore.QSize(40, 40))
        self.media_doc.setStyleSheet("QPushButton{image: url(:/icons/icons/document.png);border-radius:20px;}"
                                     "QPushButton:hover{border:1px solid #3385CC;}")
        self.media_doc.setToolTip("Envoyer un document (PRO)")
        self.media_layout.addWidget(self.media_doc)

        self.media_button.setStyleSheet(MediaButton.style_less)

    def create_left_bubble(self, kind, title, format, content, time):

        # GRID LAYOUT
        self.left_msg_layout = QtWidgets.QGridLayout()
        self.left_msg_layout.setContentsMargins(0, 0, 0, 0)
        self.left_msg_layout.setHorizontalSpacing(0)
        self.left_msg_layout.setVerticalSpacing(3)

        # LEFT MESSAGE FRAME
        self.l_bubble_container = QtWidgets.QWidget()
        self.l_bubble_container.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.l_bubble_container.setLayout(self.left_msg_layout)

        self.layout_bubble.addWidget(self.l_bubble_container, Qt.AlignCenter | Qt.AlignBottom)

        # Small left bubble
        self.l_bubble = QtWidgets.QFrame()
        self.l_bubble.setFixedSize(16, 16)
        self.l_bubble.setStyleSheet("background-color: rgb(255, 170, 0);border-radius:7px;")
        self.left_msg_layout.addWidget(self.l_bubble, 0, 0, 1, 1, Qt.AlignTop)

        if kind == "string":
            # LAYOUT MESSAGE
            message = self.layout_message(content)

            # Left text container
            self.left_bubble = QtWidgets.QLabel()
            self.left_bubble.setMinimumWidth(110)
            self.left_bubble.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
            self.left_bubble.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
            self.left_bubble.setCursor(Qt.IBeamCursor)
            self.left_bubble.setText(message)
            self.left_bubble.setStyleSheet("border-radius:13px; color: rgb(0, 0, 0);background-color: rgb(255, 170, 0);"
                                           "padding-left:10px;padding-right:10px;padding-top:5px;padding-bottom:5px;"
                                           "font-size:16px;")
            self.left_msg_layout.addWidget(self.left_bubble, 0, 1, 1, 1)

        else:
            # CREATE THE MEDIA PARENT WIDGET
            self.left_media_parent = QtWidgets.QWidget()
            self.left_media_parent.setFixedSize(304, 73)
            self.left_media_parent.setStyleSheet("QWidget{border-radius:15px;"
                                                  "background-color: rgb(255, 170, 0);}")

            self.left_msg_layout.addWidget(self.left_media_parent, 0, 1, 1, 1)

            # Create media bubble
            self.create_media_bubble(self.left_media_parent, kind, title, format, content)

        # Left time bubble
        self.left_time = QtWidgets.QLabel()
        self.left_time.setFixedSize(90, 16)
        self.left_time.setText(f"<p align='center'>{time}</p>")
        self.left_time.setStyleSheet("QLabel{border-radius:8px; color:#000000; background-color:#C5C5C5;"
                                     "font-size:10px;}")
        self.left_msg_layout.addWidget(self.left_time, 1, 1, 1, 1, Qt.AlignHCenter)

        # UPDATE SCROLL BAR
        QTimer.singleShot(10, lambda: self.scroll_to_end())
        QTimer.singleShot(510, lambda: self.scroll_to_end())

    def create_right_bubble(self, kind, title, format, content, time, status):

        # GRID LAYOUT
        self.right_msg_layout = QtWidgets.QGridLayout()
        self.right_msg_layout.setContentsMargins(0, 0, 0, 0)
        self.right_msg_layout.setHorizontalSpacing(0)
        self.right_msg_layout.setVerticalSpacing(3)

        # RIGHT MESSAGE WIDGET (BUBBLE AND TIME CONTAINER)
        self.r_bubble_container = QtWidgets.QWidget()
        self.r_bubble_container.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.r_bubble_container.setLayout(self.right_msg_layout)
        self.r_bubble_container.setLayoutDirection(Qt.RightToLeft)
        self.r_bubble_container.setStyleSheet("background-color:99000000")

        self.layout_bubble.addWidget(self.r_bubble_container, Qt.AlignCenter, Qt.AlignBottom)

        # Small right bubble (design)
        self.r_bubble = QtWidgets.QFrame()
        self.r_bubble.setFixedSize(QtCore.QSize(16, 16))
        self.r_bubble.setStyleSheet("background-color:#3385CC; border-radius:8px;")
        self.right_msg_layout.addWidget(self.r_bubble, 0, 0, 1, 1, Qt.AlignBottom)

        # CREATE TEXT MESSAGE, OR MEDIA BUBBLE
        if kind == "string":
            message = self.layout_message(content)

            # Right text container
            self.right_bubble = QtWidgets.QLabel()
            self.right_bubble.setMinimumWidth(110)
            self.right_bubble.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
            self.right_bubble.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
            self.right_bubble.setCursor(Qt.IBeamCursor)
            self.right_bubble.setText(message)
            self.right_bubble.setStyleSheet("QLabel{border-radius:13px;color: rgb(255, 255, 255);"
                                            "background-color: #3385CC;padding-left:10px; padding-right:10px;"
                                            "padding-top:5px;padding-bottom:5px;font-size:16px;}")
            self.right_bubble.setObjectName("label_")
            self.right_msg_layout.addWidget(self.right_bubble, 0, 1, 1, 1)

        else:
            # CREATE THE MEDIA PARENT WIDGET
            # Set layout to the right bubble to prevent reversed progressbar
            ly = QtWidgets.QHBoxLayout()
            ly.setContentsMargins(0, 0, 0, 0)

            self.right_media_parent = QtWidgets.QWidget()
            self.right_media_parent.setFixedSize(304, 73)
            self.right_media_parent.setStyleSheet("QWidget{border-radius:15px;"
                                            "background-color: #3385CC;}")
            self.right_media_parent.setLayout(ly)
            self.right_media_parent.setLayoutDirection(Qt.LeftToRight)

            self.right_msg_layout.addWidget(self.right_media_parent, 0, 1, 1, 1)

            # Create media bubble
            self.create_media_bubble(self.right_media_parent, kind, title, format, content)

        # Right time
        self.right_time = QtWidgets.QLabel()
        self.right_time.setFixedSize(90, 16)
        self.right_time.setText(f"<p align='center'>{time}</p>")
        self.right_time.setStyleSheet("QLabel{border-radius:7px;color:#000000; background-color:#C5C5C5;"
                                      "font-size:10px;}")
        self.right_msg_layout.addWidget(self.right_time, 1, 1, 1, 1, Qt.AlignHCenter)

        # SHOW MESSAGE STATUS INDICATOR
        self.message_status = QtWidgets.QPushButton()
        self.message_status.setFixedSize(16, 16)
        self.message_status.setObjectName("buton_")

        if status:
            self.message_status.setStyleSheet(MessageStatus.style_sent)
        else:
            self.message_status.setStyleSheet(MessageStatus.style_not_sent)
            self.message_status.setToolTip("Cliquez pour renvoyer le message")
            self.message_status.clicked.connect(self.resend_message)

        self.right_msg_layout.addWidget(self.message_status, 1, 1, 1, 0)

        # UPDATE SCROLL BAR
        QTimer.singleShot(10, lambda: self.scroll_to_end())
        QTimer.singleShot(510, lambda: self.scroll_to_end())

    def scroll_to_end(self):
        # SCROLL TO END
        self.scroll_bar = self.chat_field.verticalScrollBar()
        self.scroll_bar.setValue(self.scroll_bar.maximum())

    def record_widget(self):
        # Frame
        self.record_tip = QtWidgets.QFrame(self.right_container)
        self.record_tip.setFixedSize(161, 31)
        self.record_tip.move(self.send_button.x() - 160, self.send_button.y()+5)
        self.record_tip.setStyleSheet("QFrame{background-color:#FFFFFF;border-radius:15px;}")
        self.record_tip.show()

        # Confirm end or record
        self.end_record = QtWidgets.QPushButton(self.record_tip)
        self.end_record.setGeometry(QtCore.QRect(10, 5, 31, 20))
        self.end_record.setToolTip("Finir l'enregistrement (PRO)")
        self.end_record.setStyleSheet("""QPushButton{background:#00FF00; border-top-left-radius:10px;
                                                    border-bottom-left-radius:10px;
                                                    image:url(:/cils/cils/cil-media-record-bl.png);}
                                        QPushButton:hover{background:#00DD00}""")
        self.end_record.show()

        # Time indicator
        self.record_time = QtWidgets.QLabel(self.record_tip)
        self.record_time.setGeometry(QtCore.QRect(45, 5, 71, 20))
        self.record_time.setStyleSheet("QLabel{background:grey; color:white; border-radius:none;}")
        self.record_time.setAlignment(QtCore.Qt.AlignCenter)
        self.record_time.setText("00:00")
        self.record_time.show()

        # Cancel record
        self.cancel_record = QtWidgets.QPushButton(self.record_tip)
        self.cancel_record.setGeometry(QtCore.QRect(119, 5, 31, 20))
        self.cancel_record.setToolTip("Annuler l'enregistrement (PRO)")
        self.cancel_record.setStyleSheet("""QPushButton{background:#FF0000;border-top-right-radius:10px;
                                                        border-bottom-right-radius:10px;
                                                        image:url(:/cils/cils/cil-media-stop-bl.png);}
                                        QPushButton:hover{background:#DD0000;}""")
        self.cancel_record.show()

    def create_voice_bubble(self, parent, title):

        def play_state():
            """Create attribute player if not exists and play.
                Else, pause or play Media or start playing an other media according to the sender
                object name"""

            sender = self.sender()
            try:
                if sender.objectName() == "np":
                    if sender.styleSheet() == Player.pause:
                        self.player.pause()

                    else:
                        self.player.play()
                else:
                    sender.setObjectName("np")
                    self.play_voice()

            except AttributeError:
                self.play_voice()

        # Frame
        self.voice_bubble = QtWidgets.QFrame(parent)
        self.voice_bubble.setGeometry(QtCore.QRect(2, 2, 300, 69))
        self.voice_bubble.setStyleSheet("QFrame{background-color:#88FFFFFF; border-radius:10px;}")

        # Title
        self.title = QtWidgets.QLabel(self.voice_bubble)
        self.title.setGeometry(QtCore.QRect(52, 3, 241, 20))
        self.title.setStyleSheet("QLabel{background:#44FFFFFF;}")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setText(title)
        self.title.setObjectName("media_")

        # Slider
        self.slider = QtWidgets.QSlider(self.voice_bubble)
        self.slider.setGeometry(QtCore.QRect(52, 30, 241, 12))
        self.slider.setStyleSheet(Slider.slider)
        self.slider.setMaximum(100)
        self.slider.setProperty("value", 0)
        self.slider.setSliderPosition(0)
        self.slider.setOrientation(QtCore.Qt.Horizontal)

        # Elapsed time
        self.elapsed_time = QtWidgets.QLabel(self.voice_bubble)
        self.elapsed_time.setGeometry(QtCore.QRect(52, 49, 51, 16))
        self.elapsed_time.setStyleSheet("QLabel{background:#22FFFFFF; border-radius:8px;}")
        self.elapsed_time.setText("00:00")
        self.elapsed_time.setAlignment(QtCore.Qt.AlignCenter)
        self.elapsed_time.setObjectName("elapsed_time")

        # Total time
        self.total_time = QtWidgets.QLabel(self.voice_bubble)
        self.total_time.setGeometry(QtCore.QRect(241, 49, 51, 16))
        self.total_time.setStyleSheet("QLabel{background:#22FFFFFF; border-radius:8px;}")
        self.total_time.setText("--:--")
        self.total_time.setAlignment(QtCore.Qt.AlignCenter)
        self.total_time.setObjectName("total_time")

        # Play button
        self.play_button = QtWidgets.QPushButton(self.voice_bubble)
        self.play_button.setGeometry(QtCore.QRect(7, 12, 41, 41))
        self.play_button.setStyleSheet(Player.play)
        self.play_button.setObjectName("play_button")
        self.play_button.clicked.connect(play_state)


# MAIN PROGRAMM
if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    run = ChatWindow()
    sys.exit(app.exec())