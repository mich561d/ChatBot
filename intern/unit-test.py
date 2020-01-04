import unittest

# import intern.data_generator as data_generator

# from intern.data_generator import ip_generator
from data_generator import generate_single_data


class test_generate_single_data(unittest.TestCase):

    def test_name_is_not_null(self):
      data = generate_single_data(2019, 5, 20)
      self.assertTrue(data)


if __name__ == 'main':
    unittest.main()
