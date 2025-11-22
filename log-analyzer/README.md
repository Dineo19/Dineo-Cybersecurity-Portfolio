#  Python Log Analyzer

A cybersecurity tool that analyzes system logs to detect:

- Failed login attempts  
- Suspicious IP addresses  
- Possible brute-force attacks  
- Frequency of IP activity  

This project demonstrates real SOC-level skills.

---

##  Features

###  Detect failed login attempts
Searches logs for any "Failed password" entries.

###  Identify suspicious IP addresses
Extracts all IPs and counts how many times each appears.

###  Brute-force detection
Flags any IP with 5+ failed login attempts.

---

##  Files Included

| File | Description |
|------|-------------|
| `log_analyzer.py` | Main Python script |
| `sample_logs.txt` | Sample log data for testing |
| `README.md` | Project explanation |

---

##  How to Run

1. Install Python 3
2. Save all files in the same folder
3. Run:

```bash
python log_analyzer.py
