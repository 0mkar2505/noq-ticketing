import jwt
import os
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()

def require_auth(required_role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization")

            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify({"error": "Missing or invalid token"}), 401

            token = auth_header.split(" ")[1]

            try:
                payload = jwt.decode(
                    token,
                    os.getenv("JWT_SECRET"),
                    algorithms=["HS256"]
                )
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Invalid token"}), 401

            # role check (if required)
            if required_role and payload["role"] != required_role:
                return jsonify({"error": "Forbidden"}), 403

            # attach user to request
            request.user = payload
            return f(*args, **kwargs)

        return wrapper
    return decorator
