import pandas as pd
from src.database import conectar_db

def limpiar_tabla_inventario():
    """Elimina todos los datos existentes en la tabla 'inventario'."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventario;")
    conn.commit()
    conn.close()
    print("Datos antiguos eliminados correctamente.")

def cargar_inventario_desde_excel(ruta_excel):
    """Cargar datos de inventario desde un archivo Excel."""
    limpiar_tabla_inventario()  # Elimina los datos antiguos
    df = pd.read_excel(ruta_excel)
    conn = conectar_db()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO inventario (producto, categoria, stock, precio, stock_minimo)
            VALUES (%s, %s, %s, %s, %s);
        """, (row['producto'], row['categoria'], row['stock'], row['precio'], row['stock_minimo']))
    conn.commit()
    conn.close()
    print("Datos cargados correctamente.")

