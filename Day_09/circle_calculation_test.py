import unittest
import circle_calculations 
import math

class TestMath(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_calculations.calculate_area(2), 12.56637061)

    def test_circumference(self):
        self.assertAlmostEqual(circle_calculations.calculate_circumference(1),6.283185307)

if __name__ == "__main__":
    unittest.main()
