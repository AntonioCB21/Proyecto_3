# 📚 Wiki - Documentación para Desarrolladores

## Índice

1. [🔧 Requisitos técnicos](#-requisitos-técnicos)  
2. [📁 Estructura del proyecto](#-estructura-del-proyecto)  
3. [⚙️ Configuración del entorno](#-configuración-del-entorno)  
4. [🧠 Lógica del sistema](#-lógica-del-sistema)  
5. [📤 Integración con APIs de almacenamiento](#-integración-con-apis-de-almacenamiento)  
6. [📦 Gestión de dependencias](#-gestión-de-dependencias)  
7. [🧪 Testing](#-testing)  
8. [📈 Ideas para ampliaciones](#-ideas-para-ampliaciones)

---

## 🔧 Requisitos técnicos

- **Lenguaje principal**: Python 3.7+
- **Dependencias**:
  - `pydrive2` (Google Drive)
  - `dropbox` (Dropbox)
  - `schedule` (Tareas programadas)
  - `os`, `shutil`, `json`, `datetime` (nativas)

---

## 📁 Estructura del proyecto
    ```bash
    AutoBackupScript/
    │
    ├── auto_backup_script.py       # Script principal
    ├── config.json                 # Configuración de carpetas, servicios y credenciales
    ├── requirements.txt            # Librerías necesarias
    ├── README.md                   # Descripción general
    ├── CONTRIBUTING.md             # Guía para colaborar
    ├── demo/                       # Simulación en Streamlit (opcional)
    └── docs/                       # Esta wiki u otros recursos técnicos

---

## ⚙️ Configuración del entorno

1. Clona el repositorio
    ```bash
    git clone https://github.com/tu_usuario/AutoBackupScript.git

2. Crea un entorno virtual
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. Instala dependencias
    ```bash
    pip install -r requirements.txt

---

## 🧠 Lógica del sistema
- El usuario define carpetas/archivos en config.json.

- El script revisa si existen en la nube.

- Si no están, los sube.

- Si ya existen versiones antiguas, las borra según configuración.

- Todo esto se puede ejecutar manualmente o por programación automática (cron, Task Scheduler).

---

## 📤 Integración con APIs de almacenamiento
### Google Drive
- Usa pydrive2

- Requiere archivo credentials.json (OAuth2 desde Google Cloud Console)

- Verifica duplicados usando title y parents.

### Dropbox
- Usa dropbox.Dropbox

- Requiere token de acceso desde Dropbox App Console

- Subidas vía files_upload

---

## 📦 Gestión de dependencias
- Archivo requirements.txt:
```
pydrive2
dropbox
schedule
```

- Actualiza con:
    ```bash
    pip freeze > requirements.txt

---

## 🧪 Testing
- Actualmente no incluye tests automatizados.

- Para contribuir, se recomienda usar unittest o pytest.

- Puedes simular cargas usando carpetas temporales en /tmp o mocks de API.

---

## 📈 Ideas para ampliaciones
- Soporte para OneDrive o Amazon S3.

- Cifrado de archivos antes de subirlos.

- Gestión de versiones (control incremental).

- Interfaz gráfica básica.

- Integración con sistemas de logs.

- Dashboard online con historial de respaldos.
