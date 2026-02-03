from flask import Blueprint, request, jsonify
from models.user import User
from auth.utils import check_password, generate_token

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user = User.find_by_email(data["email"])

    if not user or not check_password(data["password"], user["password_hash"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user)

    return jsonify({
        "token": token,
        "user": {
            "id": str(user["_id"]),
            "role": user["role"],
            "company_id": str(user.get("company_id")) if user.get("company_id") else None
        }
    })
