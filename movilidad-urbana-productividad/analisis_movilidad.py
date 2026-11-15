# ==========================================
# PROYECTO: MOVILIDAD URBANA Y PRODUCTIVIDAD
# ==========================================

# PASO 1. CARGAR Y EXPLORAR LOS DATOS

# Importar librerías

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# PASO 2. CARGAR LOS ARCHIVOS
# ==========================================

# Cargar archivo de movilidad
traffic = pd.read_csv('data/tomtom_traffic.csv')

# Cargar archivo de economía
eco = pd.read_csv('data/oecd_city_economy.csv')

# Mostrar las primeras 5 filas de movilidad
print(traffic.head(5))

# Mostrar las primeras 5 filas de economía
print(eco.head(5))

# ==========================================
# PASO 3. EXAMINAR LA ESTRUCTURA DE LOS DATOS
# ==========================================

# Examinar la estructura de traffic

print(traffic.info())
print(traffic.head(3))


# Examinar la estructura de eco

print(eco.info())
print(eco.head(3))

# ==========================================
# PASO 4. RENOMBRAR LAS COLUMNAS
# ==========================================

# Estandarizar los nombres de las columnas de traffic

traffic = traffic.rename(columns={
    'Country': 'country',
    'City': 'city',
    'UpdateTimeUTC': 'update_time_utc',
    'JamsDelay': 'jams_delay',
    'TrafficIndexLive': 'traffic_index_live',
    'JamsLengthInKms': 'jams_length_in_kms',
    'JamsCount': 'jams_count',
    'TrafficIndexWeekAgo': 'traffic_index_week_ago',
    'UpdateTimeUTCWeekAgo': 'update_time_utc_week_ago',
    'TravelTimeLivePer10KmsMins': 'travel_time_live_per_10_kms_mins',
    'TravelTimeHistoricPer10KmsMins': 'travel_time_historic_per_10_kms_mins',
    'MinsDelay': 'mins_delay'
})

# Verificar cambios en traffic

print(traffic.columns)


# Estandarizar los nombres de las columnas de eco

eco = eco.rename(columns={
    'Country': 'country',
    'City GDP/capita': 'city_gdp_capita',
    'Unemployment %': 'unemployment_percent',
    'Year': 'year',
    'City': 'city',
    'PM2.5 (μg/m³)': 'pm25_level',
    'Population (M)': 'population_million'
})

# Verificar cambios en eco

print(eco.columns)

# ==========================================
# PASO 5. CORREGIR FORMATOS NUMÉRICOS Y DE FECHA
# ==========================================

# Convertir las columnas de traffic a formato datetime
traffic['update_time_utc'] = pd.to_datetime(
    traffic['update_time_utc'], errors='coerce', utc=True
)

traffic['update_time_utc_week_ago'] = pd.to_datetime(
    traffic['update_time_utc_week_ago'], errors='coerce', utc=True
)

# Verificar los cambios en traffic
print(traffic.info())


# Limpiar y convertir valores numéricos de eco

# Convertir city_gdp_capita a float
eco['city_gdp_capita'] = (
    eco['city_gdp_capita'].astype(str)
    .str.replace('.', '')
    .str.replace(',', '.')
    .astype(float)
)

# Convertir unemployment_percent a float
eco['unemployment_percent'] = (
    eco['unemployment_percent'].astype(str)
    .str.replace('%', '')
    .str.replace(',', '.')
    .astype(float)
)

# Convertir pm25_level a float
eco['pm25_level'] = (
    eco['pm25_level'].astype(str)
    .str.replace(',', '.')
    .astype(float)
)

# Convertir population_million a float
eco['population_million'] = (
    eco['population_million'].astype(str)
    .str.replace(',', '.')
    .astype(float)
)

# Calcular la población total en unidades absolutas
eco['population'] = eco['population_million'] * 1000000

# Verificar los cambios en eco
print(eco.info())
print(eco.head(3))
