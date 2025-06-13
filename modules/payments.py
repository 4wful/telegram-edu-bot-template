from data.excel_loader import load_excel_data
from data.utils import normalize_text

def get_all_payments():
    df = load_excel_data()
    if df is None:
        return []
    return list(zip(df["nombre_del_alumno"], df["pago"].fillna("Sin dato")))

def get_student_payment(nombre):
    df = load_excel_data()
    if df is None:
        return None
    nombre = normalize_text(nombre)
    row = df[df["nombre_del_alumno"].str.contains(nombre)]
    return row.iloc[0]["pago"] if not row.empty else None

def get_pending_payments():
    df = load_excel_data()
    if df is None:
        return []
    df["pago"] = df["pago"].fillna("").str.lower()
    pendientes = df[~df["pago"].str.contains("canceló|pagado")]
    return list(zip(pendientes["nombre_del_alumno"], pendientes["pago"]))

def get_total_payment(nombre):
    df = load_excel_data()
    if df is None:
        return None
    nombre = normalize_text(nombre)
    row = df[df["nombre_del_alumno"].str.contains(nombre)]
    return row.iloc[0].get("total_pago", "No registrado") if not row.empty else None
