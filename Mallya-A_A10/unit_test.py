import unittest
from math_functions import power, divide
import math

class TestMathFunctions(unittest.TestCase):
	
	def testPower(self):
		self.assertEqual(power(2, 3), 8)
		self.assertEqual(power(5, 0), 1)
		self.assertEqual(power(4, -3), 1/64)
		self.assertEqual(power(-4, 3), -64)
		self.assertEqual(power(0, 3), 0)
		self.assertEqual(power(2, 1/2), math.sqrt(2))
		self.assertEqual(power(1/2, 2), 1/4)
		with self.assertRaises(ValueError):
			power(0, -3)
		
	def testDivide(self):
		self.assertEqual(divide(10, 4), 5/2)
		self.assertEqual(divide(10, 2), 5)
		with self.assertRaises(ValueError):
			divide(10, 0)
		self.assertEqual(divide(0, 2), 0)
		self.assertEqual(divide(-10, 2), -5)
		self.assertEqual(divide(10, -2), -5)
		self.assertEqual(divide(-10, -2), 5)

if __name__ == '__main__':
	unittest.main()

	
