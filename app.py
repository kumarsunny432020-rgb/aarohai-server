@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message")

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are AarohiAI, a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload
    )

    result = response.json()

    reply = result["choices"][0]["message"]["content"]

    return jsonify({"reply": reply})
