# Calculadora de Sumas - Reto Semana 1

Programa que procesa líneas de texto con números separados por comas, limpia los datos y calcula la suma total por línea.

## Descripción

Este programa lee datos desde la entrada estándar (stdin) línea por línea. Cada línea contiene números separados por comas que pueden incluir:
- Decimales
- Caracteres basura
- Espacios extras
- Líneas vacías

El programa procesa cada línea siguiendo estas reglas:
1. Líneas vacías → `0`
2. Elimina caracteres no válidos (solo dígitos, punto y signo negativo)
3. Trunca decimales a enteros (usando `int()`, no `round()`)
4. Suma todos los valores
5. Imprime el resultado

## Clona el repositorio:
git clone https://github.com/Barb-Fatima/reto-semana-01.git