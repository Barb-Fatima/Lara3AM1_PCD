# Calculadora de Sumas - Reto Semana 1
# Lara Herrera Barbara Fatima. 3AM1
Programa que procesa líneas de texto con números separados por comas, limpia los datos y calcula la suma total por línea.

## Descripción

Este programa lee datos desde la entrada estándar (stdin) línea por línea. Cada línea contiene números separados por comas que pueden incluir:
- Decimales
- Caracteres basura
- Espacios extras
- Líneas vacías

El programa procesa cada línea siguiendo estas reglas:
1. Líneas vacías = 0
2. Elimina caracteres no válidos (solo dígitos, punto y signo negativo)
3. Trunca decimales a enteros (usando int())
4. Suma todos los valores
5. Imprime el resultado

## Ejemplos
Entrada: 
1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
  5 , 10 , 15  
0,0,0
-1,-2,-3
abc,def
3.99
-0.5,0.5
,1,2,
100

Salida:
6
10
6
8
30
0
-6
0
3
0
3
100

## Clona el repositorio:
git clone https://github.com/Barb-Fatima/reto-semana-01.git