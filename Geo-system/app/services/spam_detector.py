import re

CIVIC_KEYWORDS = [
    "road", "pothole", "water", "garbage", "electricity",
    "sewage", "drainage", "traffic", "accident", "bus",
    "signal", "street", "overflow", "pipeline"
]

def detect_spam(text: str):
    cleaned = text.strip().lower()

    # Rule 1: Minimum length
    if len(cleaned) < 15:
        return {
            "is_spam": True,
            "reason": "Text too short",
            "message": "Please describe the civic issue in more detail (minimum 15 characters)."
        }

    # Rule 2: Must contain alphabetic characters
    if not re.search(r"[a-zA-Z]", cleaned):
        return {
            "is_spam": True,
            "reason": "No readable words",
            "message": "Please enter a readable description of the civic issue."
        }

    # Rule 3: Civic relevance
    if not any(keyword in cleaned for keyword in CIVIC_KEYWORDS):
        return {
            "is_spam": True,
            "reason": "No civic context detected",
            "message": (
                "Your message does not seem to describe a civic issue. "
                "Please mention problems like road damage, water issues, garbage, or traffic."
            )
        }

    return {
        "is_spam": False
    }
