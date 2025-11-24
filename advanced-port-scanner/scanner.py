import socket
import threading
from queue import Queue
import datetime

# Thread-safe queue for ports
port_queue = Queue()

# Store open ports
open_ports = []

def scan_port(target_ip, port):
    """Attempts to connect to a port to check if it is open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            open_ports.append(port)
        sock.close()

    except:
        pass


def worker(target_ip):
    """Thread worker function."""
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(target_ip, port)
        port_queue.task_done()


def run_scan(target_ip, start_port, end_port, threads_count=50):
    """Runs the multi-threaded port scan."""
    print("\n=== Starting Port Scan ===")
    print(f"Target: {target_ip}")
    print(f"Port Range: {start_port}-{end_port}\n")

    # Fill queue with ports
    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    # Create threads
    threads = []
    for _ in range(threads_count):
        thread = threading.Thread(target=worker, args=(target_ip,))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    # Wait for all work to finish
    port_queue.join()

    return open_ports


if __name__ == "__main__":
    print("=== Advanced Port Scanner ===")
    target = input("Enter target IP or domain: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    # Run scan
    results = run_scan(target, start, end)

    # Save results
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"scan_results_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(f"Port Scan Results for {target}\n")
        file.write(f"Scanned Range: {start}-{end}\n\n")

        if results:
            file.write("Open Ports:\n")
            for port in results:
                file.write(f"- {port}\n")
        else:
            file.write("No open ports found.\n")

    print("\n=== Scan Complete! ===")
    print(f"Open Ports: {results if results else 'None'}")
    print(f"Results saved to {filename}\n")
