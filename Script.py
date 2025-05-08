# Importamos las librerías necesarias
import os  # Para trabajar con archivos y rutas en el sistema operativo
import json  # Para cargar configuraciones en formato JSON
import time  # Para trabajar con temporizadores y pausas
import datetime  # Para trabajar con fechas y horas
import schedule  # Para programar tareas de manera automática
from pydrive.auth import GoogleAuth  # Para autenticar con Google Drive
from pydrive.drive import GoogleDrive  # Para interactuar con Google Drive
import dropbox  # Para interactuar con Dropbox

# Función para cargar el archivo de configuración en formato JSON
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

# Función para autenticar con Google Drive
def authenticate_google_drive():
    gauth = GoogleAuth()  # Crear objeto de autenticación para Google
    gauth.LocalWebserverAuth()  # Realizar autenticación usando un servidor web local
    return GoogleDrive(gauth)  # Retornar una instancia de GoogleDrive autenticada

# Función para autenticar con Dropbox usando un token de acceso
def authenticate_dropbox(token):
    return dropbox.Dropbox(token)  # Retorna una instancia de Dropbox autenticada

# Función para subir un archivo a Google Drive
def upload_to_google_drive(drive, file_path):
    # Extraemos el nombre del archivo de su ruta
    file_name = file_path.split("/")[-1]
    # Creamos un objeto de archivo en Google Drive con el nombre dado
    file = drive.CreateFile({'title': file_name})
    # Establecemos el contenido del archivo a subir
    file.SetContentFile(file_name)
    # Subimos el archivo a Google Drive
    file.Upload()
    print(f"Uploaded {file_name} to Google Drive")  # Mensaje de confirmación

# Función para subir un archivo a Dropbox
def upload_to_dropbox(dbx, file_path):
    with open(file_path, "rb") as f:  # Abrimos el archivo en modo binario
        # Subimos el archivo a Dropbox, reemplazando si ya existe
        dbx.files_upload(f.read(), f"/{os.path.basename(file_path)}", mode=dropbox.files.WriteMode("overwrite"))
    print(f"Uploaded {file_path} to Dropbox")  # Mensaje de confirmación

# Función para eliminar archivos antiguos que superan el tiempo de retención especificado
def clean_old_files():
    config = load_config()  # Cargamos la configuración
    retention_days = config.get("retention_days", 7)  # Número de días a conservar los archivos
    now = datetime.datetime.now()  # Obtenemos la fecha y hora actuales
    # Recorremos todos los archivos en la carpeta de backups
    for file in os.listdir(config["backup_folder"]):
        file_path = os.path.join(config["backup_folder"], file)
        # Obtenemos la fecha de creación del archivo
        file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        # Si el archivo tiene más de los días permitidos de retención, lo eliminamos
        if (now - file_time).days > retention_days:
            os.remove(file_path)  # Eliminamos el archivo
            print(f"Deleted old backup: {file}")  # Mensaje de confirmación

# Función principal de respaldo que se ejecuta para realizar el proceso de backup
def backup():
    config = load_config()  # Cargamos la configuración
    drive, dbx = None, None  # Inicializamos las variables de Google Drive y Dropbox como None
    
    # Si en la configuración se habilita Google Drive, autenticamos
    if config.get("use_google_drive", False):
        drive = authenticate_google_drive()
    # Si en la configuración se habilita Dropbox, autenticamos
    if config.get("use_dropbox", False):
        dbx = dropbox.Dropbox(config["dropbox_token"])
    
    # Subimos los archivos especificados en la configuración a los servicios correspondientes
    for file in config["files_to_backup"]:
        if drive:
            upload_to_google_drive(drive, file)  # Subimos a Google Drive
        if dbx:
            upload_to_dropbox(dbx, file)  # Subimos a Dropbox
    
    # Limpiamos los archivos antiguos según la configuración
    clean_old_files()

# Configuración inicial del programa
config = load_config()  # Cargamos la configuración

# Programamos la tarea de backup para que se ejecute automáticamente cada cierto número de horas
schedule.every(config.get("backup_interval", 24)).hours.do(backup)

# Bucle principal que ejecuta las tareas programadas
while True:
    schedule.run_pending()  # Ejecuta las tareas programadas que estén pendientes
    time.sleep(60)  # Espera 60 segundos antes de comprobar de nuevo
