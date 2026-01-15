import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from tensorflow.keras.models import load_model
import joblib
from app.core.config import MODEL_PATH, SCALER_PATH

# Load model and scaler once
model = None
scaler = None

def load_model_and_scaler():
    global model, scaler
    if model is None:
        model = load_model(MODEL_PATH)
    if scaler is None:
        scaler = joblib.load(SCALER_PATH)

def generate_pm25_forecast(horizon: str):
    load_model_and_scaler()

    # Determine forecast hours based on horizon
    if horizon == "24h":
        hours = 24
    elif horizon == "48h":
        hours = 48
    elif horizon == "72h":
        hours = 72
    else:
        hours = 24

    # Generate timestamps starting from current time
    start_time = datetime.now()
    timestamps = [(start_time + timedelta(hours=i)).strftime("%Y-%m-%d %H:%M") for i in range(hours)]

    # For demonstration, use dummy historical data (last 24 hours)
    # In a real scenario, this would come from a database or sensor
    historical_pm25 = np.array([150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0,
                               230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0,
                               310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0])

    # Scale the historical data
    historical_scaled = scaler.transform(historical_pm25.reshape(-1, 1))

    # Reshape for LSTM input (assuming model expects shape [batch_size, timesteps, features])
    # Assuming timesteps = 24
    input_sequence = historical_scaled[-24:].reshape(1, 24, 1)

    # Generate forecast
    forecast_scaled = model.predict(input_sequence)

    # Inverse transform to get actual PM2.5 values
    pm25 = scaler.inverse_transform(forecast_scaled.reshape(-1, 1)).flatten()

    # Ensure we have the right number of predictions
    if len(pm25) < hours:
        # If model predicts less, repeat or extrapolate
        pm25 = np.tile(pm25, hours // len(pm25) + 1)[:hours]
    elif len(pm25) > hours:
        pm25 = pm25[:hours]

    return timestamps, pm25.tolist()
