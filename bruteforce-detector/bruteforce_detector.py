# Brute-Force Login Detection Tool

FAILED_LIMIT = 5  # Number of failed logins before alert

def detect_bruteforce(log_file):
    failed_attempts = {}

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                parts = line.split()
                ip = parts[-1]  # Last element is the IP address

                if ip not in failed_attempts:
                    failed_attempts[ip] = 0
                
                failed_attempts[ip] += 1

    print("=== Brute-Force Detection Report ===")
    for ip, count in failed_attempts.items():
        if count >= FAILED_LIMIT:
            print(f"[ALERT] {ip} triggered a brute-force attempt ({count} failed logins)")
        else:
            print(f"{ip} failed {count} time(s)")

if __name__ == "__main__":
    log_path = "auth_logs.txt"
    detect_bruteforce(log_path)
