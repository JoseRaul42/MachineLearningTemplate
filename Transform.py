import os 
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas_ta as ta
from Extract import fetch_data_from_db


def prepare_data(data):
    # Convert datetime to more meaningful features
    data['timestamp'] = pd.to_datetime(data['formatted_timestamp'])
    data['hour'] = data['timestamp'].dt.hour
    data['day_of_week'] = data['timestamp'].dt.dayofweek

  import os 
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas_ta as ta
from Extract import fetch_data_from_db


def prepare_data(data):
    # Convert datetime to more meaningful features
    data['timestamp'] = pd.to_datetime(data['formatted_timestamp'])
    data['hour'] = data['timestamp'].dt.hour
    data['day_of_week'] = data['timestamp'].dt.dayofweek

    # 'volume' is the target
    y = data['volume']

    # Calculate lagged volume (e.g., previous hour)
    data['lagged_volume'] = data['volume'].shift(1)

    # Add more technical indicators here as needed
    # Example: Moving Average
    data['SMA_10'] = ta.sma(data['volume'], length=10)

    # Fill any NaN values
    data.bfill(inplace=True)

    # Features selection
    features = ['hour', 'day_of_week', 'lagged_volume', 'SMA_10']
    X = data[features]

    # Data splitting and scaling
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test



    y = data['volume']

    # Calculate lagged volume (e.g., previous hour)
    data['lagged_volume'] = data['volume'].shift(1)

    # Add more technical indicators here as needed
    # Example: Moving Average
    data['SMA_10'] = ta.sma(data['volume'], length=10)

    # Fill any NaN values
    data.bfill(inplace=True)

    # Features selection
    features = ['hour', 'day_of_week', 'lagged_volume', 'SMA_10']
    X = data[features]

    # Data splitting and scaling
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test


