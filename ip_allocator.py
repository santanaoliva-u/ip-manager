# ip_allocator.py
import subprocess
import socket

def get_used_ips(subnet):
    """Escanea la subred y retorna las IPs en uso."""
    used_ips = []
    for ip in subnet.hosts():
        try:
            socket.gethostbyaddr(str(ip))
            used_ips.append(str(ip))
        except (socket.herror, socket.gaierror):
            pass
    return used_ips

def get_available_ips(subnet):
    """Devuelve la lista de IPs disponibles en la subred."""
    used = set(get_used_ips(subnet))
    return [str(ip) for ip in subnet.hosts() if str(ip) not in used]

