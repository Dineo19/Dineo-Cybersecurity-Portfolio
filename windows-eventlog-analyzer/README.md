# Windows Event Log Analyzer

A SOC-ready tool that analyzes Windows Security Event Logs, detects failed login attempts, successful logins, and identifies possible brute-force attacks.

Based on Event IDs used in real investigations:
- **4624 – Successful login**
- **4625 – Failed login**

---

##  Features
- Detects failed login attempts  
- Detects successful logins  
- Flags brute-force attacks (5+ failed attempts)  
- Investigates suspicious user activity  
- Uses real Windows Event IDs  

---

##  Project Structure

windows-eventlog-analyzer/
│── eventlog_analyzer.py # Analyzer script
│── sample_logs.txt # Example Windows logs
│── README.md # Documentation


---

##  Run the Tool
```bash
python3 eventlog_analyzer.py
sample_logs.txt
