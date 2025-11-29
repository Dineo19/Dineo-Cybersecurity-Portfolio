SIEM Log Analysis Project (Splunk Simulation)

Analyst: Dineo Matlabyana
Role: SOC Analyst L1
Tools simulated: Splunk / Wazuh / Elastic

1. Objective

To detect suspicious events using log analysis, identify attack patterns, and recommend mitigation steps.

2. Log Source

Security logs collected from:

Authentication logs

Windows Event Logs

Linux auth logs

Firewall logs

Web server logs

3. Key Events Identified
🔎 Event 1: Brute Force Attack Detected

Indicator:
Multiple failed login attempts from the same external IP.

Field	Value
Source IP	185.221.100.92
Destination	Auth Server
Attempts	42 failed logins
Status	FAILED
Time Window	8 minutes

Tactic: Credential Access
Technique: Brute Force (MITRE T1110)

Action Taken:

IP blocked at firewall

Account temporarily locked

User notified

🔎 Event 2: Suspicious Privilege Escalation

Indicator:
A normal user executed admin-level commands.

Field	Value
Username	j.smith
Event ID	4672
Action	Admin privilege assigned
Device	WIN10-Workstation

Tactic: Privilege Escalation (T1068)

Action Taken:

Session terminated

AD Admin notified

Forensic review initiated

🔎 Event 3: Malware Hash Detected

Security tool flagged a file hash:

e99c6512f5ce12341a9f91834fbd88e4


VirusTotal → MALICIOUS
Category → Trojan Downloader
Severity → High

Action Taken:

File quarantined

System isolated

Malware analysis started

4. SIEM Queries Used (Simulated)
Failed login attempts
index=security sourcetype=auth action=failure 
| stats count by src_ip, user 
| where count > 10

Privilege escalation
index=windows EventID=4672

Malicious hash lookup
index=security file_hash=*

5. Summary

This analysis demonstrated skills in:

✔ Threat detection
✔ SIEM query logic
✔ Incident triage
✔ MITRE ATT&CK mapping
✔ Reporting

6. Files Included

sample_logs.txt

analysis_report.txt

siem_queries.txt
