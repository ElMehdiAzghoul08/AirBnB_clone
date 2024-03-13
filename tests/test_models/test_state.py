""" UNITTEST STATE """

import unittest
from models.state import State

state = State()


class TestState(unittest.TestCase):
    """ UNITTEST STATE"""

    def test_name(self):
        """ UNITTEST NAME """
        self.assertTrue(type(state.name) is str)


if __name__ == '__main__':

    unittest.main()
