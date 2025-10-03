# 🔍 Escáner de Red - Network Scanner

## Descripción
Herramienta de ciberseguridad en Python para escanear y detectar dispositivos activos en redes locales (privadas) y obtener información de tu IP pública.

## Características
- ✅ Detección automática de tu red local
- ✅ Escaneo rápido con múltiples hilos
- ✅ Identificación de hosts activos
- ✅ Resolución de nombres de host (hostname)
- ✅ Consulta de IP pública
- ✅ Escaneo de redes personalizadas
- ✅ Interfaz de línea de comandos intuitiva

## Requisitos
- Python 3.6 o superior
- Librerías estándar de Python (no requiere instalación adicional)

## Instalación
```bash
# Clonar o descargar el archivo
wget https://CybersecurityTools-for-Education/IPscan.py

# Dar permisos de ejecución (Linux/Mac)
chmod +x IPscan.py
```

## Uso

### Ejecución básica
```bash
python3 IPscan.py
```

### Opciones disponibles
1. **Escanear red local**: Detecta automáticamente tu red privada y escanea todos los dispositivos
2. **Ver IP pública**: Muestra tu dirección IP pública actual
3. **Escanear red personalizada**: Permite escanear cualquier rango de red
4. **Salir**: Cierra la aplicación

### Ejemplos
```bash
# Escanear tu red local (opción 1)
# Ejemplo de salida:
# [+] IP: 192.168.1.1
#     Hostname: router.home
#     Estado: ACTIVO

# Escanear red personalizada (opción 3)
# Ingresar: 192.168.1.0/24
# o: 10.0.0.0/24
```

## Cómo funciona
1. **Detección de red local**: Identifica automáticamente tu dirección IP y calcula la red local
2. **Escaneo de puertos**: Verifica puertos comunes (80, 443, 22) para detectar hosts activos
3. **Resolución DNS**: Intenta obtener el nombre de host de cada dispositivo activo
4. **Multithreading**: Utiliza hasta 50 hilos simultáneos para acelerar el escaneo

## Limitaciones
- El escaneo puede ser bloqueado por firewalls
- Algunos dispositivos pueden no responder a los puertos escaneados
- La precisión depende de la configuración de red
- No es un escáner de vulnerabilidades completo

## Consideraciones legales ⚖️
⚠️ **IMPORTANTE**: Solo usa esta herramienta en redes de tu propiedad o para las que tengas autorización explícita. El escaneo no autorizado de redes puede ser ilegal en tu jurisdicción.

## Casos de uso
- 🏠 Auditoría de dispositivos en tu red doméstica
- 🔒 Detección de dispositivos no autorizados
- 🖥️ Inventario de equipos en red local
- 🎓 Aprendizaje de conceptos de redes y ciberseguridad

## Troubleshooting
- **No detecta dispositivos**: Verifica que estés en la misma red
- **Error de permisos**: Algunos puertos pueden requerir privilegios de administrador
- **Timeout**: Aumenta el valor de timeout en la función `scan_port()`

## Autor
Maximiliano Hernández

## Licencia

Uso educativo y personal

