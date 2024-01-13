import os 
import pandas as pd
from sqlalchemy import create_engine


def fetch_data_from_db():
    # PostgreSQL ConnectionString
    server = 'localhost'
    database = '' #Need to set your database name filled with data to train the model.
    username = 'postgres' 
    password = os.getenv('DBpassword') #I personally like using the ENV variables of my host machine so for ease of use set DBpassword as your db password.

    # Create a connection string and engine
    connection_string = f"postgresql://{username}:{password}@{server}/{database}"
    engine = create_engine(connection_string)

    # SQL query
    query = "SELECT volume, to_char(to_timestamp(timestamp), 'YYYY-MM-DD HH24:MI:SS') AS formatted_timestamp FROM public.solana_historical_data"
    data = pd.read_sql(query, engine)
    return data
