import unittest
import socket
import threading

def run_fake_server(self):
    # Run a server to listen for a connection and then close it
    server_sock = socket.socket()
    server_sock.bind(('127.0.0.1', 7777))
    server_sock.listen(0)
    server_sock.accept()
    server_sock.close()

def test_client_with_fake_server(self):
    server_thread = threading.Thread(target=self.run_fake_server)
    cli