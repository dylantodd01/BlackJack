import unittest

from game import Card



class TestCardClass(unittest.TestCase):

    def setUp(self):
        self.card = Card("Red", "Spade", "A")

    def test_colour_getter_method(self):
        self.assertEquals("Red", self.card.get_colour())

if __name__ == '__main__':
    unittest.main()