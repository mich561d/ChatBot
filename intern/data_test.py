import unittest

from os import path
from data_generator import generate_single_data

class test(unittest.Testcase):

    def test_name_is_not_null(self):
        data = generate_single_data(2019, 5, 20)
        self.assertTrue(data)

    # def test_if_brain_data_excist(self):
    #     self.assertTrue(path.exists('../server/intents.json'))

    # def run_fake_server(self):
    #     # Run a server to listen for a connection and then close it
    #     server_sock = socket.socket()
    #     server_sock.bind(('127.0.0.1', 7777))
    #     server_sock.listen(0)
    #     server_sock.accept()
    #     server_sock.close()

    # def test_client_with_fake_server(self):
    #     server_thread = threading.Thr

if __name__ == '__main__':
    unittest.main()