# create-git-project.py
import os
import sys
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(script_dir, "..")

env_path = os.path.join(project_root, ".env")
load_dotenv(env_path)

# ================= CONFIGURACIÓN DESDE .env =================
TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("GITHUB_OWNER")
REPO_NAME = os.getenv("GITHUB_REPO")

# Verificar que las variables existan
if not all([TOKEN, REPO_OWNER, REPO_NAME]):
    print("❌ Error: Faltan variables en .env")
    print("Asegúrate de tener GITHUB_TOKEN, GITHUB_OWNER y GITHUB_REPO")
    exit(1)

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

BASE_URL = "https://api.github.com/repos"

# Fechas para los milestones (ajustar según fecha de inicio)
fecha_inicio = datetime(2026, 5, 20)  # Cambiar según corresponda

milestones_data = [
    ("M1 — Investigación y especificaciones (mes 1)",
     fecha_inicio,
     fecha_inicio + timedelta(days=30)),

    ("M2 — Diseño de hardware (mes 2)",
     fecha_inicio + timedelta(days=31),
     fecha_inicio + timedelta(days=60)),

    ("M3 — PCB y fabricación (mes 3)",
     fecha_inicio + timedelta(days=61),
     fecha_inicio + timedelta(days=90)),

    ("M4 — Firmware (mes 4)",
     fecha_inicio + timedelta(days=91),
     fecha_inicio + timedelta(days=120)),

    ("M5 — App PC y pruebas (mes 5)",
     fecha_inicio + timedelta(days=121),
     fecha_inicio + timedelta(days=150)),

    ("M6 — Documentación y entrega (mes 6)",
     fecha_inicio + timedelta(days=151),
     fecha_inicio + timedelta(days=180))
]

# Issues por milestone
issues_m1 = [
    "Confirmar director y completar datos del SAT",
    "Definir corriente máxima de descarga (5A, 10A, 20A?)",
    "Decidir entre PIC16F877A o PIC16F876A",
    "Elegir MUX analógico: CD4067 vs DG406",
    "Definir tipo de celda 18650 a usar (nueva vs reciclada)",
    "Relevar precios de componentes en Córdoba y MercadoLibre",
    "Estudiar datasheet completo PIC16F877A (ADC, UART, timers)",
    "Estudiar material del director: aplicaciones y BMS"
]

issues_m2 = [
    "Diseñar circuito de medida: MUX + amplificador diferencial",
    "Calcular circuito de acondicionamiento (offset 3.0V, ganancia)",
    "Diseñar circuito de balanceo: TLP220G + resistencia por celda",
    "Diseñar tarjeta de potencia: MOSFETs CH/DCH back-to-back",
    "Seleccionar y calcular sensor de corriente (shunt + INA219)",
    "Definir sensores de temperatura DS18B20 y ubicación",
    "Diseñar circuito de alimentación del módulo",
    "Dibujar esquemático completo en KiCad"
]

issues_m3 = [
    "Diseñar PCB tarjeta de control",
    "Diseñar PCB tarjeta de potencia",
    "Revisar reglas DRC y verificar footprints",
    "Fabricar PCB (JLCPCB, PCBWay o local en Córdoba)",
    "Comprar componentes según BOM",
    "Soldar y verificar continuidad"
]

issues_m4 = [
    "Inicializar ADC y rutina de lectura con MUX",
    "Implementar lectura de 10 celdas con corrección de offset",
    "Implementar lectura de temperatura DS18B20 (1-wire)",
    "Implementar lectura de corriente (INA219 vía I2C)",
    "Implementar máquina de estados: init / espera / carga / descarga / fallo",
    "Implementar algoritmo de balanceo pasivo",
    "Implementar estimación SOC por Coulomb Counting",
    "Implementar protecciones: OVP, UVP, OTP, OCP",
    "Implementar comunicación UART hacia PC"
]

issues_m5 = [
    "App Python: conexión UART con pyserial",
    "App Python: gráfico en tiempo real de voltajes por celda",
    "App Python: visualización de SOC, temperatura y corriente",
    "Ensayo de carga completa del pack (10 celdas)",
    "Ensayo de descarga completa del pack",
    "Verificar actuación de protecciones",
    "Verificar funcionamiento del balanceo"
]

issues_m6 = [
    "Redactar capítulo 1: introducción y estado del arte",
    "Redactar capítulo 2: especificaciones y arquitectura",
    "Redactar capítulo 3: diseño de hardware",
    "Redactar capítulo 4: firmware",
    "Redactar capítulo 5: resultados y pruebas",
    "Redactar conclusiones y trabajo futuro",
    "Armar presentación de defensa",
    "Hacer repositorio público"
]

issues_por_milestone = [issues_m1, issues_m2, issues_m3, issues_m4, issues_m5, issues_m6]

# ================= FUNCIONES =================
def crear_milestone(titulo, descripcion, fecha_inicio, fecha_entrega):
    url = f"{BASE_URL}/{REPO_OWNER}/{REPO_NAME}/milestones"
    data = {
        "title": titulo,
        "state": "open",
        "description": descripcion,
        "due_on": fecha_entrega.isoformat() + "Z"
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"✅ Milestone creado: {titulo}")
        return response.json()["number"]
    else:
        print(f"❌ Error creando milestone {titulo}: {response.status_code}")
        print(response.json())
        return None

def crear_issue(titulo, milestone_numero):
    url = f"{BASE_URL}/{REPO_OWNER}/{REPO_NAME}/issues"
    data = {
        "title": titulo,
        "milestone": milestone_numero,
        "labels": ["task"]
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"  ✅ Issue creado: {titulo[:60]}...")
        return True
    else:
        print(f"  ❌ Error creando issue: {response.status_code}")
        return False

# ================= EJECUCIÓN PRINCIPAL =================
def main():
    print("🚀 Iniciando creación de Milestones e Issues en GitHub...\n")
    print(f"📌 Repositorio: {REPO_OWNER}/{REPO_NAME}\n")

    milestone_numeros = []

    # Crear milestones
    for i, (titulo, inicio, fin) in enumerate(milestones_data):
        descripcion = f"Mes {i+1} - {titulo.split('—')[1].strip()}"
        numero = crear_milestone(titulo, descripcion, inicio, fin)
        if numero:
            milestone_numeros.append(numero)
        print()

    # Crear issues para cada milestone
    for i, (numero, issues) in enumerate(zip(milestone_numeros, issues_por_milestone)):
        if numero:
            print(f"\n📋 Creando issues para Milestone {i+1}...")
            for issue_titulo in issues:
                crear_issue(f"{issue_titulo}", numero)

    print("\n" + "="*50)
    print("🎉 ¡PROCESO COMPLETADO!")
    print(f"📌 Revisa tu repositorio: https://github.com/{REPO_OWNER}/{REPO_NAME}/milestones")
    print("="*50)

if __name__ == "__main__":
    print("⚠️  Verificando configuración...")
    if not TOKEN:
        print("❌ No se encontró GITHUB_TOKEN en .env")
        print("   Crea un archivo .env con:")
        print("   GITHUB_TOKEN=tu_token_aqui")
        print("   GITHUB_OWNER=tu_usuario")
        print("   GITHUB_REPO=BMS-LiIon-PI")
    else:
        print("✅ Configuración encontrada")
        main()