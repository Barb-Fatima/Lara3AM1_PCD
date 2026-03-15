"""
Clasificador de Temperaturas - Reto Semana 2
Programacion para Ciencia de Datos - IPN
Lara Herrera Barbara Fatima. 3AM1 
"""
import sys

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def clasificar_temperatura(celsius):
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"


def procesar_linea(linea):
    """
    Regresa una tupla (ciudad, celsius, clasificacion)
    o nada si la linea es invalida
    """
    # Eliminar espacios en blanco al inicio y final
    linea = linea.strip()
    
    if not linea:
        return None
    
    # Separar por comas
    partes = linea.split(',')
    if len(partes) != 3:
        return None
    
    # Extraer datos
    ciudad = partes[0].strip()
    temperatura_str = partes[1].strip()
    unidad = partes[2].strip().upper()
    
    # Validar unidad
    if unidad not in ['C', 'F']:
        return None
    
    # Convertir temperatura a número
    try:
        temperatura = float(temperatura_str)
    except ValueError:
        return None
    
    # Convertir a Celsius (si es necesario)
    if unidad == 'F':
        celsius = fahrenheit_a_celsius(temperatura)
    else:
        celsius = temperatura
    
    clasificacion = clasificar_temperatura(celsius)
    
    return (ciudad, celsius, clasificacion)


def main():
    """
    Lee desde stdin, procesa los datos y escribe el resultado en stdout.
    """
    # Variable para identificar encabezado
    primera_linea = True
    
    # Imprimir encabezado
    print("ciudad,temperatura_celsius,clasificacion")
    
    # Leer línea por línea desde stdin
    for linea in sys.stdin:
        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue
        
        resultado = procesar_linea(linea)
        
        if resultado:
            ciudad, celsius, clasificacion = resultado
            print(f"{ciudad},{celsius:.1f},{clasificacion}")


if __name__ == "__main__":
    main()