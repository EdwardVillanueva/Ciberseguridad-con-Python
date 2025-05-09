import sys
import socket
from datetime import datetime

def verificar_conexion(target_ip):
    """
    Verifica si hay conexión con el host haciendo un intento de conexión rápida.
    """
    try:
        # Intentamos conectar al puerto 80 (HTTP) como verificación general
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)  # Esperamos máximo 2 segundos
            resultado = sock.connect_ex((target_ip, 80))
            return resultado == 0  # True si hay conexión
    except Exception:
        return False

def main():
    target = "192.168.0.31"
    
    print("-" * 40)
    print(f"El objetivo es: {target}")
    print(f"Inicio del escaneo: {datetime.now()}")
    print("-" * 40)
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("No se puede resolver el nombre del host.")
        sys.exit()
    
    if not verificar_conexion(target_ip):
        print(f"No hay conexión con el host {target_ip}. El host podría estar apagado o fuera de red.")
        sys.exit()
    
    print(f"Conexión exitosa con {target_ip}. Iniciando escaneo de puertos...\n")

    for port in range(1, 81):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"El puerto {port} está ABIERTO.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nEscaneo interrumpido por el usuario.")
        sys.exit()
