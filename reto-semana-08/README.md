# Sistema de Análisis Meteorológico Modular - Reto Semana 8
# Lara Herrera Bárbara Fátima. 3AM1

Sistema modular de análisis de datos meteorológicos que procesa mediciones de sensores, aplica operaciones vectorizadas con NumPy, detecta anomalías y genera reportes ejecutivos sobre las condiciones ambientales en la CDMX.  

## Descripción

El sistema implementa un **análisis completo de datos meteorológicos** para la startup **MeteoSense**, procesando información de 5 estaciones de monitoreo en la Ciudad de México durante 7 días, con mediciones cada hora (24 lecturas diarias).  

### Datos Generados

El programa genera datos simulados de sensores para:  

- **Temperatura (°C)**: Rango típico 10-35°C con variación día/noche
- **Humedad Relativa (%)**: Rango 20-90% con comportamiento inverso a la temperatura
- **CO2 (ppm)**: Rango 350-500 ppm con patrones de tráfico vehicular

### Estaciones de Monitoreo

| Índice | Estación | Zona |  
|--------|----------|------|  
| 0 | Coyoacán | Sur |   
| 1 | Azcapotzalco | Norte |  
| 2 | Xochimilco | Sur |  
| 3 | Tlalpan | Sur |  
| 4 | Miguel Hidalgo | Centro-Oeste |  

## Módulos y Funcionalidades
Para generar arrays 3D de NumPy (estaciones × días × horas)  
  - `generar_temperatura()`: Incluye variación día/noche y ruido aleatorio
  - `generar_humedad()`: Incluye variación inversa a temperatura
  - `generar_co2()`: Incluye patrones de tráfico y día de contingencia
  - `generar_datos_completos()`: Genera todas las variables y promedios diarios

Cálculo de métricas estadísticas.  
  - `estadisticas_globales()`: Media, máximo, mínimo, desviación, varianza, rango
  - `estadisticas_por_estacion()`: Promedio por cada estación
  - `estadisticas_por_dia()`: Promedio por cada día
  - `estadisticas_por_hora()`: Promedio por hora del día
  - `matriz_correlacion()`: Correlación entre variables

Identificación de valores atípicos.  
  - `detectar_anomalias()`: Método de desviación estándar (media ± 2σ)
  - `detectar_todas_anomalias()`: Analiza todas las variables
  - `analisis_contingencia()`: Impacto del día de contingencia (día 4)

Evaluación del confort térmico.  
  - `calcular_ict()`: ICT = T + 0.05 × H (T=temperatura, H=humedad)
  - `clasificar_confort()`: Categorías (Frío, Confortable, Cálido, Muy caluroso)
  - `estadisticas_ict()`: Estadísticas del índice

Conversiones de unidades.  
  - `celsius_a_fahrenheit()`: °C → °F
  - `celsius_a_kelvin()`: °C → K
  - `normalizar_min_max()`: Normalización [0,1]
  - `normalizar_z_score()`: Estandarización z-score

Validación de datos.  
  - `verificar_nan()`: Contar valores faltantes
  - `verificar_rango()`: Validar rangos permitidos
  - `verificar_consistencia()`: Detectar inconsistencias
  - `limpiar_datos()`: Reemplazar NaN con media/mediana/cero

Generación de reportes.  
  - `generar_reporte_ejecutivo()`: Reporte completo con todas las métricas
  - `generar_reporte_estacion()`: Reporte específico por estación

## Validaciones Implementadas

1. **Valores Faltantes (NaN)**
   - Detección y conteo de valores NaN por variable
   - Uso de funciones `nan*` de NumPy para cálculos
   - Opciones de limpieza (media, mediana, cero)

2. **Rangos Válidos**
   - Temperatura: 10-35°C
   - Humedad: 20-95%
   - CO2: 300-600 ppm

3. **Detección de Anomalías**
   - Método de desviación estándar (media ± 2σ)
   - Identificación de valores atípicos por variable

4. **Análisis de Contingencia**
   - Día 4 (índice 3) con incremento de CO2 del 15%
   - Identificación de estación más afectada

## Ejemplos de Ejecución

### Ejemplo 1: Ejecución Normal

python main.py  

**Salida en consola:**

METEOSENSE ANALYTICS - SISTEMA DE ANÁLISIS METEOROLÓGICO  

   Generando datos de sensores...  
   Datos generados correctamente  
   Temperatura: (5, 7, 24)  
   Humedad:     (5, 7, 24)  
   CO2:         (5, 7, 24)  

Realizando análisis estadístico...  
Estadísticas calculadas  

Detectando anomalías...  
   temperatura: 0 anomalías  
   humedad: 0 anomalías  
   co2: 0 anomalías  

Analizando contingencia ambiental...  
   Incremento de CO2: 15.0%  

Calculando índice de confort...  
   Distribución de confort:  
     frio: 0.0%  
     confortable: 45.2%  
     calido: 35.8%  
     muy_caluroso: 19.0%  

### Ejemplo 2: Reporte Ejecutivo

======================================================================  
               METEOSENSE - REPORTE EJECUTIVO SEMANAL   
                        CDMX - Semana de Análisis
======================================================================  

 RESUMEN DE CONDICIONES  
────────────────────────────────────────  
   Temperatura promedio:    22.5 °C  
   Humedad promedio:         54.3 %  
   CO2 promedio:            401.7 ppm  

 RANKINGS  
────────────────────────────────────────  
   Estación más calurosa:   Azcapotzalco  
   Estación más húmeda:     Xochimilco  
   Mejor calidad de aire:   Tlalpan  

 PATRONES TEMPORALES  
────────────────────────────────────────  
   Hora más calurosa:       14:00 hrs  
   Hora con más CO2:        18:00 hrs  

 CALIDAD DE DATOS  
────────────────────────────────────────  
   Temperatura:  7 NaN  
   Humedad:      3 NaN  
   CO2:          3 NaN  
  Total valores faltantes:  13  


### Ejemplo 3: Reporte por Estación

REPORTE DE ESTACIÓN: Coyoacán  

  Temperatura:  
  Promedio: 21.8 °C  
  Máximo:   28.5 °C  
  Mínimo:   15.2 °C  
  Desv.:    3.42 °C  

  Humedad:  
  Promedio: 58.4 %  
  Máximo:   85.0 %  
  Mínimo:   32.0 %  
  Desv.:    12.15 %  

  CO2:  
  Promedio: 395.2 ppm  
  Máximo:   520.0 ppm  
  Mínimo:   350.0 ppm  
  Desv.:    25.30 ppm  

## Métricas y Cálculos Realizados

| Métrica | Descripción | Función |  
|---------|-------------|---------|  
| **Estadísticas Globales** | Media, máximo, mínimo, desviación, varianza, rango | `nanmean`, `nanmax`, `nanmin`, `nanstd` |  
| **Análisis por Eje** | Promedios por estación, día y hora | `axis=(1,2)`, `axis=(0,2)`, `axis=(0,1)` |  
| **Conversiones** | °C → °F, °C → K | Operaciones vectorizadas |  
| **Normalización** | Min-Max [0,1], Z-score | `(x - min) / (max - min)` |  
| **Índice de Confort** | ICT = T + 0.05H | Operaciones vectorizadas |  
| **Detección de Anomalías** | Media ± 2σ | Filtrado booleano |  
| **Correlación** | Matriz de correlación | `np.corrcoef()` |  

## Requisitos e Instalación

### Dependencias

numpy>=1.24.0  

### Instalación

# Clonar el repositorio
git clone https://github.com/Barb-Fatima/Lara3AM1_PCD.git  

# Navegar al directorio del reto
cd Lara3AM1_PCD/reto-semana-08  

# Instalar dependencias
pip install numpy  

# Ejecutar el sistema
python main.py  

## Interpretación de Resultados

### Índice de Confort Térmico (ICT)

| Rango | Categoría | Interpretación |  
|-------|-----------|----------------|  
| ICT < 20 |  Frío | Sensación de frío, necesidad de abrigo |  
| 20 ≤ ICT < 25 |  Confortable | Condiciones ideales |  
| 25 ≤ ICT < 30 |  Cálido | Sensación de calor moderado |  
| ICT ≥ 30 |  Muy caluroso | Condiciones extremas, riesgo de golpe de calor |  

### Calidad del Aire (CO2)

| Nivel | Rango (ppm) | Interpretación |  
|-------|-------------|----------------|  
| Bueno | < 400 | Aire limpio, condiciones normales |  
| Moderado | 400 - 500 | Calidad aceptable |  
| Alto | 500 - 600 | Contaminación vehicular significativa |  
| Muy Alto | > 600 | Contingencia ambiental |  

---

## Principios de NumPy Aplicados

1. **Arrays Multidimensionales**: Datos organizados en arrays 3D (estaciones × días × horas)  
2. **Operaciones Vectorizadas**: Cálculos sin loops  
3. **Broadcasting**: Operaciones entre arrays de diferentes formas  
4. **Indexación Booleana**: Filtrado de datos  
5. **Funciones nan***: Manejo de valores faltantes  
6. **Reducción por Ejes**: Agregación en diferentes dimensiones  

## 🐛 Manejo de Errores
El sistema implementa validaciones para:  

1. **Datos fuera de rango**: Detecta y reporta valores inconsistentes
2. **Valores NaN**: Calcula estadísticas ignorando valores faltantes
3. **Inconsistencias**: Verifica relaciones entre variables

## 👨‍💻 Autor

**Lara Herrera Bárbara Fátima**  
3AM1 - Programación para Ciencia de Datos  
Instituto Politécnico Nacional - 2026  

## Repositorio

git clone https://github.com/Barb-Fatima/Lara3AM1_PCD.git  

*MeteoSense Analytics - Reto desarrollado para Programación para Ciencia de Datos, IPN 2026*