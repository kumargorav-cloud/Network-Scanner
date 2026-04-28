# 🔍 Network Scanner with Email Alert System

A real-time network monitoring tool built with Python that scans your network, detects connected devices, and sends email alerts when a new device joins.

## 🚀 Features

- Scans your local network for all connected devices
- Displays IP Address, MAC Address and Device Name
- Monitors network continuously every 60 seconds
- Sends automatic email alert when a new device is detected

## 🛠️ Built With

- Python 3
- Scapy — network packet manipulation
- Socket — hostname resolution
- SMTP / Gmail — email alerts
- Linux Terminal

## 📋 Requirements

- Python 3.x
- Linux OS
- Gmail account with App Password

## ⚙️ Installation

1. Clone the repository
   git clone https://github.com/kumargorav-cloud/Network-Scanner.git

2. Create virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install scapy

4. Add your email credentials in scanner.py
   YOUR_EMAIL = "your@gmail.com"
   YOUR_APP_PASSWORD = "your16charpassword"
   ALERT_EMAIL = "your@gmail.com"

5. Run the scanner
   sudo venv/bin/python3 scanner.py

## 📸 Output Example

Available devices on your network:
IP Address           MAC Address          Device Name
------------------------------------------------------------
172.29.112.1         00:15:5d:14:ca:bd    gateway

## 🧠 Concepts Used

- ARP Protocol
- Network Scanning
- Python Scripting
- Email Automation
- Linux Administration

## 👨‍💻 Author

Gorav Kumar
MCA Student | CCNA Certified
GitHub: kumargorav-cloud

## 📄 License

This project is open source and available under the MIT License.