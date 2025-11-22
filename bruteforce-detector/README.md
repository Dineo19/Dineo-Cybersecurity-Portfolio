
# Brute-Force Login Detection Tool

This project detects brute-force login attempts by analyzing failed authentication logs.  
It identifies IP addresses with repeated failed login attempts and flags potential attacks.

---

##  Features
- Detects failed SSH login attempts  
- Counts failed attempts per IP  
- Flags IPs exceeding a brute-force threshold  
- Easy to modify for real SOC / Linux environments  

---

##  Project Structure

bruteforce-detector/
│── bruteforce_detector.py # Main detection script
│── auth_logs.txt # Sample authentication logs
│── README.md # Documentation


---

## How It Works
1. Reads authentication logs  
2. Searches for “Failed password” entries  
3. Extracts the attacker’s IP address  
4. Counts failed attempts per IP  
5. Generates alerts if attempts exceed the limit (default = 5)

---

## Run the Tool
```bash
python3 bruteforce_detector.py

