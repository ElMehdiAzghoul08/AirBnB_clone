#!/usr/bin/python3
""" UNITTEST """

import unittest
from models.city import City

city = City()


class TestCity(unittest.TestCase):
    """ UNITTEST FOR CITY"""

    def test_state_id(self):
        """ UNITTEST FOR STATE ID """
        self.assertTrue(type(city.state_id) is str)

    def test_name(self):
        """ UNITTEST FOR NAME """
        self.assertTrue(type(city.name) is str)


if __name__ == '__main__':

    unittest.main()
