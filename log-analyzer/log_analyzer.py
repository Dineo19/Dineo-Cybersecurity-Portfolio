import re
from collections import Counter

# === Load Logs ===
def load_logs(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

# === Detect Failed Logins ===
def detect_failed_logins(logs):
    pattern = r"Failed password for"
    return [log for log in logs if re.search(pattern, log)]

# === Detect Suspicious IPs ===
def detect_suspicious_ips(logs):
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    ips = []

    for log in logs:
        match = re.findall(ip_pattern, log)
        if match:
            ips.extend(match)

    ip_count = Counter(ips)
    return ip_count.most_common()

# === Detect Brute Force Attempts ===
def detect_bruteforce(logs, threshold=5):
    failed = detect_failed_logins(logs)
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    attempts = Counter()

    for log in failed:
        ip = re.search(ip_pattern, log)
        if ip:
            attempts[ip.group()] += 1

    return {ip: count for ip, count in attempts.items() if count >= threshold}

# === Main Runner ===
def main():
    logs = load_logs("sample_logs.txt")

    print("\n==== FAILED LOGIN ATTEMPTS ====")
    for log in detect_failed_logins(logs):
        print(log.strip())

    print("\n==== SUSPICIOUS IP ADDRESSES ====")
    for ip, count in detect_suspicious_ips(logs):
        print(f"{ip} attempted connections {count} times")

    print("\n==== BRUTE FORCE ATTEMPTS (>=5 FAILS) ====")
    brute_force = detect_bruteforce(logs)
    if brute_force:
        for ip, count in brute_force.items():
            print(f"{ip} failed {count} times — POSSIBLE BRUTE FORCE")
    else:
        print("No brute force attempts detected.")

if __name__ == "__main__":
    main()
