import pandas as pd
import requests
from io import BytesIO
from .config import EXCEL_URL
from .utils import normalize_text

def normalize_columns(cols):
    return [normalize_text(c).replace(" ", "_") for c in cols]

def load_excel_data():
    try:
        response = requests.get(EXCEL_URL)
        response.raise_for_status()
        df = pd.read_excel(BytesIO(response.content))
        df.columns = normalize_columns(df.columns)
        df["nombre_del_alumno"] = df["nombre_del_alumno"].astype(str).apply(normalize_text)
        return df
    except Exception as e:
        print(f"[❌ ERROR] No se pudo cargar el Excel: {e}")
        return None
