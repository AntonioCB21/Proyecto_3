# 🛡️ AutoBackupScript

## 📌 Motivación del Proyecto

Hoy en día, tanto personas como pequeñas empresas generan constantemente archivos digitales de gran valor. Sin embargo, muchas veces se carece de una solución simple, automática y segura para realizar copias de seguridad. Herramientas complejas, configuraciones avanzadas o costes elevados impiden una adopción generalizada.

**AutoBackupScript** nace como un proyecto **open source, minimalista y funcional** que permite hacer **copias de seguridad automáticas** de archivos o carpetas en la nube (Google Drive o Dropbox) sin complicaciones.

Este proyecto tiene como metas:
- Ofrecer una herramienta accesible para usuarios con pocos conocimientos técnicos.
- Garantizar que los archivos importantes estén siempre respaldados y actualizados.
- Automatizar tareas comunes de backup sin depender de software de terceros con licencias privativas.

---

## 🚀 Instrucciones de Instalación y Despliegue

### 📦 Requisitos previos
- Python 3.7 o superior
- Acceso a Google Drive y/o Dropbox
- Conexión a internet

### 🔧 Instalación

1. **Clona el repositorio**
```bash
git clone https://github.com/tuusuario/autobackupscript.git
cd autobackupscript
```

2. **Instala las dependencias necesarias**
```
pip install pydrive2 dropbox schedule
```

3. **Configura tu archivo config.json**
```
{
  "folders_to_backup": ["C:/mis_documentos", "D:/trabajos"],
  "use_google_drive": true,
  "use_dropbox": false,
  "delete_old_backups_after_days": 30,
  "google_drive_credentials_file": "credentials.json",
  "dropbox_access_token": ""
}
```

## 🖥️ Despliegue por plataforma
### En Windows
· Ejecuta manualmente el script:
```
python auto_backup_script.py
```
· O programa su ejecución automática con el Programador de Tareas de Windows.

### En Linux/macOS
· Ejecuta manualmente:
```
python3 auto_backup_script.py
```
· O automatiza con cron:
```
crontab -e
```

· Ejemplo para ejecutar cada día a las 2 AM:
```
0 2 * * * /usr/bin/python3 /ruta/completa/auto_backup_script.py
```

## 🧪 Ejemplo de uso
1. Configuras las rutas a respaldar y servicios en config.json.

2. Ejecutas el script:
```
python auto_backup_script.py
```

3. El script sube automáticamente los archivos que no están en la nube.
4. Archivos antiguos son eliminados según los días definidos.

## ✅ Características destacadas
✔ Respaldo automático y configurable

✔ Compatibilidad con Google Drive y Dropbox

✔ Elimina versiones antiguas automáticamente

✔ Ligero y sin interfaz gráfica innecesaria

✔ Seguridad con OAuth2

✔ Ideal para automatizar con cron o tareas programadas

## 🧠 Futuras mejoras
- Soporte para OneDrive y Amazon S3

- Interfaz gráfica web minimalista

- Compresión automática de archivos antes de subirlos

- Notificaciones por correo o Telegram al terminar el respaldo

## 👥 Licencia y comunidad
Este proyecto es open source bajo licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
¡Las contribuciones están abiertas!
