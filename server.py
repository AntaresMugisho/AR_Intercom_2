# -*- coding:utf-8 -*-

import os, sys, time
import socket
import select

from PyQt5.QtCore import QObject, pyqtSignal

from users import Users

class Server(QObject):
    """Class server to listen, accept connections and receive messages."""

    # Signals will outsent when receiving messages to
    new_message = pyqtSignal()
    new_file = pyqtSignal()

    # Creating setters
    def set_usercode(self, code: str):
        """Set the user code. Must be unique in same compagny."""
        self.user_code = code

    def set_port(self):
        """Create a server listening port according to the user code."""
        self.get_user_code()
        for x in Users.dictionnary.keys():
            if x == self.user_code:
                self.port = Users.dictionnary[x]

    # Creating getters des getters
    def get_user_code(self):
        """Returns the usercode."""
        return self.user_code

    # Creating socket
    def create_socket_server(self):
        """Create a socket as server and listen waiting for new connections."""

        global server_connection
        host = ""

        server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            server_connection.bind((host, self.port))

        except OSError:
            pass

        else:
            server_connection.listen(5)
            print(f"Server listening on port {self.port}.")

    # Accept connections and wait for messages
    def launch_server(self):
        """Accept connection if asked and call the 'receive_message' funtion to receive message."""

        # ONLINE CLIENTS LIST
        self.connected = []

        # MESSAGING CLIENT LIST
        self.readlist = []

        while True:
            waiters, wlist, xlist = select.select([server_connection], [], [], 0.50)

            # Accept connections
            for connection in waiters:
                connect_client, adress = connection.accept()
                self.connected.append(connect_client)

            # Receive message
            try:
                self.readlist, wlist, xlist = select.select(self.connected, [], [], 0.50)

            except select.error:
                # If 'connected' list is empty
                pass

            else:
                self.receive_message()

    def receive_message(self):
        """Receive message and send status report."""

        for client in self.readlist:

            # TRY TO RECEIVE MESSAGE
            try:
                self.received_message = client.recv(1024)

            except ConnectionError:
                # If this error occurs (probably ConnectionAbortedError) no message will be received.
                pass

            else:
                # TRY TO DECODE IT
                try:
                    self.received_message = self.received_message.decode("utf8")

                except UnicodeDecodeError:
                    # If this error occurs, it means the message is a media file. It's not a problem.
                    pass

                finally:
                    # SEND STATUS REPORT
                    received = "1"
                    self.confirm_reception = received.encode("utf8")

                    try:
                        client.send(self.confirm_reception)
                    except:
                        pass

                    try:
                        if self.received_message[1] == "S":
                            # EMIT NEW TEXT MESSAGE SIGNAL > TO SHOW GUI BUBBLE
                            self.new_message.emit()

                        elif self.received_message[1] == "B":
                            # IF MESSAGE IS NOT STRING, COLLECT MEDIA INFO THEN EMIT 'NEW FILE' SIGNAL > TO SHOW  BUBBLE

                            spliter = self.received_message[2:].split(",")
                            self.media_info = {"Kind": f"{spliter[0]}", "Size": f"{spliter[1]}",
                                               "Title": f"{spliter[2]}", "Extension": f"{spliter[3]}"}

                            # CHOOSE FOLDER WHERE TO SAVE FILE (BYTES) ACCORDING TO OS
                            if sys.platform == "win32":
                                home = os.environ["USERPROFILE"]
                            else:
                                home = os.environ["HOME"]

                            # Building folder / path
                            file_folder = self.media_info["Kind"].capitalize() + "s"
                            directory = f"{home}/Documents/AR Intercom/Media/{file_folder}/"

                            # Set file title
                            if self.media_info["Kind"] == "voice":
                                f_title = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}"
                                self.media_info["Extension"] = ".wav" if sys.platform == "darwin" else ".arv"
                            else:
                                f_title = self.media_info["Title"]

                            self.media_info["Title"] = f_title

                            # RECEIVE AND WRITE BLOB (MEDIA CONTENT)
                            file = open(f"{directory}{self.media_info['Title']}{self.media_info['Extension']}", "ab")

                            self.data = b""
                            while len(self.data) < int(self.media_info["Size"]):

                                blob = client.recv(10240)   # Receive  10Kb/transaction

                                file.write(blob)

                                self.data += blob

                            # When it's done close file and emit new file signal to show widget
                            file.close()
                            self.new_file.emit()

                    except IndexError:
                        pass

                    except Exception as e:
                        print("ERR166 SR: ", e)

    def close_server(self):
        server_connection.close()
# ===================================================== END ============================================================