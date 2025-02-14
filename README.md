
---

# **IP Manager 🚀**  
📡 *Administrador de Direcciones IP Dinámico para Linux*  

![Linux Network](https://img.shields.io/badge/Linux-Network%20Management-blue.svg)  
![Python](https://img.shields.io/badge/Python-3.12-green.svg)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)  

## **📖 Descripción**  
**IP Manager** es una herramienta avanzada de administración y asignación de direcciones IP para sistemas **Linux** *(Arch, Kali, Ubuntu, Parrot)*.  

🔹 **Evita conflictos de IPs** en servicios y contenedores Docker.  
🔹 **Automatiza la detección** de IPs y puertos disponibles.  
🔹 **Asigna dinámicamente direcciones** según la red activa (*wlan0* o *eth0*).  
🔹 **Interfaz interactiva** y colorida en la terminal.  
🔹 **Optimizado para rendimiento** y bajo consumo de recursos.  

---

## **📂 Estructura del Proyecto**
```
📂 ip-manager/
 ├── 📜 ip_manager.py          # Script principal
 ├── 📜 network_scanner.py     # Escaneo de red
 ├── 📜 ip_allocator.py        # Asignador de IPs
 ├── 📜 port_checker.py        # Escaneo de puertos
 ├── 📜 interactive_ui.py      # Interfaz interactiva
 ├── 📜 config.json            # Configuración persistente
 ├── 📜 README.md              # Documentación
```

---

## **🛠️ Instalación**
### **🔹 Requisitos Previos**
Antes de instalar **IP Manager**, asegúrate de tener lo siguiente en tu sistema:  
✅ **Python 3.12** o superior  
✅ **Permisos de administrador** (*sudo*)  
✅ **Dependencias necesarias** (instalar con `pip`)  

### **🔹 Instalación Rápida**
```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/santanaoliva-u/ip-manager.git
cd ip-manager

# 2️⃣ Instala dependencias
pip install -r requirements.txt

# 3️⃣ Ejecuta el escáner de IPs
python ip_manager.py --scan
```

---

## **🚀 Uso**
### **🔍 Escaneo de la Red**
```bash
python ip_manager.py --scan
```
*Muestra la interfaz activa, la subred detectada y las IPs disponibles.*  

### **🎨 Interfaz Interactiva**
```bash
python interactive_ui.py
```
*Navega de forma visual y asigna IPs dinámicamente desde la terminal.*  

### **🛠️ Configuración Avanzada**
El archivo `config.json` guarda las asignaciones de IPs y ajustes personalizados.  

---

## **🖥️ Ejemplo de Uso**
```bash
> python ip_manager.py --scan
📡 Interfaz Activa: eth0  
🌐 Subred Detectada: 192.168.1.0/24  
🔍 IPs Disponibles: ['192.168.1.100', '192.168.1.101', '192.168.1.102']  
```

---

## **🤝 Contribuciones**
¡Este proyecto es de código abierto! Si deseas contribuir:  
1. **Haz un fork** 🍴  
2. **Crea una rama** `feature/nueva-funcion`  
3. **Haz commit de tus cambios**  
4. **Abre un Pull Request**  

---

## **📜 Licencia**
**MIT License** - Eres libre de usarlo, modificarlo y mejorarlo 🚀.  

📌 **Repositorio Oficial:** [GitHub - santanaoliva-u/ip-manager](https://github.com/santanaoliva-u/ip-manager)  

🔥 *¿Ideas para mejorar? ¡Toda contribución es bienvenida!* 🚀
