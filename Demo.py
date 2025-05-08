import streamlit as st
import datetime
import random

# Simulador de archivos para respaldo
sample_files = [
    {"name": "informe_final.docx", "size": "450 KB", "last_modified": "2024-05-01"},
    {"name": "factura_mayo.pdf", "size": "220 KB", "last_modified": "2024-05-03"},
    {"name": "respaldo_antiguo.zip", "size": "3.1 MB", "last_modified": "2024-03-15"},
    {"name": "presentacion.pptx", "size": "1.2 MB", "last_modified": "2024-04-20"},
    {"name": "proyecto_code.py", "size": "25 KB", "last_modified": "2024-05-06"},
]

st.title("🔐 AutoBackupScript - Demo Simulada")

st.markdown("""
Esta es una simulación del comportamiento de AutoBackupScript, un software que automatiza el respaldo de archivos en la nube (Google Drive / Dropbox).
""")

st.header("📂 Archivos detectados para respaldo")
st.table(sample_files)

# Selección de servicio
service = st.radio("Selecciona el servicio de respaldo simulado:", ["Google Drive", "Dropbox"])

# Simulación de respaldo
if st.button("Iniciar respaldo simulado"):
    with st.spinner("Procesando respaldo..."):
        st.success("✔ Archivos respaldados correctamente en " + service)
        st.balloons()

        st.markdown("### 🧹 Gestión automática de versiones antiguas")
        old_deleted = [f for f in sample_files if "respaldo" in f["name"].lower()]
        if old_deleted:
            st.warning(f"{len(old_deleted)} archivo(s) antiguo(s) han sido eliminados:")
            for f in old_deleted:
                st.markdown(f"- `{f['name']}` (última modificación: {f['last_modified']})")
        else:
            st.info("No se encontraron versiones antiguas para eliminar.")

# Footer
st.markdown("---")
st.caption("🔁 Esta es una simulación. No se realizan respaldos reales ni se accede a archivos locales.")
