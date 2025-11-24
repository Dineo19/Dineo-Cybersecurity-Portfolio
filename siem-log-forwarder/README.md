# 🔥 SIEM Log Forwarder & Normalizer

A Python-based SIEM log forwarder that collects system logs, normalizes them into a structured JSON format, and forwards them to a SIEM endpoint (Splunk, ELK, Wazuh, etc.).

This shows real SOC Analyst skills — log parsing, normalization, and SIEM ingestion.

---

## 🔥 Features

- Normalizes logs into consistent JSON format  
- Adds timestamp, hostname, category, and severity  
- Collects logs from:
  - Linux authentication logs
  - Custom log files
- Sends logs to a SIEM endpoint via HTTP POST  
- Falls back to local backup if SIEM is offline  

---

## 🗂 Project Structure

siem-log-forwarder/
│── siem_forwarder.py
│── README.md


---

## ▶️ How to Run

```bash
python3 siem_forwarder.py
