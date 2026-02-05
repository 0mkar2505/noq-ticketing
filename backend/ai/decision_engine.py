def evaluate_severity(data):
    severity = "LOW"
    priority = 3

    if data.get("account_locked") and data.get("business_user"):
        severity = "HIGH"
        priority = 1

    if data.get("amount", 0) > 10000:
        severity = "HIGH"
        priority = 1

    return {
        "severity": severity,
        "priority": priority
    }
