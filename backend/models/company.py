from models.db import company_collection
from datetime import datetime

def create_company(name, email):
    company = {
        "name": name,
        "email": email,
        "created_at": datetime.utcnow(),
        "is_active": True
    }
    company_collection.insert_one(company)
    return company
