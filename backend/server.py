from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "sample_scans.json")


@app.route("/scan", methods=["POST"])
def receive_scan():
    data = request.get_json(force=True, silent=True) or {}
    data["received_at"] = datetime.utcnow().isoformat() + "Z"

    scans = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                scans = json.load(f)
            except json.JSONDecodeError:
                scans = []

    scans.append(data)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(scans, f, indent=2)

    return jsonify({"status": "ok"})


@app.route("/scans", methods=["GET"])
def list_scans():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                scans = json.load(f)
            except json.JSONDecodeError:
                scans = []
    else:
        scans = []

    return jsonify(scans)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
