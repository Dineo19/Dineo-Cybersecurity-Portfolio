# 🛡 Incident Response Report — Unauthorized Login Attempt  
### Author: Dineo Matlabyana  
### Role: Junior Cybersecurity Analyst (SOC Analyst Level 1)

---

## 📌 Overview

This report documents a simulated incident involving repeated unauthorized login attempts on a Windows endpoint.  
The purpose of this project is to demonstrate my skills in:

- Incident triage  
- Log analysis  
- Identifying Indicators of Compromise (IOCs)  
- Applying the NIST Incident Response Framework  
- Writing professional security reports  

---

## 🧩 Incident Summary

| Field | Details |
|------|---------|
| **Incident Type** | Unauthorized login attempts (Brute Force) |
| **Date Identified** | 29 November 2025 |
| **Detection Source** | Windows Security Event Logs |
| **Severity Level** | Medium |
| **Target System** | Windows 10 Workstation |
| **User Impacted** | Local Administrator Account (admin01) |

---

## 🛠 Detection & Analysis

During routine monitoring, multiple failed authentication events were detected in the Windows Security logs:

✔ Event ID **4625** — Failed login  
✔ Event ID **4624** — Successful login  

Analysis revealed:

- **27 failed login attempts** within 5 minutes  
- Attempts originated from suspicious IP: **185.234.219.37**  
- User account targeted: **admin01**  
- Authentication type: **Explicit credentials** (suggesting brute-force attempts)  

### 🔎 Example Log Entry (Anonymized)

Event ID: 4625
Account Name: admin01
Source Network Address: 185.234.219.37
Failure Reason: Unknown user name or bad password
Logon Type: 3

### ✔ Indicators of Compromise (IOCs)
- Repeated failed logins
- Remote IP associated with known malicious activity
- Login attempts outside business hours (02:13 AM)

---

## 🚨 Containment Measures

- Blocked external IP **185.234.219.37** at firewall level  
- Forced password reset for account **admin01**  
- Locked account temporarily to prevent further attempts  
- Initiated monitoring for additional suspicious IPs  

---

## 🔧 Eradication

- Scanned Windows system for malware — no threats found  
- Confirmed no successful unauthorized logins  
- Verified no new accounts were created  

---

## 🛡 Recovery

- Enabled multi-factor authentication (MFA) on high-risk accounts  
- Updated endpoint security policies  
- Restored normal account access with strong password enforcement  
- Enabled additional auditing on logon events  

---

## 📚 Lessons Learned

- Accounts with weak passwords remain high-risk  
- MFA would have prevented this attack completely  
- Brute-force attempts continue to be a common external threat vector  
- Automated log monitoring should run hourly instead of daily  

---

## 🧠 Skills Demonstrated

✔ Log analysis (Windows Event Viewer)  
✔ Identifying brute-force attacks  
✔ Threat detection & incident classification  
✔ Writing clear, professional IR documentation  
✔ Understanding of NIST Incident Response Lifecycle  
✔ Evidence collection & IOC identification  

---

## 📂 Files Included

- `/sample_logs.txt` — anonymized Windows security logs  
- `/investigation-notes.txt` — analyst notes  
- `/report.pdf` — printable incident response report  

---

## 📫 Contact

For detailed review or collaboration:  
**Email:** matlabyanadineo1@gmail.com  

---

