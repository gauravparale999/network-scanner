import socket

def scan_port(target, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout for connection attempt
        s.settimeout(1)
        # Attempt to connect to the target IP address and port
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_target(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        scan_port(target, port)

def main():
    target = input("Enter target IP address: ")
    ports = [21, 22, 23, 80, 443]  # Example list of ports to scan
    scan_target(target, ports)

if __name__ == "__main__":
    main()
