import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()


def hash_password(password: str) -> str:
    """Hash a password using bcrypt. Returns utf-8 decoded string."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode("utf-8")


def check_password(password: str, password_hash: str) -> bool:
    """Check a password against a bcrypt hash."""
    if not password_hash:
        return False
    try:
        return bcrypt.checkpw(
            password.encode(),
            password_hash.encode()
        )
    except Exception:
        return False


def generate_token(user) -> str:
    payload = {
        "user_id": str(user._id),
        "role": user.role,
        "company_id": str(user.company_id) if user.company_id else None,
        "exp": datetime.utcnow() + timedelta(hours=6)
    }
    return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")
