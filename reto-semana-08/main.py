"""
Sistema de Análisis Meteorológico Modular - Reto Semana 8
Implementar un sistema de análisis de datos meteorológicos con una estructura
de carpetas específica, usando NumPy, operaciones vectorizadas y manejo de datos con valores faltantes.
Programacion para Ciencia de Datos - IPN
Lara Herrera Barbara Fatima. 3AM1
"""

import numpy as np

# Configuración para reproducibilidad
np.random.seed(42)

print("NumPy cargado correctamente")
print(f"Versión: {np.__version__}")

#  GENERACIÓN DE DATOS DE SENSORES
# Nombres de estaciones
estaciones = ['Coyoacán', 'Azcapotzalco', 'Xochimilco', 'Tlalpan', 'Miguel Hidalgo']
n_estaciones = len(estaciones)
n_dias = 7
n_horas = 24

# TEMPERATURA (°C)
temp_base = np.array([22, 24, 20, 19, 23])
hora_del_dia = np.arange(24)
variacion_diaria = 5 * np.sin((hora_del_dia - 6) * np.pi / 12)

temperatura = np.zeros((n_estaciones, n_dias, n_horas))
for i in range(n_estaciones):
    for d in range(n_dias):
        temperatura[i, d, :] = temp_base[i] + variacion_diaria + np.random.normal(0, 1.5, n_horas)

temperatura[1, 2, 10:14] = np.nan
temperatura[3, 5, 0:3] = np.nan

# HUMEDAD RELATIVA (%)
humedad_base = np.array([55, 45, 70, 65, 50])
variacion_humedad = -15 * np.sin((hora_del_dia - 6) * np.pi / 12)

humedad = np.zeros((n_estaciones, n_dias, n_horas))
for i in range(n_estaciones):
    for d in range(n_dias):
        humedad[i, d, :] = humedad_base[i] + variacion_humedad + np.random.normal(0, 5, n_horas)

humedad = np.clip(humedad, 20, 95)
humedad[0, 4, 15:18] = np.nan

# NIVELES DE CO2 (ppm)
co2_base = np.array([380, 420, 360, 350, 410])
patron_trafico = np.zeros(24)
patron_trafico[7:10] = 30
patron_trafico[17:20] = 40
patron_trafico[12:14] = 15

co2 = np.zeros((n_estaciones, n_dias, n_horas))
for i in range(n_estaciones):
    for d in range(n_dias):
        co2[i, d, :] = co2_base[i] + patron_trafico + np.random.normal(0, 10, n_horas)

co2[:, 3, :] *= 1.15
co2[2, 1, 5:8] = np.nan

# ARRAY 2D SIMPLIFICADO: Promedios diarios por estación
temp_promedio_diario = np.nanmean(temperatura, axis=2)
humedad_promedio_diario = np.nanmean(humedad, axis=2)
co2_promedio_diario = np.nanmean(co2, axis=2)

print("\n╔══════════════════════════════════════════════════════════════╗")
print("║              DATOS GENERADOS EXITOSAMENTE                    ║")
print("╠══════════════════════════════════════════════════════════════╣")
print(f"║    temperatura     : shape {temperatura.shape}                    ║")
print(f"║    humedad         : shape {humedad.shape}                    ║")
print(f"║    co2             : shape {co2.shape}                    ║")
print("╠══════════════════════════════════════════════════════════════╣")
print(f"║    temp_promedio_diario    : shape {temp_promedio_diario.shape}                 ║")
print(f"║    humedad_promedio_diario : shape {humedad_promedio_diario.shape}                 ║")
print(f"║    co2_promedio_diario     : shape {co2_promedio_diario.shape}                 ║")
print("╚══════════════════════════════════════════════════════════════╝")
print("\nEstaciones:", estaciones)

# PARTE 1: EXPLORACIÓN DE ARRAYS
print("\nPARTE 1: EXPLORACIÓN DE ARRAYS")

# EJERCICIO 1.1: Inspección de Datos
print("\nEJERCICIO 1.1: Inspección de Datos")

# 1. Número de dimensiones del array temperatura
n_dimensiones = temperatura.ndim

# 2. Forma (shape) del array
forma = temperatura.shape

# 3. Número total de elementos
total_elementos = temperatura.size

# 4. Tipo de datos
tipo_datos = temperatura.dtype

# 5. Tamaño en memoria (bytes)
memoria_bytes = temperatura.nbytes

print("\nPROPIEDADES DEL ARRAY TEMPERATURA")
print(f"\nDimensiones: {n_dimensiones}D")
print(f"Forma: {forma}")
print(f"{forma[0]} estaciones")
print(f"{forma[1]} días")
print(f"{forma[2]} horas por día")
print(f"Total de mediciones: {total_elementos:,}")
print(f"Tipo de datos: {tipo_datos}")
print(f"Memoria: {memoria_bytes:,} bytes ({memoria_bytes/1024:.2f} KB)")

# EJERCICIO 1.2: Indexación Básica
print("\nEJERCICIO 1.2: Indexación Básica")

# 1. Temperatura de Coyoacán (índice 0), día 1 (índice 0), a las 12:00 (índice 12)
temp_coyoacan_d1_12h = temperatura[0, 0, 12]
print(f"Coyoacán, Día 1, 12:00h: {temp_coyoacan_d1_12h:.1f}°C")

# 2. Todas las temperaturas de Xochimilco (índice 2) en el día 3 (índice 2)
temp_xochimilco_d3 = temperatura[2, 2, :]
print(f"\nXochimilco, Día 3 (24 horas):")
print(f"Primeras 6 horas: {temp_xochimilco_d3[:6].round(1)}")

# 3. Temperatura promedio diario de Miguel Hidalgo (índice 4) para los 7 días
temp_mh_7dias = temp_promedio_diario[4, :]
print(f"\nMiguel Hidalgo - Promedio por día:")
print(f"{temp_mh_7dias.round(1)}")

# 4. Último valor de CO2 registrado
ultimo_co2 = co2[-1, -1, -1]
print(f"\nÚltimo CO2 registrado: {ultimo_co2:.1f} ppm")

# EJERCICIO 1.3: Slicing Avanzado
print("\nEJERCICIO 1.3: Slicing Avanzado")

# 1. Temperaturas de TODAS las estaciones, TODOS los días, solo horas de la TARDE (12-18)
temp_tardes = temperatura[:, :, 12:18]
print(f"Temperaturas de tardes (12-17h)")
print(f"Shape: {temp_tardes.shape}")

# 2. Humedad de las primeras 3 estaciones, últimos 3 días, todas las horas
humedad_subset = humedad[:3, 4:, :]
print(f"\nSubset de humedad")
print(f"Shape: {humedad_subset.shape}")

# 3. CO2 de estaciones pares (0, 2, 4), todos los días, horas de mañana (6-12)
co2_mananas_pares = co2[::2, :, 6:12]
print(f"\nCO2 mañanas (estaciones pares)")
print(f"Shape: {co2_mananas_pares.shape}")

# 4. Temperaturas en orden inverso de días
temp_inverso = temperatura[:, ::-1, :]
print(f"\nTemperatura días invertidos")
print(f"Shape: {temp_inverso.shape}")


# PARTE 2: ESTADÍSTICAS BÁSICAS
print("\nPARTE 2: ESTADÍSTICAS BÁSICAS")

# EJERCICIO 2.1: Estadísticas Globales
print("\nEJERCICIO 2.1: Estadísticas Globales")

# 1. Temperatura promedio global
temp_promedio = np.nanmean(temperatura)

# 2. Temperatura máxima registrada
temp_maxima = np.nanmax(temperatura)

# 3. Temperatura mínima registrada
temp_minima = np.nanmin(temperatura)

# 4. Desviación estándar de temperatura
temp_std = np.nanstd(temperatura)

# 5. Rango de temperatura
temp_rango = temp_maxima - temp_minima

print("╔══════════════════════════════════════════════════════════════╗")
print("║           ESTADÍSTICAS GLOBALES DE TEMPERATURA               ║")
print("╠══════════════════════════════════════════════════════════════╣")
print(f"║  Promedio:     {temp_promedio:>6.2f} °C                                   ║")
print(f"║  Máxima:       {temp_maxima:>6.2f} °C                                   ║")
print(f"║  Mínima:       {temp_minima:>6.2f} °C                                   ║")
print(f"║  Desv. Est.:   {temp_std:>6.2f} °C                                   ║")
print(f"║  Rango:        {temp_rango:>6.2f} °C                                   ║")
print("╚══════════════════════════════════════════════════════════════╝")

# EJERCICIO 2.2: Estadísticas por Eje
print("\nEJERCICIO 2.2: Estadísticas por Eje")

# 1. Temperatura promedio POR ESTACIÓN
temp_por_estacion = np.nanmean(temperatura, axis=(1, 2))

print("TEMPERATURA PROMEDIO POR ESTACIÓN")
for i, est in enumerate(estaciones):
    print(f"   {est:15s}: {temp_por_estacion[i]:5.1f} °C")

# 2. Humedad promedio POR HORA DEL DÍA
humedad_por_hora = np.nanmean(humedad, axis=(0, 1))

print("\nHUMEDAD PROMEDIO POR HORA")
print("   Hora  │ Humedad")
for h in [0, 6, 12, 18]:
    print(f"   {h:02d}:00 │ {humedad_por_hora[h]:5.1f}%")

# 3. CO2 máximo POR DÍA
co2_max_por_dia = np.nanmax(co2, axis=(0, 2))

print("\nCO2 MÁXIMO POR DÍA")
for d in range(n_dias):
    print(f"Día {d+1}: {co2_max_por_dia[d]:6.1f} ppm")


# PARTE 3: OPERACIONES VECTORIZADAS
print("\nPARTE 3: OPERACIONES VECTORIZADAS")

# EJERCICIO 3.1: Conversiones de Unidades
print("\nEJERCICIO 3.1: Conversiones Vectorizadas")

# 1. Convertir temperatura de Celsius a Fahrenheit
temperatura_fahrenheit = temperatura * 9/5 + 32

print("TEMPERATURA EN FAHRENHEIT")
print(f"Promedio: {np.nanmean(temperatura_fahrenheit):.1f} °F")
print(f"Máxima: {np.nanmax(temperatura_fahrenheit):.1f} °F")
print(f"Mínima: {np.nanmin(temperatura_fahrenheit):.1f} °F")

# 2. Convertir temperatura de Celsius a Kelvin
temperatura_kelvin = temperatura + 273.15

print(f"\nTEMPERATURA EN KELVIN")
print(f"Promedio: {np.nanmean(temperatura_kelvin):.1f} K")

# 3. Normalizar humedad a rango [0, 1]
humedad_min = np.nanmin(humedad)
humedad_max = np.nanmax(humedad)
humedad_normalizada = (humedad - humedad_min) / (humedad_max - humedad_min)

print(f"\nHUMEDAD NORMALIZADA [0-1]")
print(f"Promedio: {np.nanmean(humedad_normalizada):.3f}")
print(f"Min: {np.nanmin(humedad_normalizada):.3f}")
print(f"Max: {np.nanmax(humedad_normalizada):.3f}")

# EJERCICIO 3.2: Índice de Confort Térmico
print("\nEJERCICIO 3.2: Índice de Confort Térmico")

# 1. Calcular el Índice de Confort Térmico
ict = temperatura + 0.05 * humedad

print("ÍNDICE DE CONFORT TÉRMICO (ICT)")
print(f"Shape del array ICT: {ict.shape}")
print(f"ICT promedio: {np.nanmean(ict):.2f}")
print(f"ICT máximo: {np.nanmax(ict):.2f}")
print(f"ICT mínimo: {np.nanmin(ict):.2f}")

# 2. Clasificar las condiciones usando indexación booleana
n_frio = np.sum((ict >= 0) & (ict < 20))
n_confortable = np.sum((ict >= 20) & (ict < 25))
n_calido = np.sum((ict >= 25) & (ict < 30))
n_muy_caluroso = np.sum(ict >= 30)
n_validas = np.sum(~np.isnan(ict))

print("\nDISTRIBUCIÓN DE CONDICIONES")
print(f"Frío (<20): {n_frio:5d} ({100*n_frio/n_validas:5.1f}%)")
print(f"Confortable (20-25): {n_confortable:5d} ({100*n_confortable/n_validas:5.1f}%)")
print(f"Cálido (25-30): {n_calido:5d} ({100*n_calido/n_validas:5.1f}%)")
print(f"Muy caluroso (≥30): {n_muy_caluroso:5d} ({100*n_muy_caluroso/n_validas:5.1f}%)")
print(f"Total válidas: {n_validas:5d}")