import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

def conectar_db():
    """Conexión segura a la base de datos MySQL."""
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=3307,
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")

    )

def inicializar_db():
    """Asegura que la tabla de inventario exista."""
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            producto VARCHAR(255) NOT NULL,
            categoria VARCHAR(255),
            stock INT DEFAULT 0,
            precio DECIMAL(10,2),
            stock_minimo INT DEFAULT 10
        );
    """)
    conn.commit()
    conn.close()

    
