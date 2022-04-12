import sys,os, sqlite3

from interfaceQt import SigninWindow
from Functions import ChatWin
from users import Users
from styles import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QFrame, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *

# CALLBACKS IN SIGN IN WINDOW
# ---------------------------

class SignIn(SigninWindow):
    def __init__(self):
        SigninWindow.__init__(self)


    def move_window(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() == 16777216:     # esc key
            self.close()

    def save_data(self, data):
        """Create a database and insert specified data inside."""

        # CREATE DATA BASE
        try:
            connection = sqlite3.connect("ui.db")
            cursor = connection.cursor()

            print("Creating table...")
            cursor.execute("""CREATE TABLE IF NOT EXISTS uidb (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            code TEXT NOT NULL,
                            psw TEXT,
                            pic BLOB,
                            port INTEGER NOT NULL)""")

            print("Saving data...")
            cursor.execute("INSERT INTO uidb (name, code, psw, pic, port) VALUES (?, ?, ?, ?, ?)", data)

            # SAVE AND CLOSE CONNEXION
            print(f"Done.\nSigned in successfully as {data[0]}.")

            connection.commit()
            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Error while saving: {e}")

    def go_back(self):
        index = self.ui.stackedWidget.currentIndex()

        if index != 0: self.ui.stackedWidget.setCurrentIndex(index - 1)
        if index == 1: self.ui.return_button.hide()

    def chooseProfile(self, event):
        if event.button() == 1:

            if sys.platform == "win32":
                home = os.environ["USERPROFILE"]
            else:
                home = os.environ["HOME"]

            self.picture = QtWidgets.QFileDialog.getOpenFileName(self, "Profile picture", home, "Photos *.jpg *.PNG")
            directory = self.picture[0]
            if directory != "":

                # SET ICON TO LABEL
                self.ui.choose_profilepicture.setPixmap(QPixmap(directory))

                # CATCH BINARY
                with open(directory, "rb") as file:
                    self.picture = file.read()

    def check_data(self):
        """Verify if data where correctlly entered by the user in the signin window,
                in which case they ara saved in a database."""


        self.data = []
        server_port = ""

        ############# CHECK FORMULAR ###################

        # CHECK LINES EDIT
        for widget in self.ui.form.findChildren(QLineEdit):
            if not widget.text():
                widget.setStyleSheet(LineEdit.style_error)

            else:
                widget.setStyleSheet(LineEdit.style_normal)
                if widget.objectName() == "user_name":
                    user_name = self.ui.user_name.text()
                    self.data.append(user_name)

        # CHEK COMBO BOX
        if self.ui.code.currentIndex() == 0:
            self.ui.code.setStyleSheet(ComboBox.style_error)
        else:
            self.ui.code.setStyleSheet(ComboBox.style_normal)
            user_code = self.ui.code.currentText()
            self.data.append(user_code)
            server_port = Users.dictionnary.get(user_code)

        # CHECK IDENTICAL PASSWORDS
        if self.ui.passcode2.text() != self.ui.passcode.text():
            self.ui.passcode2.setStyleSheet(LineEdit.style_error)
        else:
            self.ui.passcode2.setStyleSheet(LineEdit.style_normal)
            passcode = self.ui.passcode2.text()
            self.data.append(passcode)

        # CHECK PROFILE PICTURE
        try:
            if self.picture:
                if type(self.picture) == bytes:
                    self.data.append(self.picture)
                else:
                    self.data.append(None)
        except AttributeError:
            self.data.append(None)

        # ASSIGN PORT
        self.data.append(server_port)

        # IF ALL DATA IS COLLECTED, GO TO THE NEXT PAGE
        if len(self.data) == 5:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.return_button.show()

    def confirm_subscription(self):

        if self.ui.iaggree.isChecked():
            self.save_data(self.data)
            self.ui.stackedWidget.setCurrentIndex(2)
            try:
                QTimer.singleShot(2900, lambda: self.ui.prev_feature.setStyleSheet(Features.prev))
                QTimer.singleShot(3000, lambda: self.ui.next_feature.setStyleSheet(Features.next))
            except Exception as e:
                print(e)
            self.ui.return_button.hide()


    def features(self, page):
        index = self.ui.what_isnew.currentIndex()

        if page == "Next":
            index += 1
            self.ui.what_isnew.setCurrentIndex(index)
            if self.ui.prev_feature.isHidden():
                self.ui.prev_feature.show()

            if index == 5:
                self.ui.next_feature.hide()

        elif page == "Previous":
            index -= 1
            self.ui.what_isnew.setCurrentIndex(index)
            if self.ui.next_feature.isHidden():
                self.ui.next_feature.show()

            if index == 0:
                self.ui.prev_feature.hide()
        else:
            index = page
            self.ui.what_isnew.setCurrentIndex(index)

            if index == 0:
                self.ui.prev_feature.hide()
                if self.ui.next_feature.isHidden(): self.ui.next_feature.show()

            elif index == 5:
                self.ui.next_feature.hide()
                if self.ui.prev_feature.isHidden(): self.ui.prev_feature.show()

            else:
                if self.ui.next_feature.isHidden(): self.ui.next_feature.show()
                if self.ui.prev_feature.isHidden(): self.ui.prev_feature.show()

        for range, w in enumerate(self.ui.current_feature.findChildren(QPushButton)):
            if range == index:
                w.setStyleSheet(Features.style_active)

            else:
                w.setStyleSheet(Features.style_inactive)

    def terminate(self):
        self.main = ChatWin()
        self.close()


# ============================================== SEE COMMAND RESULT ====================================================
# Run the app   -------  Just for trying
if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    run = SignIn()
    sys.exit(app.exec_())