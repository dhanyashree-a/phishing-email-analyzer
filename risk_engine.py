RISK_SCORES = {
    "urgency": 1,
    "threat": 2,
    "credential": 2,
    "IP-based URL": 2,
    "HTTP URL": 1,
    "Possible brand impersonation": 3,
    "Possible lookalike domain": 3
}


def calculate_risk(analysis):
    score = 0

    text_analysis = analysis["text_analysis"]
    url_analysis = analysis["url_analysis"]

    # Urgency
    if text_analysis["urgency"]:
        score += RISK_SCORES["urgency"]

    # Threats
    threat_score = min(
        len(text_analysis["threats"]) * RISK_SCORES["threat"],
        4
    )
    score += threat_score

    # Credential requests
    credential_score = min(
        len(text_analysis["credentials"]) * RISK_SCORES["credential"],
        4
    )
    score += credential_score

    # URL indicators
    for url in url_analysis:
        for indicator in url["indicators"]:
            if indicator in RISK_SCORES:
                score += RISK_SCORES[indicator]

    return score


def get_risk_level(score):
    if score >= 6:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"


def generate_risk_report(analysis):
    score = calculate_risk(analysis)
    risk_level = get_risk_level(score)

    indicators = []

    text_analysis = analysis["text_analysis"]

    if text_analysis["urgency"]:
       indicators.append("Urgency / time-pressure")

    if text_analysis["threats"]:
        indicators.append("Threat / fear language")

    if text_analysis["credentials"]:
       indicators.append("Credential request")

    for url in analysis["url_analysis"]:
        indicators.extend(url["indicators"])

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "indicators": indicators
    }