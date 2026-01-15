from fastapi import APIRouter
from app.services.forecast_service import generate_pm25_forecast
from app.utils.aqi_utils import pm25_to_aqi

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.get("/")
def forecast(horizon: str = "24h"):
    timestamps, pm25 = generate_pm25_forecast(horizon)
    forecast_data = []
    for i in range(len(timestamps)):
        aqi_value, aqi_category = pm25_to_aqi(pm25[i])
        forecast_data.append({
            "datetime": timestamps[i],
            "pm25": pm25[i],
            "aqi": aqi_value,
            "category": aqi_category
        })
    return forecast_data
