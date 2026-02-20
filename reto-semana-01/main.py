"""
Reto Semana 1: Calculadora de Sumas
Programacion para Ciencia de Datos - IPN
Lara Herrera Barbara Fatima. 3AM1 
"""

import sys

def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos (solo mantiene digitos, punto y signo negativo)
    - Retorna el numero limpio como string
    """
    #Quitar espacios
    valor = valor.strip()
    
    #Si esta vacio despues de limpiar espacios
    if not valor:
        return ""
    
    #Caracteres permitidos
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
    

def procesar_linea(linea):
    """
    Procesa una linea completa:
    - Separa por comas
    - Limpia cada valor
    - Trunca a entero
    - Suma todos
    - Retorna el resultado
    """
    

def main():
    """
    Lee de stdin linea por linea
    Procesa cada linea
    Imprime el resultado
    """
    #probando la funcion de limpieza de valores
    valor = "1a2b, 3f5h"  #valor de ejemplo
    resultado = limpiar_valor(valor)
    print(resultado)

if __name__ == "__main__":
    main()