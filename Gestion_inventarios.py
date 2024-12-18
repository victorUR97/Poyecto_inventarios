from src.database import inicializar_db
from src.etl import cargar_inventario_desde_excel
from src.reporting import generar_reporte_excel
from src.alerts import generar_alertas_stock

def main():
    inicializar_db()

    while True:
        print("\n--- MENÚ DE GESTIÓN DE INVENTARIOS ---")
        print("1. Cargar inventario desde Excel")
        print("2. Generar reporte en Excel")
        print("3. Mostrar alertas de stock bajo")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ruta = input("Ingresa la ruta del archivo Excel: ")
            cargar_inventario_desde_excel(ruta)
            print("Datos cargados correctamente.")
        elif opcion == "2":
            ruta_reporte = "reports/reporte_inventario.xlsx"
            generar_reporte_excel(ruta_reporte)
        elif opcion == "3":
            generar_alertas_stock()
        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
