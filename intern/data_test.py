import unittest
import requests

from os import path
from data_generator import generate_single_data, ip_generator, generate_lines, get_country_from_ip

class test(unittest.TestCase):

    def test_name_is_not_null(self):
        data = generate_single_data(2019, 5, 20)
        self.assertTrue(data["user"]["name"])

    # def test_if_brain_data_excist(self):
    #     self.assertTrue(path.exists('../server/intents.json'))

    def test_ip_contains_numbers(self):
        ip = ip_generator()
        ip.split('.')
        self.assertTrue(ip[1])

    def test_generate_lines(self):
        lines = generate_lines(7)
        self.assertEqual(len(lines), 7)

    def test_generate_lines_exception(self):
        lines = generate_lines("nej")
        self.assertRaises(TypeError, lines)

    def test_get_country_from_ip(self):
        country = get_country_from_ip("5.179.80.204")
        self.assertTrue(country)

if __name__ == '__main__':
    unittest.main()