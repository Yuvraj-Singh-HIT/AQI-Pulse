def pm25_to_aqi(pm25: float):
    if pm25 <= 30:
        return 50, "Good"
    elif pm25 <= 60:
        return 100, "Satisfactory"
    elif pm25 <= 90:
        return 200, "Moderate"
    elif pm25 <= 120:
        return 300, "Poor"
    elif pm25 <= 250:
        return 400, "Very Poor"
    else:
        return 500, "Severe"
