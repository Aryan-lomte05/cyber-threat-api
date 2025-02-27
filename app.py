from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route("/")
def home():
    return "🚀 Cyber Threat Detection API is running successfully!"

@app.route("/classify", methods=["POST"])
def classify():
    data = request.json
    text = data.get("text", "")

    # Simple classification logic (replace with actual ML model later)
    if "phishing" in text.lower() or "login credentials" in text.lower():
        classification = "Phishing Attempt"
    elif "ransomware" in text.lower() or "bitcoin" in text.lower():
        classification = "Ransomware Threat"
    elif "unauthorized access" in text.lower() or "admin panel" in text.lower():
        classification = "Unauthorized Access"
    else:
        classification = "Unknown Threat"

    return jsonify({"classification": classification})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Ensure proper binding for Render
