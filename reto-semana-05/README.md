# Analizador de Ventas - Reto Semana 3
# Lara Herrera Barbara Fatima. 3AM1

Programa que procesa transacciones de ventas de una tienda de tecnología, consolida los datos por producto y genera un reporte con métricas clave ordenado por ingreso total.

## Descripción

Este programa lee datos desde la entrada estándar (stdin) en formato CSV. Cada línea contiene:
- Fecha de la venta (YYYY-MM-DD)
- Nombre del producto
- Cantidad vendida (entero)
- Precio unitario (decimal)

El programa procesa cada línea siguiendo estas reglas:
1. Ignora la primera línea (encabezados)
2. Agrupa todas las transacciones del mismo producto
3. Calcula por producto:
   - Unidades vendidas: suma de todas las cantidades
   - Ingreso total: suma de (cantidad × precio) de cada transacción
   - Precio promedio: ingreso total / unidades vendidas
4. Ordena los productos por ingreso total de mayor a menor
5. Ignora líneas con datos inválidos (cantidad no numérica, precio no numérico, formato incorrecto)
6. Muestra los valores monetarios con 2 decimales

## Ejemplos

### Entrada:
fecha,producto,cantidad,precio_unitario  
2026-01-01,Laptop,2,15000.00  
2026-01-02,Mouse,10,250.00  
2026-01-03,Laptop,1,14500.00  
2026-01-04,Teclado,5,800.00  
2026-01-05,Mouse,8,250.00  

### Salida:
producto,unidades_vendidas,ingreso_total,precio_promedio  
Laptop,3,44500.00,14833.33  
Mouse,18,4500.00,250.00  
Teclado,5,4000.00,800.00  


### Entrada con datos inválidos:
fecha,producto,cantidad,precio_unitario  
2026-01-01,Laptop,2,15000.00  
2026-01-02,Mouse,abc,250.00  
2026-01-03,Teclado,5,invalid  
2026-01-04,Laptop,1,14500.00  
linea,incompleta  

### Salida (ignora líneas inválidas):
producto,unidades_vendidas,ingreso_total,precio_promedio  
Laptop,3,44500.00,14833.33  

### Entrada con producto único:
fecha,producto,cantidad,precio_unitario  
2026-01-01,Monitor,1,5000.00  

### Salida:
producto,unidades_vendidas,ingreso_total,precio_promedio  
Monitor,1,5000.00,5000.00  

## Clonar el repositorio:
git clone https://github.com/Barb-Fatima/Lara3AM1_PCD.git