#!/usr/bin/python3
"""UNITTEST FOR AMENITY *"""

import unittest
from models.amenity import Amenity

amenity = Amenity()


class TestAmenity(unittest.TestCase):
    """ UNITTEST TESTCASE * """

    def test_name(self):
        """ UNITTEST NAME * """
        self.assertTrue(type(amenity.name) is str)


if __name__ == '__main__':

    unittest.main()
