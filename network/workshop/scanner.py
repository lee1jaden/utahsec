import socket
import threading

def tcp_scan(target, start_port, end_port):
    for port in range(start_port, end_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open.")
            s.close()

    threads = []
    for port in range(start_port, end_port):
        thread = threading.Thread(target=scan_port, args=(port))

def scan_port(target):


tcp_scan('127.0.0.1', 1, 12346)

