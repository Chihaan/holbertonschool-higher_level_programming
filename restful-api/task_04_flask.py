#!/usr/bin/python3
"""A simple RESTful API built with Flask."""

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """Return the welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def list_usernames():
    """Return the list of all stored usernames."""
    return jsonify(list(users))


@app.route("/status")
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>")
def show_user(username):
    """Return the user object for a username, or a 404 error."""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from the posted JSON data."""
    donnees = request.get_json(silent=True)
    if donnees is None:
        return jsonify({"error": "Invalid JSON"}), 400
    elif "username" not in donnees:
        return jsonify({"error": "Username is required"}), 400
    elif donnees["username"] in users:
        return jsonify({"error": "Username already exists"}), 409
    else:
        users[donnees["username"]] = donnees
        return jsonify({"message": "User added", "user": donnees}), 201


if __name__ == "__main__":
    app.run()
