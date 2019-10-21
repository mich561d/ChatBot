#!/usr/bin/env python3
import socket
import sys
import collections
import time
import queue
import threading

from threading import Thread
from socketserver import ThreadingMixIn

import serverSettings as settings


class ClientThreadWrite(Thread):

    def __init__(self, socket, ip, port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port

    def run(self):
        print("Thread ready for {}:{}\n".format(self.ip, self.port))
        self.socket.sendall(str.encode(settings.WELCOME_MESSAGE))

        while True:
            try:
                lock.acquire()
                userInput = sendqueues[self.socket.fileno()].get(False)
                lock.release()
                if userInput == 'exit':
                    break
                self.socket.send(userInput.encode('utf-8'))
            except queue.Empty:
                userInput = "none"
                time.sleep(2)
            except KeyError:
                pass
            except:
                pass
        print("Chat thread ended")
        sys.exit()


class ClientThreadRead(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

    def run(self):
        readSocket.listen(1)
        while True:
            userInput = readSocket.recv(2048)
            print(userInput)
            lock.acquire()
            sendqueues[self.socket.fileno()].push(userInput.decode('utf-8'))
            lock.release()


lock = threading.Lock()

sendqueues = {}

writeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writeSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
writeSocket.bind(('', settings.TCP_PORT_WRITE))

readSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
readSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
readSocket.bind(('', settings.TCP_PORT_READ))


threads = []
while True:
    writeSocket.listen(6)
    print("Waiting for incoming connections on {}:{}\n".format(
        settings.TCP_IP, settings.TCP_PORT_WRITE))
    (connection, (ip, port)) = writeSocket.accept()

    lock.acquire()
    sendqueues[readSocket.fileno()] = queue.Queue()
    lock.release()

    print("New thread with fileno:{}".format(readSocket.fileno()))

    writeThread = ClientThreadWrite(connection, ip, port)
    writeThread.daemon = True
    writeThread.start()

    readThread = ClientThreadRead(connection)
    readThread.daemon = True
    readThread.start()

    threads.append(writeThread)
    threads.append(readThread)

for t in threads:
    t.join()
    print(">>>>>>>>>> END <<<<<<<<<<")
