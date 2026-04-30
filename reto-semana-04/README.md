# Sistema de Inventario Modular - Reto Semana 4
# Lara Herrera Barbara Fatima. 3AM1

Sistema modular de gestión de inventario que procesa un archivo CSV con información de productos, valida los datos, identifica qué productos necesitan reorden (stock por debajo del mínimo) y genera un reporte ordenado por unidades faltantes.  

## Descripción

Este programa lee datos desde la entrada estándar (stdin) en formato CSV.  
Cada línea contiene:
- sku (str): Identificador único
- nombre (str): Nombre del producto
- categoria (str): Categoría del producto
- precio (float): Precio unitario
- stock (int): Cantidad actual
- stock_minimo (int): Nivel mínimo de stock

El programa procesa cada línea siguiendo estas reglas:
1. Formato del archivo
   - El archivo debe tener encabezados en la primera línea: sku,nombre, categoria,precio,stock,stock_minimo
   - Cada línea debe tener exactamente 6 columnas (separadas por coma)
   - Las líneas con número incorrecto de columnas son ignoradas

2. Validación de SKU
   - No puede estar vacío
   - No puede ser solo espacios en blanco
   - Si es inválido → se ignora el registro completo

3. Validación de nombre
   - No puede estar vacío
   - No puede ser solo espacios en blanco
   - Si es inválido se ignora el registro completo

4. Validación de precio
   - Debe ser convertible a número decimal (float)
   - Debe ser mayor o igual a 0
   - Si es inválido se ignora el registro

5. Validación de stock
   - Debe ser convertible a número entero (int)
   - Debe ser mayor o igual a 0
   - Si hay valores inválidos se ignora el registro

6. Validación de stock mínimo
   - Debe ser convertible a número entero (int)
   - Debe ser mayor o igual a 0
   - Si hay valores inválidos se ignora el registro

7. Manejo de errores
   - Cuando un registro es inválido, se muestra un mensaje: "Ignorando registro inválido - razón"
   - El programa continúa procesando las líneas restantes
   - Los productos inválidos no se incluyen en el reporte final

8. Conversión de tipos
   - precio → convertido a float
   - stock → convertido a int
   - stock_minimo → convertido a int

9. Cálculo de necesidades de reorden
   - Un producto necesita reorden si: stock < stock_minimo
   - Se calculan las unidades_faltantes = stock_minimo - stock (solo si necesita reorden)

10. Ordenamiento del reporte
   - Los productos que necesitan reorden se ordenan de mayor a menor según unidades_faltantes

## Ejemplos

### Entrada:
fsku,nombre,categoria,precio,stock,stock_minimo  
SKU00001,Notebook Acer,Electronica,13098.61,45,25  
SKU00002,Teclado Mecanico TP-Link,Accesorios,869.72,86,30  
SKU00003,Mouse Gaming Epson,Accesorios,725.53,14,5  
SKU00004,Monitor Gaming HP,Electronica,22879.96,2,5  
SKU00005,Audifonos Bluetooth Dell,Audio,939.54,12,30  

### Salida en consola:
SISTEMA DE INVENTARIO - Reporte de Reorden  
Leyendo inventario de: data/inventario.csv  
Registros leídos: 5  
Productos válidos: 5  
Productos que necesitan reorden: 2  
SKU00004: Monitor Gaming HP - Stock: 2/5  
SKU00005: Audifonos Bluetooth Dell - Stock: 12/30  
Reporte guardado en: outputs/reporte_inventario.csv  

### Salida del reporte:
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario  
SKU00004,Monitor Gaming HP,Electronica,2,5,3,45759.92  
SKU00005,Audifonos Bluetooth Dell,Audio,12,30,18,11274.48  

### Entrada con datos inválidos:
sku,nombre,categoria,precio,stock,stock_minimo  
SKU00001,Notebook Acer,Electronica,13098.61,45,25  
SKU00002,Teclado Mecanico TP-Link,Accesorios,869.72,86,30  
SKU00003,Mouse Gaming Epson,Accesorios,725.53,14,5  
SKU00004,Monitor Gaming HP,Electronica,22879.96,2,5  
SKU00005,Audifonos Bluetooth Dell,Audio,939.54,12,???  
SKU00006,USB Drive Kingston,Almacenamiento,157.26,18,25  
SKU00007,Microfono USB TP-Link,Audio,1300.31,sin_dato,30  
SKU00008,HDD WD,Almacenamiento,2602.18  
SKU00009,Monitor 4K Lenovo,Electronica,10931.78,5,5  
SKU00010,Teclado Gaming Lenovo,Accesorios,3808.51,mil,20  

### Salida en consola (ignora líneas inválidas):
SISTEMA DE INVENTARIO - Reporte de Reorden  
Leyendo inventario de: data/inventario.csv  
Registros leídos: 9  
Ignorando registro inválido - Stock mínimo inválido: ???  
Ignorando registro inválido - Stock inválido: sin_dato  
Ignorando registro inválido - SKU vacío o inválido  
Ignorando registro inválido - Stock inválido: mil  
Productos válidos: 5  
Productos que necesitan reorden: 1  
SKU00004: Monitor Gaming HP - Stock: 2/5  
Reporte guardado en: outputs/reporte_inventario.csv  

### Salida del reporte (ignora líneas inválidas):
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario  
SKU00004,Monitor Gaming HP,Electronica,2,5,3,45759.92  

### Entrada sin productos que necesiten reorden:
sku,nombre,categoria,precio,stock,stock_minimo  
SKU00001,Notebook Acer,Electronica,13098.61,50,25  
SKU00002,Teclado Mecanico TP-Link,Accesorios,869.72,40,30  
SKU00003,Mouse Gaming Epson,Accesorios,725.53,20,5  
SKU00004,Monitor Gaming HP,Electronica,22879.96,10,5  

### Salida en consola:
SISTEMA DE INVENTARIO - Reporte de Reorden  
Leyendo inventario de: data/inventario.csv  
Registros leídos: 4  
Productos válidos: 4  
Productos que necesitan reorden: 0  
Reporte guardado en: outputs/reporte_inventario.csv  

### Salida del reporte (vacío, solo encabezados):
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario  

## Clonar el repositorio:
git clone https://github.com/Barb-Fatima/Lara3AM1_PCD.git