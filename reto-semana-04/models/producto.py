"""
sku (str): Identificador único
nombre (str): Nombre del producto
categoria (str): Categoría del producto
precio (float): Precio unitario
stock (int): Cantidad actual
stock_minimo (int): Nivel mínimo de stock
"""
class Producto:
    def __init__(self, sku, nombre, categoria, precio, stock, stock_minimo):
        """
        Inicializa un nuevo producto.
        sku: Identificador único
        nombre: Nombre del producto
        categoria: Categoría
        precio: Precio unitario (>=0)
        stock: Cantidad actual (>=0)
        stock_minimo: Nivel mínimo (>=0)
        """
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

    def necesita_reorden(self):
        # Determina si el producto necesita reorden
        return self.stock < self.stock_minimo

    def unidades_faltantes(self):
        # Realiza una resta para saber las unidades faltantes para alcanzar el stock mínimo
        if self.necesita_reorden():
            return self.stock_minimo - self.stock
        return 0

    def valor_inventario(self):
        # Valor total del inventario actual
        return self.precio * self.stock

    def __str__(self):
        # Impresión en la terminal de productos que necesitan reorden
        return f"{self.sku}: {self.nombre} - Stock: {self.stock}/{self.stock_minimo}"

    def __repr__(self):
        # Para programadores
        return (f"Producto('{self.sku}', '{self.nombre}', '{self.categoria}', "
                f"{self.precio}, {self.stock}, {self.stock_minimo})")