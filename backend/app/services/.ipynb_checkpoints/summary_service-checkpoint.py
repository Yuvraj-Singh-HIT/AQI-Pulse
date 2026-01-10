from collections import Counter
from app.utils.aqi_utils import pm25_to_aqi

def generate_summary(pm25_values, timestamps, horizon):
    avg_pm25 = round(sum(pm25_values) / len(pm25_values), 2)
    peak_pm25 = max(pm25_values)
    idx = pm25_values.index(peak_pm25)

    peak_aqi, peak_category = pm25_to_aqi(peak_pm25)

    dominant_category = Counter(
        [pm25_to_aqi(v)[1] for v in pm25_values]
    ).most_common(1)[0][0]

    return {
        "horizon": horizon,
        "avg_pm25": avg_pm25,
        "peak_pm25": peak_pm25,
        "peak_pm25_time": timestamps[idx],
        "peak_aqi": peak_aqi,
        "peak_aqi_time": timestamps[idx],
        "dominant_category": dominant_category,
        "overall_risk_level": "Very High" if peak_aqi >= 300 else "Moderate"
    }
