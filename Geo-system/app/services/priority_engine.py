def compute_priority(issue_type: str, sentiment: float, text: str):
    text = text.lower()

    base_priority = {
        "ROAD": 2,
        "GARBAGE": 2,
        "WATER": 3,
        "ELECTRICITY": 3,
        "SEWAGE": 3,
        "OTHER": 1
    }

    priority_score = base_priority.get(issue_type, 1)

    urgency_keywords = [
        "accident", "danger", "emergency",
        "blocked", "overflow", "fire"
    ]

    if any(word in text for word in urgency_keywords):
        priority_score += 1

    if sentiment < -0.4:
        priority_score += 1

    priority_score = min(priority_score, 4)

    priority_map = {
        1: "LOW",
        2: "MEDIUM",
        3: "HIGH",
        4: "CRITICAL"
    }

    return {
        "priority": priority_map[priority_score],
        "severity_score": priority_score * 25
    }
