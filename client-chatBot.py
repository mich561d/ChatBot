#!/usr/bin/env python3
import sys
import socket
import time
import threading

from threading import Thread
from socketserver import ThreadingMixIn

import clientSettings as settings


class ServerThreadRead(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

    def run(self):
        WELCOME_MESSAGE = self.socket.recv(settings.BUFFER_SIZE)
        print('{}: {}'.format(settings.BOT_NAME,WELCOME_MESSAGE))
        settings.accept_input = True
        chat = settings.WAITING
        while True:
            chat = self.socket.recv(settings.BUFFER_SIZE)
            print('{}: {}'.format(settings.BOT_NAME, chat))
            time.sleep(5)


class ServerThreadWrite(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

    def run(self):
        while True:
            while settings.accept_input:
                clientInput = input('{}: '.format(settings.USER_NAME))
                self.socket.send(str.encode(clientInput))


readSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
readSocket.connect((settings.TCP_IP, settings.TCP_PORT))
writeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writeSocket.connect((settings.TCP_IP, settings.TCP_PORT2))

threads = []
try:
    writeThread = ServerThreadRead(readSocket)
    readThread = ServerThreadWrite(writeSocket)
    writeThread.daemon = True
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
    clientInput = 'exit'
    print(settings.QUIT)
    writeSocket.send(clientInput)
    sys.exit()
