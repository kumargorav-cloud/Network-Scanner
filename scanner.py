from scapy.all import ARP, Ether, srp
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# FILL THESE IN
YOUR_EMAIL = "youremailid"
YOUR_APP_PASSWORD = "app code 16 characters"
ALERT_EMAIL = "alertemailid"

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

def scan(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({
            'ip': received.psrc,
            'mac': received.hwsrc,
            'name': get_hostname(received.psrc)
        })
    return devices if devices else []

def send_alert(new_devices):
    subject = "🚨 New Device Joined Your Network!"
    body = "The following new devices were detected:\n\n"
    for d in new_devices:
        body += f"IP: {d['ip']}\nMAC: {d['mac']}\nName: {d['name']}\n\n"

    msg = MIMEMultipart()
    msg['From'] = YOUR_EMAIL
    msg['To'] = ALERT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(YOUR_EMAIL, YOUR_APP_PASSWORD)
        server.sendmail(YOUR_EMAIL, ALERT_EMAIL, msg.as_string())
        server.quit()
        print("Alert email sent!")
    except Exception as e:
        print(f"Email error: {e}")

# Main monitoring loop
print("🔍 Starting network monitor...")
known_devices = set()

# First scan - learn existing devices
for d in scan("actual ip"):
    known_devices.add(d['mac'])
print(f"Found {len(known_devices)} existing devices. Monitoring for new ones...\n")

while True:
    current_devices = scan("actual ip")
    new_devices = []

    for device in current_devices:
        if device['mac'] not in known_devices:
            print(f"New device found: {device['ip']} | {device['mac']} | {device['name']}")
            known_devices.add(device['mac'])
            new_devices.append(device)

    if new_devices:
        send_alert(new_devices)
    else:
        print("No new devices. Network is clean.")

    time.sleep(60)  # scan every 60 seconds