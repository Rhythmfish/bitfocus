import pandas as pd
from pathlib import Path
import sqlalchemy
import mysql.connector as msql

# create sqlalchemy engine
# credentials should be environmental variables in best practice.
engine_url = "mysql+mysqlconnector://perkins:perkins@45.79.53.180:3306/bitfocus_perkins"
engine = sqlalchemy.create_engine(engine_url)

# Assign directory
directory = 'C:\\Users\\Landon\\Python Projects\\bitfocus\\files'

# Iterate over csv files. Create dataframes and load with engine.
files = Path(directory).glob('*.csv')

for file in files:
    bf_df = pd.read_csv(file,index_col=False)
    # gets file name from full file path
    file_name = Path(file).stem
    # Insert DataFrame into db. If table exists -> replace table
    bf_df.to_sql(file_name, con= engine,chunksize= 200, method= 'multi', if_exists= 'replace',index=False)