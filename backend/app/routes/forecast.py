from fastapi import APIRouter
from app.services.forecast_service import generate_pm25_forecast

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.get("/")
def forecast(horizon: str = "24h"):
    timestamps, pm25 = generate_pm25_forecast(horizon)
    return {"horizon": horizon, "timestamps": timestamps, "pm25": pm25}
