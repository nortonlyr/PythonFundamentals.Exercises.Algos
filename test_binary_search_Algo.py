import unittest
import binary_search_Algo

class test_binary_search_Algo(unittest.TestCase):

    def test_number_value(self):
        self.assertEqual(0, binary_search_Algo.binary_search([2, 3, 4, 6, 7, 9, 13, 14, 15, 16], 2))
        self.assertEqual(2, binary_search_Algo.binary_search([-20, -13, 2, 6, 7, 19, 22, 24, 35, 56], 2))
        self.assertEqual(11, binary_search_Algo.binary_search([0, 2, 55, 16, 7, 99, 22, 46, 35, 68, 59, 70, 100], 99))
        self.assertEqual(None, binary_search_Algo.binary_search([0, 2, 5, 6, 7, 19, 22, 24, 35, 44, 59, 70, 100], 101))
        with self.assertRaises(AssertionError):
            binary_search_Algo.binary_search([0, 2, 3.7, 5, 6, 7, 19, 22, 24], 6)
        with self.assertRaises(AssertionError):
            binary_search_Algo.binary_search([0, 2, 5, 6, 7, 19, 22, 24], 'b')
        with self.assertRaises(AssertionError):
            binary_search_Algo.binary_search([0, 2, 5, 6, 't', 19, 22, 24], 22)