# 💾 AutoBackupScript

AutoBackupScript is a minimal, lightweight Python tool that automates cloud backups of selected files and folders. It's designed for users and developers who need a hassle-free, open-source backup solution without graphical interfaces or complex setups.

---

## 🚀 Motivation

In the age of remote work and distributed systems, data loss due to accidents or lack of backups is still common. AutoBackupScript was created to offer:

- 🔄 Automatic cloud backup scheduling.
- ☁️ Support for Google Drive and Dropbox.
- ♻️ Automatic deletion of old versions.
- 🧩 Easy integration and modification.

---

## 📦 Features

- ✅ Backup selected files/folders to the cloud.
- 🔐 Avoid duplicates by checking existing uploads.
- 🧹 Auto-delete outdated versions (optional).
- 🛠 Easy configuration via `config.json`.
- 🕒 Run manually or schedule with `cron` or Task Scheduler.
- 🧪 Simulated demo interface with [Streamlit](https://streamlit.io/).

---

## 🧪 Live Demo

Test a simulated interface of AutoBackupScript online:

👉 [**Launch Demo on Streamlit Cloud**](https://auto-backup-demo.streamlit.app/) ← *replace with your link*

> ⚠️ Files are not uploaded in the demo – it's a visual simulation only.

---

## 🖥️ Installation

### 1. Install Python 3

Download from [https://www.python.org](https://www.python.org). During installation, check the **"Add Python to PATH"** option.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/AutoBackupScript.git
cd AutoBackupScript
