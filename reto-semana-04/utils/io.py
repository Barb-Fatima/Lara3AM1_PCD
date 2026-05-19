# Funciones de lectura y escritura de archivos CSV

def leer_inventario(ruta_archivo):
    # lee el archivo csv y lo devuelve como un diciconario
    import csv
    productos_raw = []
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for num_linea, fila in enumerate(lector, start=2):
            # Fila ya tiene exactamente las columnas del encabezado
            # csv.DictReader ignora columnas extra automáticamente
            productos_raw.append(fila)
    
    return productos_raw

def escribir_reporte(productos, ruta_archivo):
    encabezados = [
        "sku", "nombre", "categoria", "stock_actual",
        "stock_minimo", "unidades_faltantes", "valor_inventario"
    ]

    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(','.join(encabezados) + '\n')

        for p in productos:
            linea = (f"{p.sku},{p.nombre},{p.categoria},{p.stock},"
                     f"{p.stock_minimo},{p.unidades_faltantes()},"
                     f"{p.valor_inventario():.2f}")
            archivo.write(linea + '\n')