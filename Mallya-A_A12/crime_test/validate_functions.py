import pandas as pd

def load_csv(csv_file_path):
	
	try:
		return pd.read_csv(csv_file_path)

	except Exception as e:
		
		raise IOError(f'Could not load CSV file. Error: {e}')


def validate_vict_sex(df):

	if 'Vict Sex' not in df.columns:
		raise ValueError('"Vict Sex" does not exist in the dataframe.')

	column = df['Vict Sex']
	df = df[column.isin(['M', 'F'])]

	return df
	
def validate_vict_age(df):
		
	if 'Vict Age' not in df.columns:
		raise ValueError('"Vict Age" does not exist in the dataframe.')

	column = df['Vict Age']
		
	df = df[column.between(1, 100)]

	return df
