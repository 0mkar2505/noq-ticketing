from flask_bcrypt import Bcrypt
import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

bcrypt = Bcrypt()

def hash_password(password: str) -> str:
    return bcrypt.generate_password_hash(password).decode("utf-8")

def check_password(password: str, password_hash: str) -> bool:
    return bcrypt.check_password_hash(password_hash, password)

def generate_token(user: dict) -> str:
    payload = {
        "user_id": str(user["_id"]),
        "role": user["role"],
        "company_id": str(user.get("company_id")) if user.get("company_id") else None,
        "exp": datetime.utcnow() + timedelta(hours=6)
    }
    return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")

