import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def pong_endpoint():
    answer_value = os.getenv("APP_ANSWER", "").strip()

    return jsonify({"message": answer_value}), 200

@app.route("/favicon.ico")
def favicon():
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
