from rules.health_advisory_rules import get_health_advisory


def generate_health_advisory(
    aqi_category: str,
    user_group: str = "general"
) -> dict:
    """
    Generate health advisory based on AQI category and user group.

    Parameters:
    - aqi_category: AQI category string (Good, Moderate, Poor, etc.)
    - user_group: general | asthma | elderly

    Returns:
    - Advisory dictionary with risk level and recommendations
    """

    advisory = get_health_advisory(aqi_category, user_group)

    if not advisory:
        return {
            "aqi_category": aqi_category,
            "user_group": user_group,
            "message": "No specific advisory available.",
        }

    return {
        "aqi_category": aqi_category,
        "user_group": user_group,
        "risk_level": advisory.get("risk_level"),
        "outdoor_activity": advisory.get("outdoor_activity"),
        "mask_required": advisory.get("mask_required"),
        "recommendations": advisory.get("recommendations"),
    }
