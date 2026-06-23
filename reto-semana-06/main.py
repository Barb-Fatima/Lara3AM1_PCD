"""
Validador de códigos - Reto Semana 6:
Sistema de validación automática de códigos de productos, envíos, empleados y facturas utilizando expresiones regulares.
Programacion para Ciencia de Datos - IPN
Lara Herrera Barbara Fatima. 3AM1
"""

import sys
import re

# Departamentos válidos para empleados
DEPARTAMENTOS_VALIDOS = {'VEN', 'ADM', 'TEC', 'LOG', 'RHH'}

# Series válidas para facturas
SERIES_VALIDAS = {'A', 'B', 'C', 'D', 'E'}


def detectar_tipo(codigo):
    # Retorna: 'producto', 'envio', 'empleado', 'factura' o 'desconocido'
    # Producto: 3 letras (may/min) - 4 digitos - 2 letras (may/min)
    if re.match(r'^[A-Za-z]{3}-\d{4}-[A-Za-z]{2}$', codigo):
        return 'producto'
    
    # Envío: ENV-AAAA-MM-DD-NNNNNN (formato estructural)
    if re.match(r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$', codigo):
        return 'envio'
    
    # Empleado: EMP-XXX-NNNN
    if re.match(r'^EMP-[A-Za-z]{3}-\d{4}$', codigo):
        return 'empleado'
    
    # Factura: FAC-X-NNNNNN
    if re.match(r'^FAC-[A-Za-z]-\d{6}$', codigo):
        return 'factura'
    
    return 'desconocido'


def validar_producto(codigo):
    # Categoría y país deben ser mayúsculas
    # Extraer partes
    match = re.match(r'^([A-Za-z]{3})-(\d{4})-([A-Za-z]{2})$', codigo)
    if not match:
        return False
    
    categoria, numero, pais = match.groups()
    
    # Validar mayúsculas
    return categoria.isupper() and pais.isupper()


def validar_envio(codigo):
    # año 2020-2030, mes 01-12, día 01-31
    match = re.match(r'^ENV-(\d{4})-(\d{2})-(\d{2})-(\d{6})$', codigo)
    if not match:
        return False
    
    anio = int(match.group(1))
    mes = int(match.group(2))
    dia = int(match.group(3))
    
    if not (2020 <= anio <= 2030):
        return False
    if not (1 <= mes <= 12):
        return False
    if not (1 <= dia <= 31):
        return False
    
    return True


def validar_empleado(codigo):
    # Departamento válido y que su numero no empiece en 0
    match = re.match(r'^EMP-([A-Za-z]{3})-(\d{4})$', codigo)
    if not match:
        return False
    
    depto = match.group(1).upper()
    numero = match.group(2)
    
    # Validar departamento
    if depto not in DEPARTAMENTOS_VALIDOS:
        return False
    
    # Validar que el número no empiece con 0
    if numero[0] == '0':
        return False
    
    return True


def validar_factura(codigo):
    # Serie A-E en mayúscula.
    match = re.match(r'^FAC-([A-Za-z])-(\d{6})$', codigo)
    if not match:
        return False
    
    serie = match.group(1).upper()
    
    # Validar serie
    return serie in SERIES_VALIDAS


def validar_codigo(codigo):
    tipo = detectar_tipo(codigo)
    
    if tipo == 'producto':
        return tipo, validar_producto(codigo)
    elif tipo == 'envio':
        return tipo, validar_envio(codigo)
    elif tipo == 'empleado':
        return tipo, validar_empleado(codigo)
    elif tipo == 'factura':
        return tipo, validar_factura(codigo)
    else:
        return 'desconocido', False


def main():
    # Imprimir encabezado CSV
    print("codigo,tipo,valido")
    
    # Leer línea por línea desde stdin
    for linea in sys.stdin:
        codigo = linea.strip()
        
        # Ignorar líneas vacías
        if not codigo:
            continue
        
        # Validar código
        tipo, es_valido = validar_codigo(codigo)
        
        # Imprimir resultado
        estado = "VALIDO" if es_valido else "INVALIDO"
        print(f"{codigo},{tipo},{estado}")


if __name__ == "__main__":
    main()