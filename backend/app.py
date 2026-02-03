from flask import Flask
from flask import request
from flask_cors import CORS
from auth.routes import auth_bp
from auth.utils import bcrypt

app = Flask(__name__)
CORS(app)

bcrypt.init_app(app)

app.register_blueprint(auth_bp)

@app.route("/health")
def health():
    return {"status": "ok"}

from auth.middleware import require_auth

@app.route("/protected")
@require_auth()
def protected():
    return {
        "message": "You are authenticated",
        "user": request.user
    }


if __name__ == "__main__":
    app.run(debug=True)
