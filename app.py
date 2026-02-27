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

    try:
        reply = result["output"][0]["content"][0]["text"]
    except:
        reply = "Error getting response from OpenAI"

    return jsonify({"reply": reply})
