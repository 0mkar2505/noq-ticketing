from flask import Blueprint, request, jsonify
from ai.ai_engine import get_next_ai_step

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/ai/step", methods=["POST"])
def ai_step():
    data = request.get_json() or {}
    step = data.get("step", "start")

    response = get_next_ai_step(step, data)
    return jsonify(response)
