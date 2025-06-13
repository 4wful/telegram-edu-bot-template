def get_welcome_message(user_name):
    return (
        f"👋 ¡Bienvenido/a *{user_name}* al *Bot de la Academia AYUX*!\n\n"
        "📋 *Comandos disponibles:*\n\n"
        "📌 *Estados y Pagos:*\n"
        "• /estado\\_todos – Estado de todos los alumnos\n"
        "• /estado [nombre] – Estado de un alumno\n"
        "• /pagos – Todos los pagos registrados\n"
        "• /pago [nombre] – Pago de un alumno\n"
        "• /pendientes – Alumnos con pagos pendientes\n"
        "• /meses [nombre] – Meses en AYUX, pagados y pendientes\n\n"
        "📚 *Información Académica:*\n"
        "• /categoria [nombre] – Categoría de un alumno\n"
        "• /por\\_categoria [nombre_categoria] – Alumnos por categoría\n"
        "• /info [nombre] – Información completa de un alumno\n"
        "• /apoderado [nombre] – Ver datos del apoderado\n\n"
        "📊 *Resumen General:*\n"
        "• /resumen – Estadísticas y categorías"
    )

