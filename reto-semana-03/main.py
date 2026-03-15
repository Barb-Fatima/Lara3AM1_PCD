import sys

def main():
    """
    Analizador de Ventas: Lee un CSV desde stdin, consolida las ventas por producto,
    calcula unidades, ingreso total y precio promedio, y genera un reporte ordenado
    por ingreso descendente.
    """
    # Diccionario para agrupar los datos: clave = nombre del producto
    # Valor = diccionario con 'unidades' (int) e 'ingreso' (float)
    productos = {}

    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        # Saltar la primera línea (encabezados)
        if primera_linea:
            primera_linea = False
            continue

        # Ignorar líneas vacías
        if not linea:
            continue

        # Dividir la línea por comas
        partes = linea.split(',')

        # Regla 5: Ignorar líneas con menos de 4 columnas
        if len(partes) != 4:
            continue

        producto = partes[1]

        # Intentar convertir cantidad y precio_unitario
        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
        except ValueError:
            # Si la conversión falla, ignorar la línea (dato inválido)
            continue

        # --- Regla 1: Agrupar por producto ---
        # Si el producto no existe en el diccionario, inicializarlo
        if producto not in productos:
            productos[producto] = {'unidades': 0, 'ingreso': 0.0}

        # --- Regla 2: Calcular métricas (acumular) ---
        productos[producto]['unidades'] += cantidad
        productos[producto]['ingreso'] += cantidad * precio

    # --- Calcular precio promedio por producto ---
    # Nota: Se añade una nueva clave 'promedio' al diccionario de cada producto
    for datos in productos.values():
        unidades = datos['unidades']
        ingreso = datos['ingreso']
        # Evitar división por cero (aunque no debería ocurrir con datos válidos)
        datos['promedio'] = ingreso / unidades if unidades > 0 else 0.0

    # --- Regla 3: Ordenar por ingreso total (descendente) ---
    # Convertimos los items del diccionario a una lista y ordenamos
    productos_ordenados = sorted(
        productos.items(),           # items() da tuplas (producto, diccionario)
        key=lambda item: item[1]['ingreso'],  # Ordenar por 'ingreso'
        reverse=True                 # Orden descendente
    )

    # --- Regla 4: Generar salida CSV con formato ---
    # Imprimir encabezado
    print('producto,unidades_vendidas,ingreso_total,precio_promedio')

    # Imprimir cada producto
    for nombre, datos in productos_ordenados:
        # Formatear ingreso_total y precio_promedio con 2 decimales
        # unidades_vendidas se imprime como entero (sin decimales)
        print(f"{nombre},{datos['unidades']},{datos['ingreso']:.2f},{datos['promedio']:.2f}")

if __name__ == "__main__":
    main()