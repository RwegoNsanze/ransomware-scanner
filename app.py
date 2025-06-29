from flask import Flask, render_template, jsonify, request
import os
import hashlib
import random
from datetime import datetime

app = Flask(__name__, static_folder='static')

# Enhanced ransomware signature database with classifications
THREAT_TYPES = {
    "READ_ME_TO_RECOVER.txt": {
        "type": "Ransom Note",
        "message": "Potential ransomware note found"
    },
    "ENCRYPTED_FILE": {
        "type": "Fake Encryption",
        "message": "Suspicious encryption pattern detected"
    },
    ".locked": {
        "type": "CryptoLocker Variant",
        "message": "File extension commonly used by CryptoLocker"
    },
    "recover_my_files.exe": {
        "type": "Malicious Executable",
        "message": "Known suspicious executable name"
    }
}

def scan_file(filepath):
    try:
        filename = os.path.basename(filepath)
        file_ext = os.path.splitext(filename)[1].lower()

        # Check against known ransomware patterns
        threat_found = None

        if filename in THREAT_TYPES:
            threat_found = THREAT_TYPES[filename]
        elif file_ext == ".locked":
            threat_found = THREAT_TYPES[".locked"]
        elif "encrypt" in filename.lower() or "decrypt" in filename.lower():
            threat_found = {
                "type": "Suspicious Name",
                "message": "Filename contains encryption keywords"
            }

        return {
            "file": filepath,
            "threat": threat_found,
            "is_clean": not bool(threat_found),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        return {
            "file": filepath,
            "error": str(e),
            "is_clean": False
        }


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    folder_path = data.get("folder")

    if not folder_path or not os.path.isdir(folder_path):
        return jsonify({"error": "Invalid folder path"}), 400

    results = []
    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                filepath = os.path.join(root, file)
                result = scan_file(filepath)
                results.append(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
