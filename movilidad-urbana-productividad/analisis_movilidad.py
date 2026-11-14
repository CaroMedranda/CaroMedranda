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
