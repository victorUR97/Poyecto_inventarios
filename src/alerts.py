from src.database import conectar_db

def generar_alertas_stock():
    """Imprime una alerta para productos con stock bajo."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT producto, stock FROM inventario WHERE stock < stock_minimo;")
    alertas = cursor.fetchall()
    conn.close()

    if alertas:
        print("¡ALERTA! Los siguientes productos tienen stock bajo:")
        for producto, stock in alertas:
            print(f"- {producto}: {stock}")
    else:
        print("Todo está en orden con el inventario.")
