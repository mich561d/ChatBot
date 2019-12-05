import unittest
import socket
import threading

from client_chatBot import ServerThreadRead, ServerThreadWrite
import time
import clientSettings as settings

def run_fake_server(self):
    # Run a server to listen for a connection and then close it
    readSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    readSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    readSocket.bind(('', settings.TCP_PORT_READ))
    readSocket.listen(6)
    readSocket.accept()


def test_client_with_fake_server(self):
    self.run_fake_server()
    readSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    readSocket.connect((settings.TCP_IP, settings.TCP_PORT_WRITE))

    threadRead = ServerThreadWrite(readSocket)
    threadRead.daemon = True
    threadRead.start()