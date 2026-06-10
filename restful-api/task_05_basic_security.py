#!/usr/bin/python3
"""API security with HTTP Basic Auth and JWT authentication."""

from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "GibvuAlbuk7-draMiasug6!-9tAtanes"
jwt = JWTManager(app)


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Return a 401 when the token is missing."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Return a 401 when the token is invalid."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Return a 401 when the token has expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Return a 401 when the token has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Return a 401 when a fresh token is required."""
    return jsonify({"error": "Fresh token required"}), 401


auth = HTTPBasicAuth()


users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password",
                                                 method="pbkdf2:sha256"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password",
                                                  method="pbkdf2:sha256"),
               "role": "admin"}
}


@auth.verify_password
def verify(username, password):
    """Verify the username and password for basic auth."""
    if username not in users:
        return None
    if check_password_hash(users[username]["password"], password):
        return username
    else:
        return None


@app.route("/basic-protected")
@auth.login_required
def authentification():
    """Return a message for a valid basic-auth user."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def grant_token():
    """Check credentials and return a JWT access token."""
    donnees = request.get_json()
    username = donnees.get("username")
    password = donnees.get("password")
    if verify(username, password) is None:
        return jsonify({"error": "Password or user incorrect"}), 401
    else:
        token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]}
        )
        return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_check():
    """Return a message for a valid JWT token."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Return a message if the JWT user has the admin role."""
    token = get_jwt()
    role = token["role"]
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
