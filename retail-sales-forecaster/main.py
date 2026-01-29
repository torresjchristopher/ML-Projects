from src.preprocessing import load_data, add_features
from src.model import train_prophet, make_future
from src.evaluation import evaluate_model

df = load_data("data/sales.csv")
df = add_features(df)

model = train_prophet(df)
forecast = make_future(model)

print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
