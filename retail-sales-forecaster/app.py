import streamlit as st
import pandas as pd
from src.preprocessing import load_data
from src.model import train_prophet, make_future

st.title("📈 Retail Sales Forecaster")

uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.line_chart(df.set_index("date")["sales"])

    model = train_prophet(df)
    forecast = make_future(model, periods=30)

    st.subheader("Forecast for Next 30 Days")
    st.line_chart(forecast.set_index("ds")[["yhat"]])
