# 🛡️ Detector de Malware - Malware Detector

## Descripción
Herramienta educativa de ciberseguridad en Python para analizar archivos sospechosos y detectar posibles indicadores de malware mediante análisis de patrones, firmas y comportamientos.

## Características
- ✅ Cálculo de hashes (MD5 y SHA256)
- ✅ Comparación con base de datos de malware conocido
- ✅ Detección de strings sospechosos
- ✅ Análisis de nombres de archivo sospechosos
- ✅ Identificación de extensiones peligrosas
- ✅ Verificación de tipo de archivo (file signature)
- ✅ Sistema de niveles de amenaza (Bajo, Medio, Alto, Crítico)
- ✅ Generación de reportes en JSON

## Requisitos

### Python
- Python 3.6 o superior

### Dependencias
```bash
pip install python-magic
```

**Nota**: En algunos sistemas también necesitas instalar libmagic:
```bash
# Ubuntu/Debian
sudo apt-get install libmagic1

# MacOS
brew install libmagic

# Windows
pip install python-magic-bin
```

## Instalación
```bash
# Clonar o descargar el archivo
wget https://CybersecurityTools-for-Education/MalwareDetector.py

# Instalar dependencias
pip install python-magic

# Dar permisos de ejecución (Linux/Mac)
chmod +x MalwareDetector.py
```

## Uso

### Sintaxis básica
```bash
python3 MalwareDetector.py <archivo_a_analizar>
```

### Ejemplos
```bash
# Analizar un archivo ejecutable
python3 MalwareDetector.py sospechoso.exe

# Analizar un script
python3 MalwareDetector.py script.ps1

# Analizar cualquier archivo
python3 MalwareDetector.py documento.pdf
```

### Ejemplo de salida
```
======================================================================
 REPORTE DE ANÁLISIS DE MALWARE
======================================================================

📄 Archivo: archivo_sospechoso.exe
📍 Ruta: /home/usuario/descargas/archivo_sospechoso.exe
📊 Tamaño: 45,321 bytes
🕐 Fecha de análisis: 2025-10-02 14:30:45

🔐 Hashes:
   MD5:    d41d8cd98f00b204e9800998ecf8427e
   SHA256: e3b0c44298fc1c149afbf4c8996fb924...

📝 Tipo de archivo: PE32 executable (GUI) Intel 80386
🏷️  MIME Type: application/x-dosexec

🟠 NIVEL DE AMENAZA: ALTO

⚠️  ALERTAS (3):
   • ⚠️ Extensión potencialmente peligrosa
   • ⚠️ Encontrados 5 strings sospechosos
   • Patrón sospechoso: \.exe$

🔍 STRINGS SOSPECHOSOS ENCONTRADOS (5):
   • cmd.exe
   • powershell
   • regsvr32
   • CreateObject
   • WScript.Shell

======================================================================
❌ RECOMENDACIÓN: NO ejecutar este archivo. Podría ser malware.
======================================================================
```

## Cómo funciona

### 1. Análisis de Hashes
- Calcula MD5 y SHA256 del archivo
- Compara contra base de datos de malware conocido
- Útil para identificar amenazas ya catalogadas

### 2. Detección de Patrones
- Analiza el nombre del archivo en busca de patrones sospechosos
- Identifica extensiones potencialmente peligrosas
- Detecta nombres típicos de malware (crack, keygen, etc.)

### 3. Análisis de Contenido
- Busca strings sospechosos comunes en malware
- Identifica comandos de sistema y shells
- Detecta funciones peligrosas de scripting

### 4. Verificación de Tipo
- Usa libmagic para identificar el tipo real del archivo
- Detecta discrepancias entre extensión y contenido real
- Identifica archivos disfrazados

### 5. Niveles de Amenaza
- **🟢 BAJO**: Archivo parece seguro
- **🟡 MEDIO**: Algunas características sospechosas
- **🟠 ALTO**: Múltiples indicadores de malware
- **🔴 CRÍTICO**: Malware conocido identificado

## Limitaciones importantes ⚠️

Esta es una herramienta **EDUCATIVA** con limitaciones:

1. **No es un antivirus completo**: No reemplaza software profesional
2. **Base de datos limitada**: Solo contiene ejemplos de hashes conocidos
3. **Falsos positivos**: Puede marcar archivos legítimos como sospechosos
4. **Falsos negativos**: Malware sofisticado puede no ser detectado
5. **Sin análisis dinámico**: No ejecuta el archivo en sandbox
6. **Sin análisis de comportamiento**: No observa acciones en tiempo real

## Expandir la herramienta

### Agregar más hashes de malware
Edita el diccionario `KNOWN_MALWARE_HASHES` en el código:
```python
KNOWN_MALWARE_HASHES = {
    'hash_md5_aqui': 'Nombre-del-Malware',
    # Agregar más...
}
```

### Agregar más patrones
Modifica las listas `SUSPICIOUS_PATTERNS` y `SUSPICIOUS_STRINGS`:
```python
SUSPICIOUS_PATTERNS.append(r'tu_patron_aqui')
SUSPICIOUS_STRINGS.append(b'tu_string_aqui')
```

## Integración con APIs

Para análisis más robusto, puedes integrar:
- **VirusTotal API**: Enviar hashes para verificación
- **MalwareBazaar**: Consultar base de datos de malware
- **Hybrid Analysis**: Análisis en sandbox

## Casos de uso
- 🎓 Aprendizaje de análisis de malware
- 🔍 Primera revisión de archivos sospechosos
- 📊 Generación de reportes de archivos
- 🏠 Análisis básico en entornos personales
- 🧪 Testing y desarrollo de detecciones

## Consideraciones de seguridad 🔒

⚠️ **NUNCA** ejecutes archivos sospechosos en tu sistema principal:
- Usa máquinas virtuales aisladas
- Utiliza entornos sandbox dedicados
- No confíes únicamente en esta herramienta
- Siempre usa antivirus profesional actualizado

## Troubleshooting

### Error: "magic" module not found
```bash
pip install python-magic
# o en Windows:
pip install python-magic-bin
```

### Error: "Permission denied"
```bash
# En Linux/Mac, necesitas permisos de lectura
chmod +r archivo_a_analizar
```

### El análisis es muy lento
- Archivos muy grandes tardan más
- Considera limitar el tamaño de archivos a analizar

## Recursos adicionales
- [YARA Rules](https://github.com/Yara-Rules/rules) - Reglas de detección avanzadas
- [VirusTotal](https://www.virustotal.com) - Análisis multi-antivirus
- [MalwareBazaar](https://bazaar.abuse.ch/) - Base de datos de malware
- [Any.run](https://any.run/) - Sandbox interactivo

## Autor
Herramienta educativa de ciberseguridad

## Licencia
Uso educativo y personal

## Disclaimer
Esta herramienta se proporciona "tal cual" con fines educativos. Los autores no se responsabilizan por mal uso o daños. Siempre usa software antivirus profesional actualizado para protección real.