from flask import Blueprint, jsonify
from auth.middleware import require_auth

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard", methods=["GET"])
@require_auth("admin")
def admin_dashboard():
    return jsonify({
        "message": "Admin dashboard access granted"
    }), 200
