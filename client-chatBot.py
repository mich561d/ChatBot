#!/usr/bin/env python3
import sys
import socket
import time
import threading

from threading import Thread
from socketserver import ThreadingMixIn

import clientSettings as settings


class ServerThreadWrite(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        print("New thread started for write")

    def run(self):
        starttime = time.time()
        while True:
            # Welcome message
            print(self.socket.recv(settings.BUFFER_SIZE))
            clientInput = input("Hvad kan jeg gøre for dig med?: ")
            curtime = time.time()
            self.socket.send(clientInput)
            ack = self.socket.recv(settings.BUFFER_SIZE)
            print(ack)


class ServerThreadRead(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        print("New thread started for chat display")

    def run(self):
        welcomemsg = self.socket.recv(settings.BUFFER_SIZE)
        print(welcomemsg)

        chat = "initial"
        while True:
            chat = self.socket.recv(settings.BUFFER_SIZE)
            print(chat)
            time.sleep(5)


writeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writeSocket.connect((settings.TCP_IP, settings.TCP_PORT))

readSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
readSocket.connect((settings.TCP_IP, settings.TCP_PORT2))

threads = []
try:
    writeThread = ServerThreadWrite(writeSocket)
    writeThread.daemon = True

    readThread = ServerThreadRead(readSocket)
    readThread.daemon = True

    writeThread.start()
    readThread.start()

    threads.append(writeThread)
    threads.append(readThread)

    while True:
        for t in threads:
            t.join(600)
            if not t.isAlive():
                break
        break
except KeyboardInterrupt:
    clientInput = "logout"
    writeSocket.send(clientInput)
    sys.exit()
