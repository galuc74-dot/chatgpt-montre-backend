import os
from flask import Flask, jsonify, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.post("/ask")
def ask():
    data = request.get_json(force=True, silent=True) or {}
    message = str(data.get("message", "")).strip()

    if not message:
        return jsonify({"error": "message manquant"}), 400

    response = client.responses.create(
        model=os.environ.get("OPENAI_MODEL", "gpt-5.6-luna"),
        input=message,
        max_output_tokens=220
    )

    return jsonify({"reply": response.output_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787)
