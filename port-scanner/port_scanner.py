import socket

def scan_port(ip, port):
    """Check if a specific port is open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        sock.connect((ip, port))
        return True
    except:
        return False
    finally:
        sock.close()

def scan_ports(ip, ports):
    """Scan multiple ports on the target IP."""
    open_ports = []

    print(f"\n🔍 Scanning {ip}...\n")
    for port in ports:
        if scan_port(ip, port):
            print(f"[OPEN]  Port {port} is open")
            open_ports.append(port)
        else:
            print(f"[CLOSED] Port {port} is closed")

    return open_ports

def main():
    ip = input("Enter target IP address: ")

    # Common ports to scan
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

    open_ports = scan_ports(ip, ports)

    print("\n=== Scan Complete ===")
    if open_ports:
        print("Open ports detected:", open_ports)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
