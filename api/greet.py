from flask import Flask, jsonify

# Vercel will run this 'app' object
app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def handle_greet():
    # This function will run when someone visits /api/greet
    return jsonify(message="Hello from the Python (Flask) API!")