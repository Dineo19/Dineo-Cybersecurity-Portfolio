from scapy.all import sniff, DNSQR, ARP, IP
from datetime import datetime

LOG_FILE = "logs.txt"

def log_event(event):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {event}\n")

# Detect DNS Queries
def analyze_dns(packet):
    if packet.haslayer(DNSQR):
        domain = packet[DNSQR].qname.decode()
        log_event(f"DNS Query: {domain}")
        print(f"[DNS] {domain}")

# Detect ARP Spoofing Attempts
def analyze_arp(packet):
    if packet.haslayer(ARP):
        if packet[ARP].op == 2:
            src_ip = packet[ARP].psrc
            src_mac = packet[ARP].hwsrc
            event = f"Possible ARP Spoofing → IP: {src_ip}, MAC: {src_mac}"
            log_event(event)
            print(f"[⚠️ ALERT] {event}")

# Detect HTTP Host Headers (unencrypted)
def analyze_http(packet):
    if packet.haslayer(IP) and packet.haslayer("Raw"):
        try:
            payload = packet["Raw"].load.decode(errors="ignore")
            if "Host:" in payload:
                host_line = [line for line in payload.split("\n") if "Host:" in line]
                if host_line:
                    host = host_line[0].replace("Host: ", "").strip()
                    log_event(f"HTTP Host: {host}")
                    print(f"[HTTP] Visiting → {host}")
        except:
            pass

def process_packet(packet):
    analyze_dns(packet)
    analyze_arp(packet)
    analyze_http(packet)

print("📡 Starting Network Packet Sniffer… (Press CTRL + C to stop)")
sniff(prn=process_packet, store=False)
