# BMS Custom de Topología Modular para Celdas de Ión-Litio

Proyecto Integrador — Ingeniería Electrónica
FCEFyN, Universidad Nacional de Córdoba
**Autor:** Joel Wayar | **Director:** Sergio Aguero

---

## Descripción

Diseño, implementación y evaluación de un Sistema de Gestión de Baterías (BMS) a medida para un pack de 10 celdas Li-ion 18650 en serie (36V nominal). El sistema monitoriza voltajes, corriente y temperatura, ejecuta balanceo pasivo de celdas y estima el estado de carga (SOC) en tiempo real.

---

## Arquitectura

- **Microcontrolador:** PIC16F877A (por ahora)
- **Medición de celdas:** MUX analógico 16:1 + circuito de acondicionamiento
- **Balanceo:** Pasivo por derivación (~100mA por celda)
- **Potencia:** MOSFETs back-to-back para control CH/DCH
- **Comunicación:** UART → USB (CP2102) → App (Python) en PC

---

## Estado del proyecto

🟡 **En curso** — Milestone actual: *M1* Investigación y especificaciones

---

## Estructura del repositorio

```
BMS-LiIon-PI/
│
├── README.md                  # Descripción general del proyecto
├── docs/
│   ├── memoria/               # Capítulos de la memoria final (Markdown)
│   ├── datasheets/            # PDFs de componentes clave
│   └── imagenes/              # Diagramas, fotos del prototipo
│
├── hardware/
│   ├── esquematicos/          # Archivos KiCad o Eagle + PDFs exportados
│   ├── pcb/                   # Archivos de PCB
│   └── BOM.md                 # Lista de materiales con precios ARS
│
├── firmware/
│   ├── src/                   # Código fuente PIC (MPLAB)
│   ├── include/               # Headers
│   └── build/                 # Archivos compilados (.hex)
│
├── software-pc/               # App Python para monitoreo
│
└── pruebas/
    ├── resultados/            # CSVs y gráficos de ensayos
    └── protocolos/            # Procedimientos de prueba documentados
```

---

## 🚀 Setup del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/BMS-LiIon-PI.git
cd BMS-LiIon-PI
```

### 2. Crear estructura de archivos y carpetas

Ejecuta el script de creación de estructura (genera carpetas y archivos vacíos):

```bash
python scripts/create-files.py
```

**Este script crea:**
- 📁 Toda la jerarquía de directorios
- 📄 Archivos base vacíos (`main.c`, `bms_config.h`, `BOM.md`, etc.)

### 3. Configurar entorno virtual e instalar dependencias

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/Mac
source venv/bin/activate

# Instalar dependencias necesarias
pip install requests python-dotenv
```

### 4. Configurar GitHub token (para milestones e issues)

Crear un archivo `.env` en la raíz del proyecto:

```bash
# .env
GITHUB_TOKEN=github_pat_tu_token_aqui
GITHUB_OWNER=tu_usuario
GITHUB_REPO=BMS-LiIon-PI
```

> ⚠️ **Importante:** El `.env` debe estar incluido en `.gitignore`.

**Cómo obtener el token:**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generar un token con permisos: `repo` (todos) y `issues`

### 5. Crear Milestones e Issues en GitHub

Ejecutar el script de automatización:

```bash
python scripts/create-github-project.py
```

**Este script crea automáticamente:**
- ✅ 6 Milestones (uno por mes, con fechas de entrega)
- ✅ 46 Issues distribuidos según cada milestone
- ✅ Issues etiquetados como "task"

### 6. Verificar en GitHub

Revisa que todo se haya creado correctamente:

```bash
https://github.com/tu-usuario/BMS-LiIon-PI/milestones
```

---

## 📦 Scripts disponibles

| Script | Ubicación | Función |
|--------|-----------|---------|
| `create-files.py` | `/scripts/` | Crea estructura de carpetas y archivos vacíos |
| `create-github-project.py` | `/scripts/` | Crea milestones e issues en GitHub automáticamente |

---

## 🛠️ Tecnologías utilizadas

- **Hardware:** KiCad, PIC16F877A, MUX CD4067, MOSFETs, INA219, DS18B20
- **Firmware:** MPLAB XC8, C
- **Software PC:** Python, pyserial, matplotlib, tkinter
- **Gestión:** GitHub (milestones, issues, proyectos)

---

## 📅 Cronograma (Milestones)

- **M1** — Investigación y especificaciones (mes 1)
- **M2** — Diseño de hardware (mes 2)
- **M3** — PCB y fabricación (mes 3)
- **M4** — Firmware (mes 4)
- **M5** — App PC y pruebas (mes 5)
- **M6** — Documentación y entrega (mes 6)

---

## 👨‍💻 Autor

**Joel Wayar**
Estudiante de Ingeniería Electrónica
FCEFyN, Universidad Nacional de Córdoba

**Director:** Sergio Aguero

---

## 📄 Licencia

Este proyecto es de uso académico. Todos los derechos reservados.
