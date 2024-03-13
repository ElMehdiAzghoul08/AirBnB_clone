#!/usr/bin/python3
""" UNITTEST REVIEW """

import unittest
from models.review import Review

review = Review()


class TestReview(unittest.TestCase):
    """UNITTEST REVIEW"""

    def test_place_id(self):
        """ UNITTEST PLACE ID """
        self.assertTrue(type(review.place_id) is str)

    def test_user_id(self):
        """ UNITTEST USER ID """
        self.assertTrue(type(review.user_id) is str)

    def test_text(self):
        """ UNITTEST TEXT """
        self.assertTrue(type(review.text) is str)


if __name__ == '__main__':

    unittest.main()
