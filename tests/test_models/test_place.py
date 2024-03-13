"""UNITTEST FOR PLACE"""

import unittest
from models.place import Place

place = Place()


class TestPlace(unittest.TestCase):
    """UNITTEST FOR place.py"""

    def test_city_id(self):
        """UNITTEST FOR city.id"""
        self.assertTrue(type(place.city_id) is str)

    def test_user_id(self):
        """ UNITTEST FOR User id"""
        self.assertTrue(type(place.user_id) is str)

    def test_name(self):
        """ UNITTEST FOR NAME """
        self.assertTrue(type(place.name) is str)

    def test_description(self):
        """ UNITTEST FOR DESCRIPTION"""
        self.assertTrue(type(place.description) is str)

    def test_number_rooms(self):
        """UNITTEST FOR NOMBER OF ROOMS"""
        self.assertTrue(type(place.number_rooms) is int)

    def test_number_bathrooms(self):
        """UNITTEST BATHROOMS"""
        self.assertTrue(type(place.number_bathrooms) is int)

    def test_max_guest(self):
        """UNITTEST MAX GUEST"""
        self.assertTrue(type(place.max_guest) is int)

    def test_price_by_night(self):
        """UNITTEST NIGHT PRICE"""
        self.assertTrue(type(place.price_by_night) is int)

    def test_latitude(self):
        """UNITTEST LATITUDE"""
        self.assertTrue(type(place.latitude) is float)

    def test_longitude(self):
        """UNITTEST LONGITUDE"""
        self.assertTrue(type(place.longitude) is float)

    def test_amenity_ids(self):
        """UNITTEST AMENITY"""
        self.assertTrue(type(place.amenity_ids) is list)


if __name__ == '__main__':

    unittest.main()
