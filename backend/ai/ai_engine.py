from ai.ai_scripts import AI_SCRIPTS

def get_next_ai_step(step, user_input=None):
    if step == "start":
        return AI_SCRIPTS["start"]

    if step in AI_SCRIPTS:
        return AI_SCRIPTS[step]

    return {
        "message": "Thanks for the info. I’m processing your request now.",
        "options": []
    }


def classify_issue(data):
    category = data.get("category")
    severity = "LOW"
    priority = 3
    action = "AUTO_REPLY"

    if category == "login":
        if data.get("account_locked"):
            severity = "HIGH"
            priority = 1
            action = "ESCALATE"

    if category == "payment":
        if data.get("amount", 0) > 10000:
            severity = "HIGH"
            priority = 1
            action = "ESCALATE"

    if category == "bug":
        severity = "MEDIUM"
        priority = 2

    return {
        "severity": severity,
        "priority": priority,
        "action": action
    }
