from flask import Blueprint, jsonify
from auth.middleware import require_auth

client_bp = Blueprint("client", __name__)

@client_bp.route("/dashboard", methods=["GET"])
@require_auth("client")
def client_dashboard():
    return jsonify({
        "message": "Client dashboard access granted"
    }), 200
