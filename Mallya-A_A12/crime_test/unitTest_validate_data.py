import unittest
from validate_functions import validate_vict_sex, validate_vict_age 
from stats_function import calculate_mean, calculate_median
import os
import pandas as pd


class TestCrimeDataFunctions(unittest.TestCase):
	
	def setUp(self):
		self.file_path = 'Crime_Data_from_2020_to_Present.csv'
		if not os.path.exists(self.file_path):
			raise FileNotFoundError(f'Error: could not find {self.file_path}.')
		
		self.dataframe = pd.read_csv(self.file_path)
		
	def test_validate_vict_sex(self):
		try:
			df = validate_vict_sex(self.dataframe)
			self.assertEqual(df['Vict Sex'].isnull().sum(), 0)
			self.assertTrue(all(df['Vict Sex'].isin(['M', 'F'])))	
		except ValueError:
			self.fail('Vict Sex could not be validated.')

	def test_validate_vict_age(self):
		try:
			df = validate_vict_age(self.dataframe)
			self.assertEqual(df['Vict Age'].isnull().sum(), 0)
			self.assertTrue(all(df['Vict Age'].between(1, 100)))
		except ValueError:
			self.fail('Vict Age could not be validated.')

	def test_calculate_mean(self):
		try:
			mean = calculate_mean(self.dataframe)
			self.assertTrue(mean > 0)
		
		except ValueError:
			self.fail('Error: Vict Age mean was not a valid value.')

	def test_calculate_median(self):
		try: 
			median = calculate_median(self.dataframe)
			self.assertTrue(median > 0)

		except ValueError:
			self.fail('Error: Vict Age median was not a valid value.')



if __name__ == '__main__':
	unittest.main()


