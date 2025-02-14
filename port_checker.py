# port_checker.py
import socket

def check_open_ports(ip, start=1, end=65535):
    """Escanea los puertos abiertos en una IP dada."""
    open_ports = []
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
    return open_ports

