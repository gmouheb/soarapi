import os

os.system('pip install flask')

from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load JSON data
with open("data.json", "r") as file:
    data = json.load(file)

@app.route("/vulnerabilities", methods=["GET"])
def get_vulnerabilities():
    return jsonify(data)

@app.route("/vulnerabilities/<ip>", methods=["GET"])
def get_vulnerabilities_by_ip(ip):
    filtered_data = [entry for entry in data if entry["Hostname/IP"] == ip]
    return jsonify(filtered_data if filtered_data else {"message": "No data found for this IP"})

if __name__ == "__main__":
    app.run(debug=True)
