#  Network Packet Sniffer (Project 7)

A real-time packet sniffer built using Scapy.  
This tool captures and analyzes network traffic for DNS requests, ARP spoofing, and HTTP host headers.

This project demonstrates real SOC Analyst and Network Security skills.

---

##  Features

###  Real-Time Packet Capture  
Sniffs packets live from the network interface.

###  DNS Monitoring  
Detects domains being visited by devices.

###  ARP Spoofing Detection  
Alerts when suspicious ARP replies occur (MITM attack indicator).

###  HTTP Host Header Extraction  
Shows websites visited over unencrypted HTTP.

###  Logging  
All captured events are saved in `logs.txt`.

---

##  Project Structure

network-packet-sniffer/
│── packet_sniffer.py
│── README.md
│── logs.txt (auto-generated)


---

##  How to Run

Install Scapy:

```bash
pip install scapy

---

## How to Run

Install Scapy:

```bash
pip install scapy

sudo python3 packet_sniffer.py
