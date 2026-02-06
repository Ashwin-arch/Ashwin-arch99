def classify_issue(text: str):
    text = text.lower()

    ISSUE_KEYWORDS = {
        "ROAD": ["road", "pothole", "traffic", "damage", "highway"],
        "WATER": ["water", "leak", "pipeline", "no water"],
        "ELECTRICITY": ["power", "electricity", "street light", "current"],
        "GARBAGE": ["garbage", "waste", "trash", "dump"],
        "SEWAGE": ["sewage", "drainage", "toilet", "overflow"]
    }

    scores = {}

    for issue, keywords in ISSUE_KEYWORDS.items():
        scores[issue] = sum(1 for kw in keywords if kw in text)

    # Find best match
    issue_type = max(scores, key=scores.get)

    if scores[issue_type] == 0:
        return {
            "issue_type": "OTHER",
            "confidence": "LOW"
        }

    confidence = "HIGH" if scores[issue_type] >= 2 else "MEDIUM"

    return {
        "issue_type": issue_type,
        "confidence": confidence
    }
