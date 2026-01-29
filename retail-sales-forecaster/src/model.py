from prophet import Prophet

def train_prophet(df):
    prophet_df = df.rename(columns={"date": "ds", "sales": "y"})
    model = Prophet()
    model.fit(prophet_df)
    return model

def make_future(model, periods=30):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
