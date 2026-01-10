def generate_pm25_forecast(horizon: str):
    timestamps = [
        "2026-01-09 00:00",
        "2026-01-09 01:00",
        "2026-01-09 02:00",
        "2026-01-09 03:00",
        "2026-01-09 04:00",
    ]

    pm25 = [180.0, 210.5, 245.3, 310.8, 290.4]

    return timestamps, pm25
