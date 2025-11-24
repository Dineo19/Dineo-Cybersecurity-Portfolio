import json
import socket
import time
import requests
from datetime import datetime

SIEM_ENDPOINT = "http://127.0.0.1:5000/siem"  # replace with real SIEM endpoint
BACKUP_FILE = "backup_logs.json"

def normalize_log(source, event_id, severity, category, message, raw):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "hostname": socket.gethostname(),
        "source": source,
        "event_id": event_id,
        "category": category,
        "severity": severity,
        "message": message,
        "raw_log": raw
    }

def send_to_siem(event):
    try:
        res = requests.post(SIEM_ENDPOINT, json=event, timeout=3)
        res.raise_for_status()
        print(f"📨 Log sent to SIEM: {event}")
    except:
        print("⚠️ SIEM unreachable — saving event locally.")
        with open(BACKUP_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")

def collect_linux_auth_logs():
    logs = []
    try:
        with open("/var/log/auth.log", "r") as f:
            for line in f.readlines()[-20:]:
                logs.append(
                    normalize_log(
                        "linux-auth",
                        1001,
                        "medium",
                        "authentication",
                        "Linux authentication event",
                        line.strip()
                    )
                )
        return logs
    except:
        return []

def collect_custom_logs():
    logs = []
    try:
        with open("sample_logs.txt", "r") as f:
            for line in f.readlines():
                logs.append(
                    normalize_log(
                        "custom-app",
                        2001,
                        "low",
                        "application",
                        "Custom app log event",
                        line.strip()
                    )
                )
        return logs
    except:
        return []

def main():
    print("\n=== SIEM Log Forwarder Started ===\n")

    while True:
        logs = []

        logs += collect_linux_auth_logs()
        logs += collect_custom_logs()

        for event in logs:
            send_to_siem(event)

        time.sleep(10)

if __name__ == "__main__":
    main()
