import pandas as pd
from pathlib import Path
import sqlalchemy

# Assign directory
directory = 'C:\\Users\\Landon\\Python Projects\\bitfocus\\files'

# Iterate over csv files. Create dataframes and load with engine.
files = Path(directory).glob('*.csv')

for file in files:
    bf_df = pd.read_csv(file,index_col=False)
    # gets file name from full file path
    file_name = Path(file).stem
    # Insert DataFrame into db. If table exists -> replace table
        # credentials should be environmental variables regarding best practice.
        # If engine is not passed in the loop to_sql() will timeout.
    engine = sqlalchemy.create_engine("mysql+mysqlconnector://perkins:perkins@45.79.53.180:3306/bitfocus_perkins")
    bf_df.to_sql(file_name, con= engine,chunksize= 1000, method= 'multi', if_exists= 'replace',index=False)