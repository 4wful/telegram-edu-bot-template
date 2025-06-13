from data.excel_loader import load_excel_data
from data.utils import normalize_text

def get_all_student_status():
    df = load_excel_data()
    if df is None:
        return []
    return list(zip(df["nombre_del_alumno"], df["estado"].fillna("Desconocido")))

def get_student_status(nombre):
    df = load_excel_data()
    if df is None:
        return None
    nombre = normalize_text(nombre)
    row = df[df["nombre_del_alumno"].str.contains(nombre)]
    return row.iloc[0]["estado"] if not row.empty else None

