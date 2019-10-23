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


class ClientThreadRead(Thread):

    def __init__(self, socket, ip, port):
        Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port

    def run(self):
        print("Thread ready at {}:{}\n".format(self.ip, self.port))
        while True:
            userInput = self.socket.recv(2048)
            print("input:"+userInput.decode('utf-8'))
            lock.acquire()
            sendqueues[self.socket.fileno()].push(userInput.decode('utf-8'))
            lock.release()


class ClientThreadWrite(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

    def run(self):
        writeSocket.listen(1)
        (connection, address) = writeSocket.accept()
        connection.sendall(str.encode(settings.WELCOME_MESSAGE))

        while True:
            try:
                lock.acquire()
                userInput = sendqueues[self.socket.fileno()].get(False)
                lock.release()
                if userInput == 'exit':
                    break
                connection.send(userInput.encode('utf-8'))
            except queue.Empty:
                userInput = "none"
                time.sleep(2)
            except KeyError:
                pass
            except:
                pass
        print("Chat thread ended")
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
