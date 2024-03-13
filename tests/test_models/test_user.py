
"""UNITTEST USER"""

import unittest
from models.user import User

usr = User()


class TestUser(unittest.TestCase):
    """UNITTEST FOR USER TEST"""

    def test_email(self):
        """UNITEST EMAIL"""
        self.assertTrue(type(usr.email) is str)

    def test_password(self):
        """UNITTEST PASSWORD"""
        self.assertTrue(type(usr.password) is str)

    def test_first_name(self):
        """UNITTEST FIRST NAME"""
        self.assertTrue(type(usr.first_name) is str)

    def test_last_name(self):
        """UNITTEST LAST NAME"""
        self.assertTrue(type(usr.last_name) is str)


if __name__ == '__main__':

    unittest.main()
