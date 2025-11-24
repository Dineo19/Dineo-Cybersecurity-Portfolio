import re

def analyze_event_logs(file_path):
    """Analyzes Windows Security Event Logs for login activity."""
    
    failed_logins = {}
    successful_logins = {}
    brute_force_alerts = []

    try:
        with open(file_path, "r") as logs:
            for line in logs:
                
                # Detect failed logons (Event ID 4625)
                if "EventID: 4625" in line:
                    match = re.search(r"Account:\s(\S+)", line)
                    if match:
                        user = match.group(1)
                        failed_logins[user] = failed_logins.get(user, 0) + 1
                
                # Detect successful logons (Event ID 4624)
                if "EventID: 4624" in line:
                    match = re.search(r"Account:\s(\S+)", line)
                    if match:
                        user = match.group(1)
                        successful_logins[user] = successful_logins.get(user, 0) + 1

        # Detect brute-force attempts
        for user, count in failed_logins.items():
            if count >= 5:
                brute_force_alerts.append((user, count))

        return failed_logins, successful_logins, brute_force_alerts

    except FileNotFoundError:
        print("Log file not found.")
        return None, None, None


if __name__ == "__main__":
    print("\n=== Windows Event Log Analyzer ===")

    file_path = input("Enter path to event logs (e.g., sample_logs.txt): ")

    failed, success, brute_force = analyze_event_logs(file_path)

    if failed is None:
        exit()

    print("\n=== Analysis Summary ===")

    print("\nFailed Login Attempts:")
    for user, count in failed.items():
        print(f" - {user}: {count} attempts")

    print("\nSuccessful Logins:")
    for user, count in success.items():
        print(f" - {user}: {count} logins")

    print("\nBrute-Force Alerts:")
    if brute_force:
        for user, count in brute_force:
            print(f" ⚠ ALERT: {user} has {count} failed logins (Possible brute-force attack!)")
    else:
        print("No brute-force activity detected.")

    print("\nAnalysis Complete.\n")
