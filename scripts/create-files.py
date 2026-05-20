# create-files.py
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(script_dir, "..")

directories = [
    "docs/memoria",
    "docs/datasheets",
    "docs/imagenes",
    "hardware/esquematicos",
    "hardware/pcb",
    "firmware/src",
    "firmware/include",
    "firmware/build",
    "software-pc",
    "pruebas/resultados",
    "pruebas/protocolos"
]

# Archivos a crear (vacíos)
files = [
    "README.md",
    "hardware/BOM.md",
    "firmware/src/main.c",
    "firmware/include/bms_config.h",
    "software-pc/bms_monitor.py",
    "software-pc/requirements.txt",
    "pruebas/README.md"
]

print(f"📂 Creando estructura en: {base_path}\n")

# Crear directorios
for dir_path in directories:
    full_path = os.path.join(base_path, dir_path)
    os.makedirs(full_path, exist_ok=True)
    print(f"📁 Creado: {dir_path}")

# Crear archivos vacíos
for file_path in files:
    full_path = os.path.join(base_path, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        pass  # Archivo vacío
    print(f"📄 Creado: {file_path}")

print("\n✅ Estructura del proyecto BMS-LiIon-PI creada exitosamente!")