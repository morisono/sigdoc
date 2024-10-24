import socket

def port_scan(target, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting.")
            exit()
        except Exception as e:
            print(f"Error: {e}")
    return open_ports

if __name__ == "__main__":
    target_host = "example.com"
    target_ports = [21, 22, 80, 443]  # Ports to scan
    open_ports = port_scan(target_host, target_ports)
    if open_ports:
        print(f"Open ports on {target_host}: {open_ports}")
    else:
        print(f"No open ports found on {target_host}")
