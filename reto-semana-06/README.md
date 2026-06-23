# Validador de Códigos con Expresiones Regulares - Reto Semana 6
# Lara Herrera Barbara Fatima. 3AM1

Sistema de validación automática de códigos de productos, envíos, empleados y facturas utilizando expresiones regulares. El programa lee códigos desde la entrada estándar (stdin), detecta su tipo según el formato, aplica reglas de validación específicas y genera un reporte en formato CSV.  

## Descripción

Este programa lee líneas desde la entrada estándar (stdin), donde cada línea contiene un código a validar.  

### Tipos de códigos soportados

#### 1. Código de Producto
- Formato: ABC-1234-MX   
- Estructura: 3 letras + - + 4 dígitos + - + 2 letras  
- Validación: Categoría y país deben estar en MAYÚSCULAS  
- Ejemplos válidos: TEC-0001-MX, ALI-9999-US, ROB-1234-CA  

#### 2. Código de Envío
- Formato: ENV-YYYY-MM-DD-NNNNNN  
- Estructura: Prefijo ENV- + año + - + mes + - + día + - + 6 dígitos  
- Validación:  
  - Año: 2020-2030  
  - Mes: 01-12  
  - Día: 01-31  
- Ejemplos válidos: ENV-2024-03-15-001234, ENV-2025-12-01-999999  

#### 3. Código de Empleado
- Formato: EMP-XXX-NNNN  
- Estructura: Prefijo EMP- + 3 letras + - + 4 dígitos  
- Departamentos válidos: VEN (Ventas), ADM (Administración), TEC (Tecnología), LOG (Logística), RHH (Recursos Humanos)  
- Validación: Número NO puede empezar con 0  
- Ejemplos válidos: EMP-VEN-1234, EMP-TEC-9999, EMP-ADM-1000  

#### 4. Código de Factura
- Formato: FAC-X-NNNNNN  
- Estructura: Prefijo FAC- + 1 letra (serie) + - + 6 dígitos  
- Series válidas: A, B, C, D, E (solo mayúsculas)  
- Ejemplos válidos: FAC-A-123456, FAC-E-000001  

### Procesamiento

1. Detección de tipo: Se identifica por la estructura del código usando expresiones regulares  
   - Si la estructura coincide con algún formato → se asigna el tipo correspondiente  
   - Si no coincide con ningún formato → tipo desconocido  

2. Validación específica por tipo:  
   - Producto: Categoría y país en mayúsculas  
   - Envío: Rango de fechas válido (año 2020-2030, mes 1-12, día 1-31)  
   - Empleado: Departamento en lista válida, número sin cero inicial  
   - Factura: Serie en {A, B, C, D, E} en mayúscula  
   - Desconocido: Siempre inválido  

3. Manejo de líneas vacías: Las líneas vacías o con solo espacios se ignoran  

## Ejemplos

### Entrada (codigos.txt):
TEC-0001-MX  
ALI-9999-US  
tec-0001-MX  
TEC-001-MX  
ENV-2024-03-15-001234  
ENV-2019-03-15-001234  
EMP-VEN-1234  
EMP-VEN-0123  
FAC-A-123456  
FAC-F-123456  
XXX-1234  

### Salida
codigo,tipo,valido  
TEC-0001-MX,producto,VALIDO  
ALI-9999-US,producto,VALIDO  
tec-0001-MX,producto,INVALIDO  
TEC-001-MX,desconocido,INVALIDO  
ENV-2024-03-15-001234,envio,VALIDO  
ENV-2019-03-15-001234,envio,INVALIDO  
EMP-VEN-1234,empleado,VALIDO  
EMP-VEN-0123,empleado,INVALIDO  
FAC-A-123456,factura,VALIDO  
FAC-F-123456,factura,INVALIDO  
XXX-1234,desconocido,INVALIDO  

### Manejo de líneas vacías
TEC-0001-MX  

EMP-VEN-1234  

FAC-A-123456  

### Salida (líneas vacías ignoradas):
codigo,tipo,valido  
TEC-0001-MX,producto,VALIDO  
EMP-VEN-1234,empleado,VALIDO  
FAC-A-123456,factura,VALIDO  

## Requisitos técnicos
- Python: 3.6 o superior  
- Módulos: Solo se utiliza la biblioteca estándar (sys y re)  
- Sin dependencias externas  

## Instrucciones de uso:
1. Clonar el repositorio:  
git clone https://github.com/Barb-Fatima/Lara3AM1_PCD.git  
cd Lara3AM1_PCD/reto-semana-06  
2. Crear archivo de prueba:  
TEC-0001-MX  
ENV-2024-03-15-001234  
EMP-VEN-1234  
FAC-A-123456  
3. Ejecutar el programa:  
python main.py < codigos.txt  
4. Guardar resultados:  
python main.py < codigos.txt > resultados.csv  

## Clonar el repositorio:
git clone https://github.com/Barb-Fatima/Lara3AM1_PCD.git