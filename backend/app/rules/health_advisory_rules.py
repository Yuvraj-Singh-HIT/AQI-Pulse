# Health advisory rules based on AQI category and user group

HEALTH_ADVISORY_RULES = {
    "Good": {
        "general": {
            "risk_level": "Low",
            "outdoor_activity": "Safe",
            "mask_required": False,
            "recommendations": [
                "Enjoy outdoor activities",
                "No health risk expected"
            ]
        },
        "asthma": {
            "risk_level": "Low",
            "outdoor_activity": "Safe",
            "mask_required": False,
            "recommendations": [
                "Normal activities are safe"
            ]
        },
        "elderly": {
            "risk_level": "Low",
            "outdoor_activity": "Safe",
            "mask_required": False,
            "recommendations": [
                "No special precautions needed"
            ]
        }
    },

    "Moderate": {
        "general": {
            "risk_level": "Moderate",
            "outdoor_activity": "Limit prolonged exposure",
            "mask_required": False,
            "recommendations": [
                "Reduce prolonged outdoor exertion"
            ]
        },
        "asthma": {
            "risk_level": "High",
            "outdoor_activity": "Avoid heavy exertion",
            "mask_required": True,
            "recommendations": [
                "Carry inhaler",
                "Avoid polluted areas"
            ]
        },
        "elderly": {
            "risk_level": "High",
            "outdoor_activity": "Limit outdoor exposure",
            "mask_required": True,
            "recommendations": [
                "Avoid peak pollution hours"
            ]
        }
    },

    "Poor": {
        "general": {
            "risk_level": "High",
            "outdoor_activity": "Avoid",
            "mask_required": True,
            "recommendations": [
                "Wear N95 mask",
                "Reduce outdoor movement"
            ]
        },
        "asthma": {
            "risk_level": "Very High",
            "outdoor_activity": "Avoid",
            "mask_required": True,
            "recommendations": [
                "Avoid going outside",
                "Seek medical advice if symptoms worsen"
            ]
        },
        "elderly": {
            "risk_level": "Very High",
            "outdoor_activity": "Avoid",
            "mask_required": True,
            "recommendations": [
                "Stay indoors",
                "Medical consultation advised"
            ]
        }
    },

    "Very Poor": {
        "general": {
            "risk_level": "Very High",
            "outdoor_activity": "Avoid",
            "mask_required": True,
            "recommendations": [
                "Stay indoors",
                "Use air purifiers"
            ]
        },
        "asthma": {
            "risk_level": "Emergency",
            "outdoor_activity": "Avoid",
            "mask_required": True,
            "recommendations": [
                "Life-threatening conditions possible",
                "Seek immediate medical help if needed"
            ]
        },
        "elderly": {
            "risk_level": "Emergency",
            "outdoor_activity": "Avoid",
            "mask_required": True,
            "recommendations": [
                "Extremely dangerous air quality",
                "Medical consultation advised"
            ]
        }
    }
}


def get_health_advisory(aqi_category: str, user_group: str) -> dict:
    """
    Returns health advisory for a specific user group.
    """
    return HEALTH_ADVISORY_RULES.get(aqi_category, {}).get(user_group, {})


def get_all_health_advisories(aqi_category: str) -> dict:
    """
    Returns health advisory for all user groups (general, asthma, elderly).
    """
    return {
        "category": aqi_category,
        "general": HEALTH_ADVISORY_RULES.get(aqi_category, {}).get("general", {}),
        "asthma": HEALTH_ADVISORY_RULES.get(aqi_category, {}).get("asthma", {}),
        "elderly": HEALTH_ADVISORY_RULES.get(aqi_category, {}).get("elderly", {})
    }
