from fastapi import APIRouter, Query
from app.rules.health_advisory_rules import get_all_health_advisories

router = APIRouter(prefix="/health-advisory", tags=["Health Advisory"])

@router.get("/")
def health_advisory(
    category: str = Query(..., description="AQI category e.g. Good, Moderate, Poor, Very Poor")
):
    return get_all_health_advisories(category)
