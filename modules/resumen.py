from data.excel_loader import load_excel_data

def get_resumen_general():
    df = load_excel_data()
    if df is None:
        return "⚠️ No se pudo generar el resumen."

    total = len(df)

    estado_col = df["estado"].fillna("").str.lower()
    al_dia = len(df[estado_col == "al día"])
    pendiente = len(df[estado_col == "pendiente"])

    pago_col = df["pago"].fillna("").str.lower()
    pagos_pendientes = len(df[~pago_col.str.contains("canceló|pagado")])

    categorias = ", ".join(df["categoria"].dropna().unique())

    return (
        f"📊 *Resumen General*\n\n"
        f"👥 *Total alumnos*: {total}\n"
        f"✅ *Alumnos al día*: {al_dia}\n"
        f"⏳ *Alumnos pendientes*: {pendiente}\n"
        f"💸 *Pagos pendientes*: {pagos_pendientes}\n"
        f"🏷️ *Categorías registradas*: {categorias}"
    )
