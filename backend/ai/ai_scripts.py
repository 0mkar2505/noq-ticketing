AI_SCRIPTS = {
    "start": {
        "message": "Hi 👋 I’m your support assistant. I’ll ask a few quick questions to understand your issue.",
        "options": [
            {"id": "login", "label": "🔐 Login Issue"},
            {"id": "payment", "label": "💳 Payment Issue"},
            {"id": "refund", "label": "🧾 Refund"},
            {"id": "bug", "label": "🐞 Bug / App Error"},
            {"id": "other", "label": "❓ Something Else"}
        ]
    },

    "login": {
        "message": "Got it. Let me ask a couple of things about your login problem.",
        "questions": [
            {
                "id": "account_locked",
                "text": "Is your account currently locked?",
                "type": "boolean"
            },
            {
                "id": "business_user",
                "text": "Is this a business or admin account?",
                "type": "boolean"
            }
        ]
    },

    "payment": {
        "message": "Thanks. I need a bit of info about the payment issue.",
        "questions": [
            {
                "id": "amount",
                "text": "What is the approximate payment amount?",
                "type": "number"
            }
        ]
    }
}
