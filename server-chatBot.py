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
        print("[+] Thread ready for "+ip+":"+str(port))
        while True:
            userInput = self.socket.recv(2048)
            if userInput == 'exit':
                break
            else:
                self.socket.send(userInput)
        print("Chat thread finished")
        sys.exit()


class ClientThreadRead(Thread):

    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock

    def run(self):
        tcpsock2.listen(1)
        (connection, address) = tcpsock2.accept()

        connection.sendall(str.encode(settings.WELCOME_MESSAGE))

        chat = "initial"
        print("ind here is")
        print(self.sock.fileno())
        while True:
            try:
                chat = sendqueues[self.sock.fileno()].get(False)
                print(chat)
                connection.send(chat)
            except queue.Empty:
                chat = "none"
                time.sleep(2)
            except KeyError:
                pass
            except:
                pass


lock = threading.Lock()

sendqueues = {}

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(('', settings.TCP_PORT))

tcpsock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock2.bind(('', settings.TCP_PORT2))

threads = []

while True:
    tcpsock.listen(6)
    print("Waiting for incoming connections on {}:{}\n".format(
        settings.TCP_IP, settings.TCP_PORT))
    (conn, (ip, port)) = tcpsock.accept()
    lock.acquire()
    sendqueues[conn.fileno()] = queue.Queue()
    lock.release()

    print("New thread with ", conn.fileno())

    writeThread = ClientThreadWrite(conn, ip, port)
    readThread = ClientThreadRead(conn)
    writeThread.daemon = True
    readThread.daemon = True
    writeThread.start()
    readThread.start()

    threads.append(writeThread)
    threads.append(readThread)

for t in threads:
    t.join()
    print("END")
