# ip_manager.py
import json
import argparse
from network_scanner import get_active_interface, get_network_subnet
from ip_allocator import get_available_ips
from port_checker import check_open_ports

def main():
    parser = argparse.ArgumentParser(description="Administrador de IPs para Linux")
    parser.add_argument("--scan", action="store_true", help="Escanea la red")
    args = parser.parse_args()

    interface = get_active_interface()
    subnet = get_network_subnet(interface)
    
    if args.scan:
        print(f"📡 Interfaz Activa: {interface}")
        print(f"🌐 Subred Detectada: {subnet}")
        print(f"🔍 Escaneando IPs disponibles...")
        available_ips = get_available_ips(subnet)
        print(f"✅ IPs disponibles: {available_ips[:5]}...")  # Solo muestra las primeras 5

if __name__ == "__main__":
    main()

