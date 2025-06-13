from data.excel_loader import load_excel_data
from data.utils import normalize_text

def get_full_info(nombre):
    df = load_excel_data()
    if df is None:
        return None
    nombre = normalize_text(nombre)
    row = df[df["nombre_del_alumno"].str.contains(nombre)]
    if row.empty:
        return None
    info = row.iloc[0].to_dict()
    return "\n".join([f"*{k.replace('_',' ').title()}*: {v}" for k, v in info.items()])

def get_apoderado(nombre):
    df = load_excel_data()
    if df is None:
        return None
    nombre = normalize_text(nombre)
    row = df[df["nombre_del_alumno"].str.contains(nombre)]
    if row.empty:
        return None
    apoderado = row.iloc[0].get("nombre_del_apoderado", "No especificado")
    telefono = row.iloc[0].get("telefono_apoderado", "No disponible")
    return f"👤 *Apoderado*: {apoderado}\n📞 *Teléfono*: {telefono}"

def get_student_months(nombre):
    df = load_excel_data()
    if df is None:
        return None
    nombre = normalize_text(nombre)
    row = df[df["nombre_del_alumno"].str.contains(nombre)]
    if row.empty:
        return None
    return {
        "meses_en_ayux": row.iloc[0].get("meses_en_ayux", "No disponible"),
        "meses_pagados": row.iloc[0].get("meses_pagados", "No disponible"),
        "meses_pendientes": row.iloc[0].get("meses_pendientes", "No disponible")
    }
