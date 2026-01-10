from app.utils.aqi_utils import pm25_to_aqi

def generate_trend_data(pm25_values, timestamps, horizon):
    aqi = []
    category = []

    for v in pm25_values:
        val, cat = pm25_to_aqi(v)
        aqi.append(val)
        category.append(cat)

    return {
        "horizon": horizon,
        "timestamps": timestamps,
        "pm25": pm25_values,
        "aqi": aqi,
        "category": category
    }
