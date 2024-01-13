import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from datetime import datetime

# Your PostgreSQL connection details
server = 'localhost'
database = 'SolanaHistorical' #for ease of use with this test data please name your database you will be working with SolanaHistorical.
username = 'postgres'  # Replace with your actual PostgreSQL username
password = os.getenv('DBpassword')  # Replace with your actual PostgreSQL password or ENV variable.

# Create a connection string and engine
connection_string = f"postgresql://{username}:{password}@{server}/{database}"
engine = create_engine(connection_string)


# Construct the file path with today's date
file_path = rf"C:\Temp\Solana_Historical_Data.csv"

# Load data from CSV
df = pd.read_csv(file_path)

# Write data into the database
df.to_sql('solana_historical_data', engine, if_exists='replace', index=False)
