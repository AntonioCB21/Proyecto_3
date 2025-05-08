# 🤝 Guía de Contribución a AutoBackupScript

¡Gracias por tu interés en contribuir a **AutoBackupScript**! Este proyecto busca ofrecer una herramienta simple y funcional para automatizar copias de seguridad en la nube, y siempre hay espacio para mejorar. Aquí te dejamos una guía rápida para participar.

---

## 🚀 ¿Cómo contribuir?

1. **Haz un fork del repositorio**
   - Puedes hacerlo desde GitHub con un solo clic.

2. **Clona tu fork localmente**
    ```bash
    git clone https://github.com/tu_usuario/AutoBackupScript.git

3. **Crea una rama para tu cambio**
    ```bash
    git checkout -b mi-mejora

4. **Haz tus modificaciones y añade pruebas si es necesario**

5. **Haz un commit claro y descriptivo**
    ```bash
    git commit -m "Agrega soporte para OneDrive"

6. **Envía tu rama al repositorio remoto**
    ```bash
    git push origin mi-mejora

7. **Abre un Pull Request en el repositorio original describiendo tu cambio.**

## 🛠 Áreas interesantes para mejorar
Si no sabes por dónde empezar, aquí te dejamos algunas ideas para contribuir:

### 🔧 Funcionalidades técnicas
 - Añadir soporte para OneDrive u otros servicios en la nube.

 - Mejorar el sistema de programación con cronjobs desde el script.

 - Crear una versión con interfaz gráfica ligera usando Tkinter o PyQt.

 - Añadir registros de logs (archivos .log) para trazabilidad.

 - Implementar cifrado opcional para los archivos respaldados.

### 📄 Documentación
 - Mejorar el README con más ejemplos de uso.

 - Añadir diagramas de flujo o arquitectura.

 - Escribir documentación técnica de cada módulo.

### 🧪 Pruebas
 - Escribir tests unitarios usando pytest.

 - Crear mocks para simular interacciones con Google Drive y Dropbox.

## 📋 Requisitos para pull requests
- Código claro, comentado y funcional.

- Si agregas nuevas dependencias, actualiza requirements.txt.

- Evita subir archivos personales o credenciales.

- Asegúrate de que no rompes funcionalidades existentes.
