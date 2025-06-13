from data.excel_loader import load_excel_data
from data.utils import normalize_text

def get_all_categories():
    df = load_excel_data()
    if df is None:
        return []
    return list(zip(df["nombre_del_alumno"], df["categoria"].fillna("Sin categoría")))

def get_category_by_name(nombre):
    df = load_excel_data()
    if df is None:
        return None
    nombre = normalize_text(nombre)
    row = df[df["nombre_del_alumno"].str.contains(nombre)]
    return row.iloc[0]["categoria"] if not row.empty else None

def get_by_category(cat):
    df = load_excel_data()
    if df is None:
        return []
    return df[df["categoria"].fillna("").str.lower() == cat.lower()]["nombre_del_alumno"].tolist()
