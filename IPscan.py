#!/usr/bin/env python3
"""
Escáner de Red - Detecta dispositivos activos en tu red
Escanea IPs públicas y privadas para identificar hosts activos
"""

import socket
import ipaddress
import concurrent.futures
from datetime import datetime
import sys

def get_local_ip():
    """Obtiene la IP local de la máquina"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

def scan_port(ip, port=80, timeout=1):
    """Escanea un puerto específico en una IP"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def get_hostname(ip):
    """Intenta obtener el hostname de una IP"""
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Desconocido"

def scan_ip(ip):
    """Escanea una IP individual"""
    ip_str = str(ip)
    
    # Intenta hacer ping mediante socket
    if scan_port(ip_str, 80, 0.5) or scan_port(ip_str, 443, 0.5) or scan_port(ip_str, 22, 0.5):
        hostname = get_hostname(ip_str)
        return {
            'ip': ip_str,
            'status': 'activo',
            'hostname': hostname
        }
    return None

def scan_network(network):
    """Escanea toda una red"""
    print(f"\n[*] Iniciando escaneo de red: {network}")
    print(f"[*] Hora de inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    active_hosts = []
    
    try:
        net = ipaddress.ip_network(network, strict=False)
        total_ips = net.num_addresses
        
        print(f"[*] Escaneando {total_ips} direcciones IP...")
        print("[*] Esto puede tomar algunos minutos...\n")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            futures = {executor.submit(scan_ip, ip): ip for ip in net.hosts()}
            
            completed = 0
            for future in concurrent.futures.as_completed(futures):
                completed += 1
                if completed % 10 == 0:
                    print(f"[*] Progreso: {completed}/{total_ips-2} IPs escaneadas", end='\r')
                
                result = future.result()
                if result:
                    active_hosts.append(result)
        
        print("\n")
        return active_hosts
    
    except ValueError as e:
        print(f"[!] Error: Red inválida - {e}")
        return []

def scan_public_ip():
    """Obtiene y muestra información de la IP pública"""
    try:
        import urllib.request
        import json
        
        print("\n[*] Obteniendo información de IP pública...")
        
        response = urllib.request.urlopen('https://api.ipify.org?format=json', timeout=5)
        data = json.loads(response.read())
        public_ip = data['ip']
        
        print(f"[+] Tu IP pública es: {public_ip}")
        return public_ip
    except Exception as e:
        print(f"[!] No se pudo obtener la IP pública: {e}")
        return None

def main():
    print("="*60)
    print(" ESCÁNER DE RED - Herramienta de Ciberseguridad")
    print("="*60)
    
    # Obtener IP local
    local_ip = get_local_ip()
    print(f"\n[+] Tu IP local es: {local_ip}")
    
    # Calcular red local
    local_network = f"{'.'.join(local_ip.split('.')[:-1])}.0/24"
    
    # Menú de opciones
    print("\nOpciones de escaneo:")
    print("1. Escanear red local (privada)")
    print("2. Ver IP pública")
    print("3. Escanear red personalizada")
    print("4. Salir")
    
    try:
        choice = input("\nSelecciona una opción (1-4): ").strip()
        
        if choice == '1':
            print(f"\n[*] Red local detectada: {local_network}")
            active_hosts = scan_network(local_network)
            
            if active_hosts:
                print("\n" + "="*60)
                print(f" HOSTS ACTIVOS ENCONTRADOS: {len(active_hosts)}")
                print("="*60)
                
                for host in active_hosts:
                    print(f"\n[+] IP: {host['ip']}")
                    print(f"    Hostname: {host['hostname']}")
                    print(f"    Estado: {host['status'].upper()}")
            else:
                print("\n[!] No se encontraron hosts activos")
        
        elif choice == '2':
            scan_public_ip()
        
        elif choice == '3':
            network = input("\nIngresa la red a escanear (ej: 192.168.1.0/24): ").strip()
            active_hosts = scan_network(network)
            
            if active_hosts:
                print("\n" + "="*60)
                print(f" HOSTS ACTIVOS ENCONTRADOS: {len(active_hosts)}")
                print("="*60)
                
                for host in active_hosts:
                    print(f"\n[+] IP: {host['ip']}")
                    print(f"    Hostname: {host['hostname']}")
                    print(f"    Estado: {host['status'].upper()}")
            else:
                print("\n[!] No se encontraron hosts activos")
        
        elif choice == '4':
            print("\n[*] Saliendo...")
            sys.exit(0)
        
        else:
            print("\n[!] Opción inválida")
    
    except KeyboardInterrupt:
        print("\n\n[!] Escaneo interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    main()