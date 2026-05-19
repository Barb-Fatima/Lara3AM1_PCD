"""
Analizador de Ventas - Reto Semana 3:
Lee un CSV desde stdin y genera un reporte ordenado por ingreso (descendente).
Programacion para Ciencia de Datos - IPN
Lara Herrera Barbara Fatima. 3AM1
"""

import sys
import math

# Función para manejar los tipo de dato inf y nan
def valorValido(valor_str):
    # Intentar convertir a tipo de dato float
    try:
        num = float(valor_str)
        if math.isinf(num) or math.isnan(num):
            return False
        return True
    except ValueError:
        return False

def main():
    # Diccionario: clave = nombre del producto
    productos = {}
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()
        if not linea:
            continue

        # Saltar encabezados
        if primera_linea:
            primera_linea = False
            continue

        #extraer las primeras 4 columnas
        partes = linea.split(',')
        if len(partes) < 4:
            continue

        #tomar solo los primeros 4 valores y convertirlos a cadena
        producto = partes[1]
        cantidad_str = partes[2].strip()
        precio_str = partes[3].strip()

        # Validar cantidad
        if not valorValido(cantidad_str):
            continue
            
        # Validar precio
        if not valorValido(precio_str):
            continue

        # convertir cantidad y precio_unitario
        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
        except ValueError:
            continue #saltar linea si hay datos invalidos

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