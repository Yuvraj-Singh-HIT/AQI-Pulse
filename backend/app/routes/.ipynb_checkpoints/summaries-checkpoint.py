from fastapi import APIRouter
from app.services.forecast_service import generate_pm25_forecast
from app.services.summary_service import generate_summary

router = APIRouter(prefix="/summaries", tags=["Summaries"])

@router.get("/")
def summaries(horizon: str = "24h"):
    timestamps, pm25 = generate_pm25_forecast(horizon)
    return generate_summary(pm25, timestamps, horizon)
