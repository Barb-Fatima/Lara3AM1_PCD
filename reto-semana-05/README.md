# Perfilador de Datasets - Reto Semana 5
# Lara Herrera Barbara Fatima. 3AM1

Herramienta que analiza automáticamente cualquier archivo CSV y genera un reporte de calidad de datos, incluyendo detección de tipos de datos, valores nulos, unicidad y ejemplos de valores.

## Descripción

El programa recibe como entrada un archivo CSV y produce un perfil detallado de cada columna.  
Es útil para explorar datasets desconocidos antes de realizar análisis más profundos.

### Parámetros de entrada (línea de comandos):
- `--input` o `-i`: Ruta al archivo CSV que se desea perfilar
- `--output` o `-o`: Ruta donde se guardará el reporte generado

### Formato del CSV de entrada:
- Primera fila: encabezados (nombres de columnas)
- Separador: coma `,`
- Codificación: UTF-8

### ¿Qué se calcula para cada columna?

| Columna de salida | Descripción |
|------------------|-------------|
| `nombre_columna` | Nombre de la columna analizada |
| `tipo_inferido` | Tipo detectado: `numerico`, `texto`, `fecha` o `booleano` |
| `total_registros` | Cantidad total de filas (sin contar encabezado) |
| `valores_nulos` | Cantidad de valores vacíos o nulos |
| `porcentaje_nulos` | Porcentaje de nulos (2 decimales) |
| `valores_unicos` | Cantidad de valores distintos (sin contar nulos) |
| `porcentaje_unicos` | Porcentaje de unicidad (2 decimales) |
| `ejemplo_valor` | Primer valor no nulo encontrado en la columna |

### Módulos de Python Utilizados en el Perfilador

El perfilador de datasets utiliza exclusivamente la **biblioteca estándar de Python**, sin dependencias externas.

#### 1. `argparse` - Gestión de argumentos de línea de comandos

Permite definir, parsear y validar los argumentos que el usuario pasa al ejecutar el script desde la terminal.  
La práctica requiere que el programa se ejecute así:
*python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv*  
argparse se encarga de:  
- Definir qué argumentos son obligatorios (required=True)
- Proveer mensajes de ayuda automáticos (--help o -h)
- Convertir los argumentos en atributos accesibles (args.input, args.output)
- Valida automáticamente que el usuario haya proporcionado los argumentos
- Genera mensaje de error claro si falta algún argumento
- Soporta nombres cortos (-i) y largos (--input)

#### 2. `sys` - Parámetros específicos del sistema

Proporciona acceso a variables y funciones interactuando directamente con el intérprete de Python y el sistema operativo.  
Controlar la terminación del programa cuando ocurre un error crítico.

**En el código:**  
sys.exit(0): Ejecución exitosa (sin errores).  
sys.exit(1): Ejecución con error (archivo no encontrado, datos inválidos, etc.)  

#### 3. `Path` (de `pathlib`) - Gestión de rutas
Es la forma "moderna" y multiplataforma de trabajar con rutas de archivos y directorios.  
Disponible desde Python 3.4 (2014), reemplaza la mayoría de las funciones de os.path.

### Reglas de procesamiento

#### 1. Detección de nulos
Se considera **nulo**:
- Celda vacía `,,`
- Celda con solo espacios `, ,`
- String vacío `""`

**NO** son nulos:
- El número `0`
- El string `"0"`
- Los strings `"null"` o `"None"`

#### 2. Inferencia de tipos
Se analizan los valores **no nulos** de cada columna:
- `numerico`: más del 80% de los valores pueden convertirse a float
- `fecha`: más del 80% tienen formato YYYY-MM-DD
- `booleano`: más del 80% son true/false/yes/no/si/1/0
- `texto`: cualquier otro caso

#### 3. Valores únicos
- Solo se cuentan valores **no nulos**
- Diferencia entre mayúsculas y minúsculas
- Cada valor distinto cuenta una vez

#### 4. Porcentajes
- Siempre con **2 decimales**
- Sin símbolo de porcentaje en el CSV
- Ejemplos: `0.00`, `25.50`, `100.00`

## Ejemplos

### Ejemplo 1: Datos de ventas

**Entrada (`data/ventas.csv`):**

fecha,producto,cantidad,precio,vendedor
2026-01-01,Laptop,2,15000.00,Ana
2026-01-02,Mouse,10,250.00,Bob
2026-01-03,Teclado,,800.00,Ana
2026-01-04,Monitor,3,,Carlos
2026-01-05,Laptop,1,15000.00,

**Comando en CMD:**

python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv

**Salida en consola:**

Columnas encontradas: 5
Registros: 5
Perfil guardado en: outputs/perfil_ventas.csv

**Salida (outputs/perfil_ventas.csv):**

nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
fecha,fecha,5,0,0.00,5,100.00,2026-01-01
producto,texto,5,0,0.00,4,80.00,Laptop
cantidad,numerico,5,1,20.00,4,80.00,2
precio,numerico,5,1,20.00,3,60.00,15000.00
vendedor,texto,5,1,20.00,3,60.00,Ana

### Ejemplo 2: Datos de empleados

**Entrada (`data/empleados.csv`):**

id,nombre,email,departamento,salario,activo
1,Ana Garcia,ana@empresa.com,TI,45000.00,true
2,Bob Lopez,,Ventas,38000.00,true
3,Carlos Ruiz,carlos@empresa.com,TI,52000.00,false
4,,diana@empresa.com,RRHH,41000.00,true
5,Eva Torres,eva@empresa.com,,47000.00,true

**Comando en CMD:**

python main.py --input data/empleados.csv --output outputs/perfil_empleados.csv

**Salida (outputs/perfil_empleados.csv):**

nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
id,numerico,5,0,0.00,5,100.00,1
nombre,texto,5,1,20.00,5,100.00,Ana Garcia
email,texto,5,1,20.00,5,100.00,ana@empresa.com
departamento,texto,5,0,0.00,3,60.00,TI
salario,numerico,5,0,0.00,5,100.00,45000.00
activo,booleano,5,0,0.00,2,40.00,true

### Ejemplo 3: Datos de sensores IoT

**Entrada (`data/sensores.csv`):**

timestamp,sensor_id,temperatura,humedad,bateria
2026-01-01 10:00:00,S001,23.5,65.2,98
2026-01-01 10:05:00,S001,23.7,64.8,98
2026-01-01 10:10:00,S002,22.1,,97
2026-01-01 10:15:00,S001,,65.5,97
2026-01-01 10:20:00,S003,25.2,70.1,

**Comando en CMD:**

python main.py --input data/sensores.csv --output outputs/perfil_sensores.csv

**Salida (`outputs/perfil_sensores.csv`):**

nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
timestamp,texto,5,0,0.00,5,100.00,2026-01-01 10:00:00
sensor_id,texto,5,0,0.00,3,60.00,S001
temperatura,numerico,5,1,20.00,4,80.00,23.5
humedad,numerico,5,1,20.00,4,80.00,65.2
bateria,numerico,5,1,20.00,2,40.00,98

### Ejemplo 4: Archivo vacío o sin datos

**Entrada (`archivo con solo encabezados`):**

id,nombre,precio

**Comando en CMD:**

python main.py --input data/vacio.csv --output outputs/perfil_vacio.csv

**Salida en consola:**

Columnas encontradas: 3
Registros: 0
Perfil guardado en: outputs/perfil_vacio.csv

**Salida (`outputs/perfil_vacio.csv`):**

nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
id,texto,0,0,0.00,0,0.00,
nombre,texto,0,0,0.00,0,0.00,
precio,texto,0,0,0.00,0,0.00,

### Ejemplo 5: Archivo no encontrado

**Comando en CMD:**

python main.py --input data/no_existe.csv --output outputs/perfil.csv

**Salida en consola:**

Error: No se encontro el archivo data/no_existe.csv

## Clonar el repositorio
git clone https://github.com/Barb-Fatima/Lara3AM1_PCD.git  
cd Lara3AM1_PCD/reto_semana_05

## Requisitos
**Python 3.6 o superior:**  
El formato de cadenas *f-strings* (`f"texto {variable}"`) fue introducido en Python 3.6

## Instalación y ejecución
1. Crear ambiente virtual  
python -m venv .venv

2. Activar ambiente virtual  
Windows:  
.venv\Scripts\activate

Linux/Mac:   
source .venv/bin/activate

3. Instalar dependencias (para este caso no se necesitan dependencias)  
pip install -r requirements.txt

4. Ejecutar el perfilador  
python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv

## Características técnicas
- Sin dependencias externas: solo biblioteca estándar de Python.
- Manejo de errores: archivo no encontrado, archivo vacío.
- Detección de tipos: 80% de umbral.
- Soporte para booleanos: múltiples formatos.
- Porcentajes con 2 decimales.
- Case-sensitive para valores únicos.
- Crea automáticamente el directorio de salida.

Autor: Lara Herrera Barbara Fatima  
Programación para Ciencia de Datos - IPN  
Semestre Febrero-Julio 2026  