"""
Reto Semana 1: Calculadora de Sumas
Programacion para Ciencia de Datos - IPN
Lara Herrera Barbara Fatima. 3AM1 
"""
import sys

def limpiar_valor(valor):
    #Quita espacios, elimina caracteres
    #quitar espacios
    valor = valor.strip()
    
    #Si esta vacio despues de limpiar espacios
    if not valor:
        return ""
    
    caracteres_validos = '0123456789.-'
    resultado = ''
    
    for char in valor:
        if char in caracteres_validos:
            resultado += char
    
    return resultado

def convertir_a_entero(texto):
    """
    Convierte un string a entero, truncando decimales.
    Si el string esta vacio o no es un numero valido, retorna 0.
    """
    if not texto:  #vacio
        return 0
    
    #signo negativo o punto
    if texto == '-' or texto == '.' or texto == '-.':
        return 0
    
    try:
        numero = float(texto)  #convertir a float
        return int(numero)     #Truncar a entero (hacia cero)
    except ValueError:
        # Si no se puede convertir
        return 0

def procesar_linea(linea):
    """
    1. Separa por comas
    2. Limpia cada valor
    3. Trunca a entero
    4. Sumar
    """
    #Quitar espacios y saltos de linea
    linea = linea.strip()
    
    #linea vacia o solo espacios = 0
    if not linea:
        return 0
    
    #Separar por comas
    elementos = linea.split(',')
    
    suma = 0
    for elem in elementos:
        valor_limpio = limpiar_valor(elem)
        
        numero = convertir_a_entero(valor_limpio)
        suma += numero
    
    return suma

def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()
    