"""
Analizador de Ventas - Reto Semana 3:
Lee un CSV desde stdin y genera un reporte ordenado por ingreso (descendente).
Programacion para Ciencia de Datos - IPN
Lara Herrera Barbara Fatima. 3AM1
"""

import sys

def main():
    # Diccionario: clave = nombre del producto
    productos = {}

    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        # Saltar encabezados
        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        partes = linea.split(',')

        # Ignorar líneas con menos de 4 columnas
        if len(partes) != 4:
            continue

        producto = partes[1]

        # convertir cantidad y precio_unitario
        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
        except ValueError:
            # dato inválido
            continue

        # Agrupar por producto. Si el producto no existe en el diccionario, inicializarlo
        if producto not in productos:
            productos[producto] = {'unidades': 0, 'ingreso': 0.0}

        productos[producto]['unidades'] += cantidad
        productos[producto]['ingreso'] += cantidad * precio

    # Calcular precio promedio por producto
    # Se añade una nueva clave 'promedio' al diccionario de cada producto
    for datos in productos.values():
        unidades = datos['unidades']
        ingreso = datos['ingreso']
        # Evitar división por cero
        datos['promedio'] = ingreso / unidades if unidades > 0 else 0.0

    # Ordenar por ingreso total (descendente)
    # Convertimos los items del diccionario a una lista
    productos_ordenados = sorted(
        productos.items(),           # items() da tuplas (producto, diccionario)
        key=lambda item: item[1]['ingreso'],  # Ordenar por 'ingreso'
        reverse=True                 # Orden descendente
    )

    # Generar salida con formato csv
    print('producto,unidades_vendidas,ingreso_total,precio_promedio')

    # Imprimir cada producto
    for nombre, datos in productos_ordenados:
        print(f"{nombre},{datos['unidades']},{datos['ingreso']:.2f},{datos['promedio']:.2f}")

if __name__ == "__main__":
    main()