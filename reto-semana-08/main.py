"""
Sistema de Inventario Modular - Reto Semana 4:
Implementar un sistema de inventario modular con una estructura de carpetas especifica, usando clases y validaciones.
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
print(f"║     temperatura     : shape {temperatura.shape}               ║")
print(f"║    humedad         : shape {humedad.shape}               ║")
print(f"║    co2             : shape {co2.shape}               ║")
print("╠══════════════════════════════════════════════════════════════╣")
print(f"║    temp_promedio_diario    : shape {temp_promedio_diario.shape}            ║")
print(f"║    humedad_promedio_diario : shape {humedad_promedio_diario.shape}            ║")
print(f"║    co2_promedio_diario     : shape {co2_promedio_diario.shape}            ║")
print("╚══════════════════════════════════════════════════════════════╝")
print("\n  Estaciones:", estaciones)


