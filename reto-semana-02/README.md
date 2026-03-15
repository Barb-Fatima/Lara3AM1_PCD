# Clasificador de Temperaturas - Reto Semana 2
# Lara Herrera Barbara Fatima. 3AM1

Programa que procesa temperaturas de ciudades, convierte de Fahrenheit a Celsius cuando es necesario y clasifica según rangos predefinidos.

## Descripción

Este programa lee datos desde la entrada estándar (stdin) en formato CSV. Cada línea contiene:
- Nombre de la ciudad
- Temperatura (puede ser entero o decimal)
- Unidad (C para Celsius, F para Fahrenheit)

El programa procesa cada línea siguiendo estas reglas:
1. Ignora la primera línea (encabezados)
2. Convierte temperaturas en Fahrenheit a Celsius usando la fórmula: (F - 32) * 5 / 9
3. Clasifica la temperatura según los siguientes rangos:
   - < 0°C → Congelante
   - 0°C a 15°C → Frio
   - 16°C a 25°C → Templado
   - 26°C a 35°C → Calido
   - > 35°C → Extremo
4. Ignora líneas con datos inválidos (unidad incorrecta, temperatura no numérica, formato incorrecto)
5. Muestra la temperatura en Celsius con 1 decimal

## Ejemplos

### Entrada:  
ciudad,temperatura,unidad  
CDMX,22,C  
Nueva York,50,F  
Moscu,-10,C  
Miami,95,F  
Cancun,30,C  
Chicago,14,F  
Phoenix,104,F  
Error,abc,C  
Lima,25,C  
Bangkok,36,C  

## Salida:  
ciudad,temperatura_celsius,clasificacion  
CDMX,22.0,Templado  
Nueva York,10.0,Frio  
Moscu,-10.0,Congelante  
Miami,35.0,Calido  
Cancun,30.0,Calido  
Chicago,-10.0,Congelante  
Phoenix,40.0,Extremo  
Lima,25.0,Templado  
Bangkok,36.0,Extremo  

## Clonar el repositorio:  
git clone https://github.com/Barb-Fatima/Lara3AM1_PCD.git