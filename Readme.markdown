# 🤖 Proyecto: Bot de Consultas Académicas vía Telegram con Excel + Python

Este repositorio contiene un bot de Telegram desarrollado originalmente para **Academia AYUX**, una academia de fútbol, con el objetivo de automatizar la consulta de datos académicos mediante archivos Excel y procesamiento en Python.

---

## 📝 Descripción

Diseñado para permitir a los administradores consultar en tiempo real información crítica sin necesidad de abrir manualmente archivos ni depender de plataformas externas.

💡 Este sistema resuelve un problema común en academias deportivas, centros educativos y organizaciones pequeñas: acceder rápidamente a datos almacenados en Excel, sin necesidad de infraestructura compleja ni conocimientos técnicos avanzados.

📱 El bot funciona directamente desde cualquier celular mediante Telegram, facilitando el acceso a información clave como pagos, estado de alumnos, categorías y meses cursados, desde cualquier lugar.

---

## 🔧 Estructura del Sistema

El proyecto está dividido en dos bloques principales:

- 🗃️ **Módulos en Python** que extraen, filtran y organizan los datos desde un archivo Excel utilizando la librería `pandas`.
- 🤖 **Bot de Telegram** que interpreta los comandos del usuario y responde con los datos consultados.

---

## 🔐 Seguridad

El sistema utiliza un archivo `.env` para gestionar variables sensibles como:

- El token del bot de Telegram
- Los IDs de usuarios autorizados

Esto asegura que solo personas con permisos específicos puedan acceder a la información.

---

## 🧩 Adaptabilidad

Este proyecto es completamente modular y personalizable. Aunque fue creado para **Academia AYUX**, puede adaptarse fácilmente a otras academias deportivas, centros educativos, o cualquier institución que maneje información en archivos Excel.

---

## 🚀 ¿Listo para implementarlo?

Puedes utilizar este repositorio como base para tu propio bot académico. Personaliza el archivo de Excel, ajusta los comandos y modifica los módulos según las necesidades de tu organización.

---

## 📦 Requisitos

- Python 3.9 o superior
- Entorno virtual (recomendado)
- Archivo `.env` con credenciales
- URL de archivo Excel actualizado
- Token del bot de Telegram y chat autorizado

---

## 🗂️ Estructura del Proyecto

```
telegram-edu-bot-template/
│
├── bot.py                 # Archivo principal que gestiona el bot
├── data/
│   └── sheet_utils.py     # Funciones generales para manejo de Excel
│
├── modules/
│   ├── bienvenida.py      # Mensaje de bienvenida
│   ├── estado.py          # Funciones relacionadas al estado de alumnos
│   ├── pagos.py           # Funciones de pagos
│   ├── categorias.py      # Funciones por categoría
│   ├── resumen.py         # Función resumen general
│   ├── info.py            # Información detallada y apoderado
│   └── meses.py           # Meses en AYUX, pagados, pendientes
│
├── .env                   # Variables sensibles (NO se sube al repo)
├── .gitignore             # Ignora venv, .env, __pycache__, etc.
├── requirements.txt       # Librerías requeridas
└── README.md              # Este archivo
```

---

## 🛠️ Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/4wful/telegram-edu-bot-template.git
   cd telegram-edu-bot-template
   ```

2. Crea y activa el entorno virtual:

   **Windows**:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea el archivo `.env` con tus credenciales:

   ```env
   TELEGRAM_BOT_TOKEN=tu_token_aqui
   AUTHORIZED_CHAT_ID=123456789
   EXCEL_URL=https://link-al-archivo.xlsx
   ```

5. Ejecuta el bot:

   ```bash
   python bot.py
   ```

---

## ✅ Comandos disponibles

| Comando                  | Descripción                                                  |
|--------------------------|--------------------------------------------------------------|
| `/start`                 | Muestra un mensaje de bienvenida con las opciones disponibles|
| `/estado_todos`          | Lista el estado de todos los alumnos                        |
| `/estado [nombre]`       | Muestra el estado de un alumno específico                   |
| `/pagos`                 | Lista todos los pagos registrados                           |
| `/pago [nombre]`         | Muestra el pago individual de un alumno                     |
| `/pendientes`            | Lista los alumnos con pagos pendientes                      |
| `/categoria [nombre]`    | Muestra la categoría de un alumno                           |
| `/por_categoria [nombre]`| Lista los alumnos de una categoría específica               |
| `/info [nombre]`         | Muestra toda la información registrada de un alumno         |
| `/apoderado [nombre]`    | Muestra los datos del apoderado de un alumno                |
| `/resumen`               | Muestra un resumen general del estado de todos los alumnos  |
| `/meses [nombre]`        | Muestra meses en AYUX, pagados y pendientes de un alumno     |

---

## 🖼️ Vista Preliminar

A continuación, una vista del bot funcionando en Telegram:

![vista preliminar del bot](https://via.placeholder.com/700x400.png?text=Ejemplo+de+uso+del+Bot+AYUX)

---

## 📄 Licencia

Este proyecto es de uso interno para la gestión académica de AYUX. Uso externo no autorizado.

Desarollado por Güido Maidana Ingeniero de Sistemas

