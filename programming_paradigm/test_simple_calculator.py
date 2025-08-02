import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0),  0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
        self.assertEqual(self.calc.add(10, -4), 6)
        self.assertEqual(self.calc.add(-10, 4), -6)
        self.assertEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertEqual(self.calc.add(-2.5, -0.5), -3.0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-3, -5), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertEqual(self.calc.subtract(-2.5, -1.5), -1.0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(10, 1), 10)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(-3, -2), 6)
        self.assertEqual(self.calc.multiply(-4, -1), 4)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2.0), -3.0)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(100, 4), 25.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(-15, -3), 5.0)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        self.assertEqual(self.calc.divide(5,0), None)

if __name__ == "__main__":
    unittest.main()