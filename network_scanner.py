# network_scanner.py
import os
import subprocess
import ipaddress

def get_active_interface():
    """Detecta la interfaz de red activa y devuelve su nombre."""
    interfaces = ["wlan0", "eth0"]
    for iface in interfaces:
        try:
            output = subprocess.check_output(f"ip -o -4 addr show {iface}", shell=True).decode()
            if output:
                return iface
        except subprocess.CalledProcessError:
            continue
    return None

def get_network_subnet(interface):
    """Obtiene la subred de la interfaz activa."""
    try:
        output = subprocess.check_output(f"ip -o -4 addr show {interface}", shell=True).decode()
        ip_info = output.split()[3]
        return ipaddress.ip_network(ip_info, strict=False)
    except:
        return None

