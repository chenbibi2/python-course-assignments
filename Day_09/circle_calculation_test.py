import unittest
import 
import math

class TestMath(unittest.TestCase):
    def test_math(self):
        self.assertEqual(circle_calculation.calculate_area(2), 12.56637061)

    def test_more_math(self):
        self.assertEqual(circle_calculation.calculate_circumference(1),6.283185307)
