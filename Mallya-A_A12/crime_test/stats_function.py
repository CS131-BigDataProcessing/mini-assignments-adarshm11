import pandas as pd


def calculate_mean(df):
	
	if 'Vict Age' not in df.columns:
		raise ValueError('"Vict Age" does not exist in the dataframe.')

	return df['Vict Age'].mean()

def calculate_median(df):
	
	if 'Vict Age' not in df.columns:
		raise ValueError('"Vict Age" does not exist in the dataframe.')

	return df['Vict Age'].median()


