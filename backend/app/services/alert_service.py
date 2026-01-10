from app.utils.aqi_utils import pm25_to_aqi

def generate_alert(pm25_values, timestamps, horizon):
    aqi_values = []
    categories = []

    for v in pm25_values:
        aqi, cat = pm25_to_aqi(v)
        aqi_values.append(aqi)
        categories.append(cat)

    worst_aqi = max(aqi_values)
    idx = aqi_values.index(worst_aqi)

    return {
        "horizon": horizon,
        "worst_aqi": worst_aqi,
        "category": categories[idx],
        "peak_time": timestamps[idx],
        "message": f"Next {horizon} AQI is expected to be {categories[idx]} ({worst_aqi})."
    }
