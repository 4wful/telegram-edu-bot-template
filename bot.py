import os
import requests
from flask import Flask, request
from dotenv import load_dotenv

# Importar módulos
from modules.welcome import get_welcome_message
from modules.status import get_all_student_status, get_student_status
from modules.payments import (
    get_all_payments, get_student_payment, get_pending_payments, get_total_payment,
)
from modules.categories import (
    get_all_categories, get_category_by_name, get_by_category,
)
from modules.info import (
    get_full_info, get_apoderado, get_student_months,
)
from modules.resumen import get_resumen_general

load_dotenv()
app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_URL = f"https://api.telegram.org/bot{TOKEN}"
RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")  # esta variable la definirás en Render

AUTHORIZED_CHAT_IDS = os.getenv("AUTHORIZED_CHAT_ID", "")
AUTHORIZED_CHAT_IDS = [x.strip() for x in AUTHORIZED_CHAT_IDS.split(",") if x.strip()]

def send_message(text, chat_id):
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    requests.post(f"{BOT_URL}/sendMessage", data=payload)

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
            msg = ap_info if ap_info else f"⚠️ No se encontró al alumno: {nombre}."
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

@app.route("/", methods=["GET"])
def index():
    return "🤖 Bot AYUX activo vía webhook"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = str(data["message"]["chat"]["id"])
        text = data["message"].get("text", "")
        user_name = data["message"]["from"].get("first_name", "Usuario")

        if chat_id in AUTHORIZED_CHAT_IDS:
            handle_command(text, chat_id, user_name)
        else:
            send_message("⛔ No tienes permiso para usar este bot.", chat_id)
    return "OK"

def set_webhook():
    url = f"{BOT_URL}/setWebhook"
    webhook_url = f"{RENDER_URL}/"
    response = requests.post(url, data={"url": webhook_url})
    print("📡 Webhook registrado:", response.text)

if __name__ == "__main__":
    set_webhook()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))




