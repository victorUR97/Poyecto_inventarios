def generar_reporte_excel(ruta_reporte):
    """Genera un reporte en Excel del inventario."""
    import pandas as pd
    from src.database import conectar_db

    conn = conectar_db()
    df = pd.read_sql("SELECT * FROM inventario", conn)
    df.to_excel(ruta_reporte, index=False)
    conn.close()
    print(f"Reporte generado: {ruta_reporte}")
