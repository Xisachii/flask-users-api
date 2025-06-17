# main.py (Render uchun)
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

USERS_FILE = 'users.json'

# Fayl mavjud bo'lmasa, bo'sh ro'yxat yaratamiz
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f:
        json.dump([], f)

@app.route("/users", methods=["GET"])
def get_users():
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    return jsonify(users)

@app.route("/add_user", methods=["POST"])
def add_user():
    user = request.json
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)

    # Dublikatni tekshirish
    if not any(u['id'] == user['id'] for u in users):
        users.append(user)
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=2)
        return jsonify({"status": "added"}), 201

    return jsonify({"status": "exists"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
