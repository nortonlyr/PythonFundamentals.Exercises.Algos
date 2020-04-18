import unittest
import binary_search_Algo

class test_binary_search_Algo(unittest.TestCase):

    def test_number_value(self):
        self.assertEqual(5, binary_search_Algo.binary_search([2, 3, 4, 6, 7, 9, 12, 14, 15, 16], 9))
        self.assertEqual(2, binary_search_Algo.binary_search([-20, -13, 2, 6, 7, 19, 22, 24, 35, 56], 2))
        self.assertEqual(11, binary_search_Algo.binary_search([0, 2, 5, 6, 7, 19, 22, 24, 35, 44, 59, 70, 100], 70))
