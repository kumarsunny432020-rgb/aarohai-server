import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.route("/")
def home():
    return "Server is running 🚀"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "No message provided"}), 400

    user_message = data.get("message")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        result = response.json()

        print(result)   # Render logs में Gemini response दिखेगा

        if "candidates" in result:
            reply = result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            reply = "Gemini API error 🤖"

    except Exception as e:
        print("Error:", e)
        reply = "AI service temporarily unavailable 🤖"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
