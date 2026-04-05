# Funciones de validación de datos

def validar_sku(sku):
    # Valida que el SKU no esté vacío
    if not sku or not str(sku).strip():
        return False
    return True


def validar_precio(precio):
    try:
        precio_num = float(precio)
        return precio_num >= 0
    except (ValueError, TypeError):
        return False


def validar_stock(stock):
    try:
        stock_num = int(stock)
        return stock_num >= 0
    except (ValueError, TypeError):
        return False


def validar_producto(sku, nombre, categoria, precio, stock, stock_minimo):
    # Valida todos los campos de un producto
    if not validar_sku(sku):
        return False, "SKU vacío o inválido"

    if not nombre or not str(nombre).strip():
        return False, "Nombre vacío"

    if not validar_precio(precio):
        return False, f"Precio inválido: {precio}"

    if not validar_stock(stock):
        return False, f"Stock inválido: {stock}"

    if not validar_stock(stock_minimo):
        return False, f"Stock mínimo inválido: {stock_minimo}"

    return True, None