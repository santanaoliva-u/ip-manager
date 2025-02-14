# interactive_ui.py
import curses
import json
from network_scanner import get_active_interface, get_network_subnet
from ip_allocator import get_available_ips
from port_checker import check_open_ports

def start_interface(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    stdscr.addstr(1, 5, "📡 IP MANAGER - Administrador de Redes Inteligente", curses.A_BOLD)

    interface = get_active_interface()
    subnet = get_network_subnet(interface)

    stdscr.addstr(3, 5, f"Interfaz Activa: {interface}", curses.color_pair(2))
    stdscr.addstr(4, 5, f"Subred Detectada: {subnet}", curses.color_pair(2))

    available_ips = get_available_ips(subnet)
    stdscr.addstr(6, 5, f"IPs Disponibles: {len(available_ips)}", curses.color_pair(3))

    stdscr.refresh()
    stdscr.getch()

curses.wrapper(start_interface)

