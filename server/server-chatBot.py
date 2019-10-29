#!/usr/bin/env python3
import socket
import sys
import collections
import time
import queue
import threading
import logging

from threading import Thread
from socketserver import ThreadingMixIn
from datetime import datetime

import serverSettings as settings
import brain as brain


class ClientThreadRead(Thread):

    def __init__(self, socket, ip, port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port

    def run(self):
        print("Thread ready at {}:{}\n".format(self.ip, self.port))
        while True:
            try:
                userInput = self.socket.recv(2048).decode('utf-8')
                print("{} | User-{}: {}".format(self.getCurrentDate(),
                                                self.socket.fileno(), userInput))
                lock.acquire()
                sendqueues[self.socket.fileno()].put(userInput)
                lock.release()
                if userInput == 'exit':
                    print('Read: Client ended sessions')
                    sys.exit()
            except:
                pass

    def getCurrentDate(self):
        return datetime.now().strftime("%d/%m/%Y_%H:%M:%S")


class ClientThreadWrite(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        self.logfilePath = ''

    def run(self):
        writeSocket.listen(1)
        (connection, (ip, port)) = writeSocket.accept()
        connection.sendall(str.encode(settings.WELCOME_MESSAGE))
        self.createLogfile(ip)

        while True:
            try:
                lock.acquire()
                userInput = sendqueues[self.socket.fileno()].get(False)
                lock.release()
                self.addToLogfile('User', userInput)
                if userInput == 'exit':
                    print('Write: Client ended sessions')
                    self.endLogfile()
                answer = brain.chat(userInput)
                self.addToLogfile('Bot', answer)
                connection.send(answer.encode('utf-8'))
            except queue.Empty:
                userInput = "none"
                lock.release()
                time.sleep(2)
            except KeyError:
                pass
            except:
                pass
        print("Chat thread ended")
        self.endLogfile()

    def createLogfile(self, ip):
        START_TIME = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        FILE_NAME = '{}_{}.txt'.format(START_TIME, ip.replace('.', ''))
        self.logfilePath = 'chatBot/server/logs/{}'.format(FILE_NAME)
        logging.basicConfig(filename=self.logfilePath, level=logging.INFO, format='%(message)s')
        logging.info('Start time: {}'.format(START_TIME))

    def addToLogfile(self, speaker, message):
        logging.info('{}: {}'.format(speaker, message))

    def endLogfile(self):
        END_TIME = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        logging.info('End time: {}'.format(END_TIME))
        sys.exit()


lock = threading.Lock()

sendqueues = {}

readSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
readSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
readSocket.bind(('', settings.TCP_PORT_READ))

writeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writeSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
writeSocket.bind(('', settings.TCP_PORT_WRITE))


threads = []
while True:
    readSocket.listen(6)
    print("Waiting for incoming connections on {}:{}\n".format(
        settings.TCP_IP, settings.TCP_PORT_READ))
    (connection, (ip, port)) = readSocket.accept()

    lock.acquire()
    sendqueues[connection.fileno()] = queue.Queue()
    lock.release()

    print("New thread with fileno:{}".format(connection.fileno()))

    readThread = ClientThreadRead(connection, ip, port)
    readThread.daemon = True
    readThread.start()

    writeThread = ClientThreadWrite(connection)
    writeThread.daemon = True
    writeThread.start()

    threads.append(readThread)
    threads.append(writeThread)

for t in threads:
    t.join()
    print(">>>>>>>>>> END <<<<<<<<<<")
