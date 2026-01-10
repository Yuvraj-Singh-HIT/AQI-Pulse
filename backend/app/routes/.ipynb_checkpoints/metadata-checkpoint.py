from fastapi import APIRouter
from app.core.config import PROJECT_NAME, DATA_PERIOD, LAST_UPDATED, DATA_SOURCE

router = APIRouter(prefix="/metadata", tags=["Metadata"])

@router.get("/")
def metadata():
    return {
        "project": PROJECT_NAME,
        "data_period": DATA_PERIOD,
        "last_updated": LAST_UPDATED,
        "source": DATA_SOURCE
    }
