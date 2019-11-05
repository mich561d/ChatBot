#!/usr/bin/env python3
import socket
import sys
import collections
import time
import queue
import threading
import logging
import traceback

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
        self.errorLogger = None

    def run(self):
        print('Thread ready at {}:{}\n'.format(self.ip, self.port))
        while True:
            try:
                userInput = self.socket.recv(2048).decode('utf-8')
                print('{} | User-{}: {}'.format(datetime.now().strftime('%d/%m/%Y-%H:%M:%S'),
                                                self.socket.fileno(), userInput))
                lock.acquire()
                sendqueues[self.socket.fileno()].put(userInput)
                lock.release()
                if userInput == 'exit':
                    print('Read: Client ended sessions')
                    sys.exit()
            except Exception:
                if self.errorLogger == None:
                    self.errorLogger = setup_logger(level=logging.ERROR)
                self.errorLogger.exception('Read | {} | {}'.format(self.ip, self.socket.fileno()))
                sys.exit()


class ClientThreadWrite(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        self.chatLogger = None
        self.errorLogger = None

    def run(self):
        writeSocket.listen(1)
        (connection, (ip, port)) = writeSocket.accept()
        self.create_log_file(ip)
        self.add_to_log_file('Bot', settings.WELCOME_MESSAGE)
        connection.sendall(str.encode(settings.WELCOME_MESSAGE))
        while True:
            try:
                lock.acquire()
                userInput = sendqueues[self.socket.fileno()].get(False)
                lock.release()
                self.add_to_log_file('User', userInput)
                if userInput == 'exit':
                    print('Write: Client ended sessions')
                    self.end_log_file()
                answer = brain.chat(userInput)
                self.add_to_log_file('Bot', answer)
                connection.send(answer.encode('utf-8'))
            except queue.Empty:
                userInput = 'none'
                lock.release()
                time.sleep(2)
            except Exception:
                if self.errorLogger == None:
                    self.errorLogger = setup_logger(level=logging.ERROR)
                self.errorLogger.exception('Write | {} | {}'.format(ip, connection.fileno()))
                self.end_log_file()
        print('Chat thread ended')
        self.end_log_file()

    def create_log_file(self, ip):
        START_TIME = datetime.now()
        FILE_NAME = '{}_{}_{}.txt'.format(START_TIME.strftime(
            '%d-%m-%Y_%H-%M-%S'), ip.replace('.', ''), self.socket.fileno())
        FILE_PATH = 'logs/{}'.format(FILE_NAME)
        self.chatLogger = setup_logger(name=FILE_NAME.replace('.txt', ''), log_file=FILE_PATH)
        self.chatLogger.info('Start: {}'.format(
            START_TIME.strftime('%d/%m/%Y %H:%M:%S')))
        self.chatLogger.info('--------------------------')

    def add_to_log_file(self, speaker, message):
        TIME = datetime.now().strftime('%H:%M:%S')
        self.chatLogger.info('{} | {}: {}'.format(TIME, speaker, message))

    def end_log_file(self):
        END_TIME = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.chatLogger.info('--------------------------')
        self.chatLogger.info('End: {}'.format(END_TIME))
        sys.exit()


def setup_logger(name='error_log', log_file='error_log.txt', level=logging.INFO):
    formatter = None
    if name == 'error_log':
        formatter = logging.Formatter('\n%(asctime)s | %(message)s')
    else:
        formatter = logging.Formatter('%(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


lock = threading.Lock()

sendqueues = {}

readSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
readSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
readSocket.bind(('', settings.TCP_PORT_READ))

writeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writeSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
writeSocket.bind(('', settings.TCP_PORT_WRITE))

connectionLogger = setup_logger()

threads = []
while True:
    readSocket.listen(6)
    print('Waiting for incoming connections on {}:{}\n'.format(
        settings.TCP_IP, settings.TCP_PORT_READ))
    (connection, (ip, port)) = readSocket.accept()

    lock.acquire()
    sendqueues[connection.fileno()] = queue.Queue()
    lock.release()

    connectionLogger.info('A connection was made | {} | {}'.format(ip, connection.fileno()))
    print('New thread with fileno:{}'.format(connection.fileno()))

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
    print('>>>>>>>>>> END <<<<<<<<<<')
