import os

PROJECT_NAME = "AQI & PM2.5 Forecasting System"

DATA_PERIOD = {
    "start": "January 2022",
    "end": "December 2024"
}

LAST_UPDATED = "January 2026"

FORECAST_HORIZONS = ["24h", "48h", "72h"]

DATA_SOURCE = "CPCB (Central Pollution Control Board, India)"

# Model paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MODEL_PATH = os.path.join(BASE_DIR, "lstm_72hr.keras")
SCALER_PATH = os.path.join(BASE_DIR, "pm25_scaler.pkl")
