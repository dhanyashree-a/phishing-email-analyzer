URGENCY_WORDS = [
    "urgent",
    "immediately",
    "act now",
    "right away",
    "don't delay"
]

def detect_urgency(message):
    message = message.lower()

    detected = []

    for phrase in URGENCY_WORDS:
        if phrase in message:
            detected.append(phrase)

    return detected

import re

THREAT_PATTERNS = {
    "Account suspension threat": r"account\s+(?:will be\s+)?(?:permanently\s+)?suspended",
    "Account deletion threat": r"account\s+(?:will be\s+)?(?:permanently\s+)?deleted",
    "Account blocking threat": r"account\s+(?:will be\s+)?(?:permanently\s+)?blocked",
    "Legal action threat": r"legal action",
    "Security breach": r"security breach",
    "Unauthorized access": r"unauthorized access",
    "Final warning": r"final warning"
}


def detect_threats(message):
    message = message.lower()

    detected = []

    for description, pattern in THREAT_PATTERNS.items():
        if re.search(pattern, message):
            detected.append(description)

    return detected

CREDENTIAL_PATTERNS = {
    "Password request": r"\bpassword\b",
    "OTP request": r"\botp\b|\bone[- ]time password\b",
    "PIN request": r"\bpin\b",
    "Verification code request": r"\bverification code\b|\bsecurity code\b",
    "Login credentials request": r"\blogin credentials\b",
    "Username request": r"\busername\b"
}

def detect_credentials(message):
    message = message.lower()

    detected = []

    for description, pattern in CREDENTIAL_PATTERNS.items():
        if re.search(pattern, message):
            detected.append(description)

    return detected

def analyze_text(message):
    return {
        "urgency": detect_urgency(message),
        "threats": detect_threats(message),
        "credentials": detect_credentials(message)
    }

