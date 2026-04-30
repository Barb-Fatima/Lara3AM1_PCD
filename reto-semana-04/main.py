"""
Sistema de Inventario Modular - Reto Semana 4:
Implementar un sistema de inventario modular con una estructura de carpetas especifica, usando clases y validaciones.
Programacion para Ciencia de Datos - IPN
Lara Herrera Barbara Fatima. 3AM1
"""

from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

# Configuración
ARCHIVO_INVENTARIO = "data/inventario.csv"
ARCHIVO_REPORTE = "outputs/reporte_inventario.csv"


def crear_productos(datos_raw):
    # Convierte lista de diccionarios en objetos Producto
    productos = []

    for datos in datos_raw:
        es_valido, error = validar_producto(
            datos.get('sku'),
            datos.get('nombre'),
            datos.get('categoria'),
            datos.get('precio'),
            datos.get('stock'),
            datos.get('stock_minimo')
        )

        if not es_valido:
            print(f"Ignorando registro inválido - {error}")
            continue

        producto = Producto(
            sku=datos['sku'],
            nombre=datos['nombre'],
            categoria=datos['categoria'],
            precio=float(datos['precio']),
            stock=int(datos['stock']),
            stock_minimo=int(datos['stock_minimo'])
        )
        productos.append(producto)

    return productos


def filtrar_necesitan_reorden(productos):
    return [p for p in productos if p.necesita_reorden()]


def ordenar_por_faltantes(productos):
    return sorted(productos, key=lambda p: p.unidades_faltantes(), reverse=True)


def main():
    print("SISTEMA DE INVENTARIO - Reporte de Reorden")
    print(f"\nLeyendo inventario de: {ARCHIVO_INVENTARIO}")
    datos_raw = leer_inventario(ARCHIVO_INVENTARIO)
    print(f"Registros leídos: {len(datos_raw)}")

    # Crear objetos Producto
    productos = crear_productos(datos_raw)
    print(f"\nProductos válidos: {len(productos)}")

    # Filtrar los que necesitan reorden
    necesitan_reorden = filtrar_necesitan_reorden(productos)
    print(f"\nProductos que necesitan reorden: {len(necesitan_reorden)}")

    # Ordenar por unidades faltantes
    necesitan_reorden = ordenar_por_faltantes(necesitan_reorden)

    # Imprimir los productos que necesitan reorden
    for p in necesitan_reorden:
        print(p)

    # Reporte
    escribir_reporte(necesitan_reorden, ARCHIVO_REPORTE)
    print(f"\nReporte guardado en: {ARCHIVO_REPORTE}")

if __name__ == "__main__":
    main()