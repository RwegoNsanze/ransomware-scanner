# 🛡️ Personal Ransomware Scanner

**Author:** Rwego Nsanze  
**License:** MIT  
**Last Updated:** 2025

## 🚀 Overview
A simple yet effective web-based ransomware detection tool presented by Rwego Nsanze for his Final Year Project that simulates the scanning of uploaded files for potential ransomware threats. Built using **Flask (Python)** for the backend and **JavaScript + HTML/CSS** for the frontend.

## 🛠 Features
- Upload and scan folders for potential ransomware indicators.
- Detects:
  - Common ransomware file extensions like `.locked`
  - Suspicious filenames containing `encrypt` or `decrypt`
  - Known ransomware bait files like `READ_ME_TO_RECOVER.txt`
- Beautiful and responsive UI

## 💻 Technologies Used
- **Python** (Flask)
- **HTML5 / CSS3**
- **JavaScript**

## 📁 Project Structure
```
ransomware-scanner/
├── app.py # Flask server
├── create_dummy_threats.py# Test data generator
├── static/
│ └── style.css # (Optional) CSS
├── templates/
│ └── index.html # Main UI
└── README.md # About my project ```


## 🧪 Running the App

1. Install Flask (if not yet installed):

```bash
pip install flask

python app.py

http://localhost:5000
