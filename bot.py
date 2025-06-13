import os
import time
import requests
from dotenv import load_dotenv

#Importar Modulos y sus funciones
from modules.welcome import get_welcome_message
from modules.status import get_all_student_status, get_student_status
from modules.payments import (
    get_all_payments,
    get_student_payment,
    get_pending_payments,
    get_total_payment,
)
from modules.categories import (
    get_all_categories,
    get_category_by_name,
    get_by_category,
)
from modules.info import (
    get_full_info,
    get_apoderado,
    get_student_months,
)
from modules.resumen import get_resumen_general

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_URL = f"https://api.telegram.org/bot{TOKEN}"
AUTHORIZED_CHAT_IDS = os.getenv("AUTHORIZED_CHAT_ID", "")
AUTHORIZED_CHAT_IDS = [x.strip() for x in AUTHORIZED_CHAT_IDS.split(",") if x.strip()]

last_update_id = None

def send_message(text, chat_id):
    try:
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        r = requests.post(f"{BOT_URL}/sendMessage", data=payload)
        if r.status_code != 200:
            print("❌ Error al enviar:", r.text)
    except Exception as e:
        print(f"❌ Excepción al enviar mensaje: {e}")

def handle_command(text, chat_id, user_name):
    cmd = text.lower().strip()

    if cmd.startswith("/start"):
        send_message(get_welcome_message(user_name), chat_id)

    elif cmd.startswith("/estado_todos"):
        estados = get_all_student_status()
        msg = (
            "📋 *Estado de todos los alumnos:*\n\n"
            + "\n".join([f"• {a}: {e}" for a, e in estados])
            if estados else "⚠️ No se pudo obtener el estado."
        )
        send_message(msg, chat_id)

    elif cmd.startswith("/estado "):
        nombre = cmd.replace("/estado", "").strip()
        estado = get_student_status(nombre)
        msg = (
            f"📌 *Estado de {nombre}*: {estado}"
            if estado else f"⚠️ No se encontró al alumno: {nombre}."
        )
        send_message(msg, chat_id)

    elif cmd.startswith("/pagos"):
        pagos = get_all_payments()
        msg = (
            "💰 *Pagos registrados:*\n\n"
            + "\n".join([f"• {a}: {p}" for a, p in pagos])
            if pagos else "⚠️ No se pudo obtener la información de pagos."
        )
        send_message(msg, chat_id)

    elif cmd.startswith("/pago "):
        nombre = cmd.replace("/pago", "").strip()
        pago = get_student_payment(nombre)
        msg = (
            f"💳 *Pago de {nombre}*: {pago}"
            if pago else f"⚠️ No se encontró al alumno: {nombre}."
        )
        send_message(msg, chat_id)

    elif cmd.startswith("/pendientes"):
        pendientes = get_pending_payments()
        msg = (
            "⏳ *Alumnos con pagos pendientes:*\n\n"
            + "\n".join([f"• {a}: {p}" for a, p in pendientes])
            if pendientes else "✅ Todos los pagos están al día."
        )
        send_message(msg, chat_id)

    elif cmd.startswith("/categoria "):
        nombre = cmd.replace("/categoria", "").strip()
        cat = get_category_by_name(nombre)
        msg = (
            f"🏷️ *Categoría de {nombre}*: {cat}"
            if cat else f"⚠️ No se encontró al alumno: {nombre}."
        )
        send_message(msg, chat_id)

    elif cmd.startswith("/por_categoria "):
        cat = cmd.replace("/por_categoria", "").strip()
        alumnos = get_by_category(cat)
        msg = (
            f"👥 *Alumnos en la categoría {cat}:*\n\n"
            + "\n".join([f"• {a}" for a in alumnos])
            if alumnos else f"⚠️ No se encontraron alumnos en la categoría: {cat}."
        )
        send_message(msg, chat_id)

    elif cmd.startswith("/info "):
        nombre = cmd.replace("/info", "").strip()
        info = get_full_info(nombre)
        msg = (
            f"📄 *Información completa de {nombre}:*\n\n{info}"
            if info else f"⚠️ No se encontró al alumno: {nombre}."
        )
        send_message(msg, chat_id)

    elif cmd.startswith("/apoderado "):
        nombre = cmd.replace("/apoderado", "").strip()
        if not nombre:
            send_message(
                "❗ Escribe el nombre del alumno. Ejemplo: /apoderado Luis Ramos",
                chat_id,
            )
        else:
            ap_info = get_apoderado(nombre)
            msg = (
                ap_info
                if ap_info else f"⚠️ No se encontró al alumno: {nombre}."
            )
            send_message(msg, chat_id)

    elif cmd.startswith("/resumen"):
        resumen = get_resumen_general()
        send_message(resumen, chat_id)

    elif cmd.startswith("/meses "):
        nombre = cmd.replace("/meses", "").strip()
        datos = get_student_months(nombre)
        if datos:
            msg = (
                f"🗓️ *Meses de {nombre}:*\n"
                f"• En AYUX: {datos['meses_en_ayux']}\n"
                f"• Pagados: {datos['meses_pagados']}\n"
                f"• Pendientes: {datos['meses_pendientes']}"
            )
        else:
            msg = f"⚠️ No se encontró al alumno: {nombre}."
        send_message(msg, chat_id)

    else:
        send_message(
            "❓ *Comando no reconocido.* Usa /start para ver todas las opciones disponibles.",
            chat_id,
        )

print("🤖 Bot de academia activo...")

while True:
    try:
        url = f"{BOT_URL}/getUpdates"
        if last_update_id:
            url += f"?offset={last_update_id + 1}"

        r = requests.get(url)
        data = r.json()

        updates = data.get("result", [])
        for update in updates:
            update_id = update["update_id"]
            message = update.get("message", {})
            text = message.get("text", "")
            chat_id = str(message.get("chat", {}).get("id", ""))
            user_name = message.get("from", {}).get("first_name", "Usuario")

            print(f"Recibido update_id={update_id} chat_id={chat_id} user={user_name} texto={text}")

            if chat_id not in AUTHORIZED_CHAT_IDS:
                send_message("⛔ No tienes permiso para usar este bot.", chat_id)
                last_update_id = update_id
                continue

            if text:
                handle_command(text, chat_id, user_name)

            last_update_id = update_id

    except Exception as e:
        print(f"[ERROR LOOP] {e}")

    time.sleep(3)



