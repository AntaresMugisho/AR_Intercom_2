# -*- coding: utf-8 -*-

import sys
import socket

class Client:
    """Class client to connect ask connections to servers and send messages."""

    # Class attribute to identifie usercode when sending a message
    prefix = ""

    def __init__(self, port):
        self.port = port

        # Setting the connection status at False by default
        self.online = False

    def connect_to_server(self):
        """Try to connect to a distant server to a specific port but an unknow IP's 4th bit."""
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # IP Attempts (192.168.1.[unkown])
        ips = (100, 101, 105, 106)
        ips = reversed(ips)

        for i in ips:
            self.hote = f"192.168.1.{str(i)}"

            #self.hote = "127.0.0.1" # Just for trying
            try:
                sock.connect((self.hote, self.port))
                print(f"Connected to host {self.hote} | Port: {self.port}")
                self.online = True  # The user will be informed by a small green widget
                break

            except ConnectionError:
                print(f"Can't connect to host {self.hote}\n")

            except TimeoutError:
                pass

            except OSError:
                pass

            except Exception as e:
                print("ERR46 CL: ", e)

    def send_message(self, kind, body):
        """Send message and try to receive status report."""

        if kind == "string":
            code = Client.prefix + "S"

            # SEND USER IDENTIFIER AND HIS TEXT MESSAGE THEN TRY TO GET SERVER RESPONSE
            text_message = (code + body).encode("utf8")
            try:
                sock.send(text_message)

            except Exception as e:
                # If an error occured here, it means message wasn't sent
                self.status = False
                print("ERR62 CL: ", e)

            else:
                # Else, it means message was sent and received
                self.status = sock.recv(1024).decode("utf8")
                print(f"Message received.")

        else:
            code = Client.prefix + "B"
            file_path = body

            # COLLECT MEDIA INFO FIRST
            with open(file_path, "rb") as file:
                content = file.read()

            size = str(len(content))
            extension = f".{str(file_path).split('.')[-1]}"
            title = str(file_path).split("/")[-1]
            title = title[:-len(extension)]
            media_info = f"{kind},{size},{title},{extension}"

            try:
                # SEND MEDIA INFORMATION
                informations = (code + media_info).encode("utf8")
                sock.send(informations)

            except Exception as e:
                # If an error occured here, it means media information message wasn't sent
                self.status = False
                print("ERR91 CL: ", e)

            else:
                # Else, it means media information message was sent and received, it's time to send media content
                self.status = sock.recv(1024).decode("utf8")

                # FINALLY SEND MEDIA
                sock.sendall(content)

    def disconnect(self):
        """Close the client socket."""
        sock.close()
# ===================================================== END ============================================================