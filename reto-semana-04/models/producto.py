"""Modelo de dominio Producto."""

class Producto:
    """
    Representa un producto en el inventario.

    Attributes:
        sku (str): Identificador único
        nombre (str): Nombre del producto
        categoria (str): Categoría del producto
        precio (float): Precio unitario
        stock (int): Cantidad actual
        stock_minimo (int): Nivel mínimo de stock
    """

    def __init__(self, sku, nombre, categoria, precio, stock, stock_minimo):
        """
        Inicializa un nuevo producto.

        Args:
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
        """Determina si el producto necesita reorden."""
        return self.stock < self.stock_minimo

    def unidades_faltantes(self):
        """Unidades faltantes para alcanzar el stock mínimo."""
        if self.necesita_reorden():
            return self.stock_minimo - self.stock
        return 0

    def valor_inventario(self):
        """Valor monetario del inventario actual."""
        return self.precio * self.stock

    def __str__(self):
        """Representación legible."""
        estado = "[REORDEN]" if self.necesita_reorden() else "[OK]"
        return f"{estado} {self.sku}: {self.nombre} - Stock: {self.stock}/{self.stock_minimo}"

    def __repr__(self):
        """Representación técnica."""
        return (f"Producto('{self.sku}', '{self.nombre}', '{self.categoria}', "
                f"{self.precio}, {self.stock}, {self.stock_minimo})")