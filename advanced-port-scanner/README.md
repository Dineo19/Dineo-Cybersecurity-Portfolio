# Advanced Port Scanner (Multi-Threaded)

A fast, multi-threaded Python port scanner that identifies open ports and saves the results to a report file.  
This tool demonstrates real-world skills used in penetration testing and network security analysis.

---

##  Features
- Multi-threaded (very fast)
- Scans any port range
- Supports IP or domain
- Stores results in a report file
- Detects open ports only (no noise)
- SOC & Pentesting friendly

---

##  Project Structure


advanced-port-scanner/
│── scanner.py # Main scanner
│── README.md # Documentation


---

##  How It Works
1. User enters an IP/domain  
2. User provides a port range  
3. Scanner tries connecting to each port  
4. Uses **threads** for high speed  
5. Saves results to a file:  
   `scan_results_YYYY-MM-DD_HH-MM-SS.txt`

---

##  Run the Tool
```bash
python3 scanner.py
