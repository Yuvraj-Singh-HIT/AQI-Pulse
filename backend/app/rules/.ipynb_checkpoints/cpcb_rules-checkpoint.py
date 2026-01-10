"""
CPCB AQI computation rules for PM2.5
Source: Central Pollution Control Board (India)
"""

# PM2.5 breakpoints: (PM_low, PM_high, AQI_low, AQI_high, Category)
PM25_BREAKPOINTS = [
    (0.0, 30.0, 0, 50, "Good"),
    (31.0, 60.0, 51, 100, "Satisfactory"),
    (61.0, 90.0, 101, 200, "Moderate"),
    (91.0, 120.0, 201, 300, "Poor"),
    (121.0, 250.0, 301, 400, "Very Poor"),
    (251.0, float("inf"), 401, 500, "Severe"),
]


def pm25_to_aqi(pm25: float):
    """
    Convert PM2.5 concentration to AQI value and category.

    Parameters
    ----------
    pm25 : float
        PM2.5 concentration (µg/m³)

    Returns
    -------
    tuple
        (aqi_value, category)
    """

    if pm25 is None:
        return None, None

    pm25 = float(pm25)

    for pm_lo, pm_hi, aqi_lo, aqi_hi, category in PM25_BREAKPOINTS:
        if pm_lo <= pm25 <= pm_hi:
            # Linear interpolation (CPCB formula)
            aqi = ((aqi_hi - aqi_lo) / (pm_hi - pm_lo)) * (pm25 - pm_lo) + aqi_lo
            aqi = round(min(aqi, 500))  # Cap AQI at 500
            return aqi, category

    return None, None
