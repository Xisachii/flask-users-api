import json
import os
from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/users")
def get_users():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump([], f)
    return send_file("users.json", mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
