from fastapi import APIRouter
from app.services.forecast_service import generate_pm25_forecast
from app.services.alert_service import generate_alert

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/")
def alerts(horizon: str = "24h"):
    timestamps, pm25 = generate_pm25_forecast(horizon)
    return generate_alert(pm25, timestamps, horizon)
