# ========== main.py ==========
main_content = '''
#!/usr/bin/env python3
"""
Mi primer script en un repositorio Git.
"""

def saludar(nombre):
    """Retorna un saludo personalizado."""
    return f"Hola, {nombre}! Bienvenido al mundo de Git."


if __name__ == "__main__":
    nombre = input("Como te llamas? ")
    print(saludar(nombre))
'''

def despedida(nombre):
    return f"Adios, {nombre}!"
