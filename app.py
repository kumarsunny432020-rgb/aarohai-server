import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Server is running 🚀"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message")

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4.1-mini",
        "input": user_message
    }

    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers=headers,
        json=payload
    )

    result = response.json()

    if "error" in result:
        return jsonify({"reply": "AI service temporarily unavailable 🤖"})

    try:
        reply = result["output"][0]["content"][0]["text"]
    except:
        reply = "AI service temporarily unavailable 🤖"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
