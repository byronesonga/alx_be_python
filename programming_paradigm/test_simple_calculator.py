import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):

        """Test the addition method."""
        self.assertEqual(self.calc.add(2,3),5)

    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(4,2),2)

    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(5,5),25)
    
    def test_division(self):
        """Test the division method"""
        self.assertEqual(self.calc.divide(10,5),2)
    
    def test_zero_division(self):
        """Test zero division"""
        self.assertEqual(self.calc.divide(int,0),None)


if __name__ == "__main__":
    unittest.main()