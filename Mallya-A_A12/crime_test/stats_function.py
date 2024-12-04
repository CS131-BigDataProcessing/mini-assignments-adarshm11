import pandas as pd

def load_csv(csv_file_path):

        try:
                return pd.read_csv(csv_file_path)

        except Exception as e:

                raise IOError(f'Could not load CSV file. Error: {e}')



def calculate_mean(df):
	
	if 'Vict Age' not in df.columns:
		raise ValueError('"Vict Age" does not exist in the dataframe.')

	return df['Vict Age'].mean()

def calculate_median(df):
	
	if 'Vict Age' not in df.columns:
		raise ValueError('"Vict Age" does not exist in the dataframe.')

	return df['Vict Age'].median()


