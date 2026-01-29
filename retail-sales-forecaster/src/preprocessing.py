import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'])
    df = df.sort_values('date')
    return df

def add_features(df):
    df['dayofweek'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['lag_1'] = df['sales'].shift(1)
    df['rolling_mean_7'] = df['sales'].rolling(window=7).mean()
    df = df.dropna()
    return df
