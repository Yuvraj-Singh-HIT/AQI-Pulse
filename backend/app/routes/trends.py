from fastapi import APIRouter
from app.services.forecast_service import generate_pm25_forecast
from app.services.trend_service import generate_trend_data

router = APIRouter(prefix="/trends", tags=["Trends"])

@router.get("/")
def trends(horizon: str = "24h"):
    timestamps, pm25 = generate_pm25_forecast(horizon)
    return generate_trend_data(pm25, timestamps, horizon)
