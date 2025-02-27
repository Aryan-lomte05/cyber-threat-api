from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    description = data.get('description', '')
    result = {"Threat Classification": "Phishing"}  # Replace with your ML logic
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
