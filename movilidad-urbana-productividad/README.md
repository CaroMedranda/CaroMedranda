# Movilidad urbana y productividad económica en ciudades de Latinoamérica

## Descripción del proyecto

Análisis exploratorio desarrollado con Python para explorar la relación entre la congestión vehicular y los indicadores de productividad económica en ciudades de Latinoamérica durante 2024.

El proyecto integra información de movilidad urbana y variables económicas, con el propósito de identificar patrones, comparar indicadores y explorar posibles asociaciones entre las condiciones de tráfico y el desempeño económico de las ciudades.

## Objetivos

- Explorar el comportamiento de la congestión vehicular en diferentes ciudades.
- Analizar indicadores económicos, especialmente el PIB per cápita.
- Integrar información de movilidad y economía mediante variables comunes.
- Identificar patrones, distribuciones y posibles relaciones entre los indicadores.

## Datos utilizados

Se trabajó con dos conjuntos de datos proporcionados en el proyecto de TripleTen:

- **TomTom Traffic:** información sobre congestión vehicular, tiempos de desplazamiento y retrasos.
- **OECD City Economy:** indicadores económicos y ambientales por ciudad, como PIB per cápita, desempleo, contaminación PM2.5 y población.

La muestra final comprende 15 ciudades de 7 países latinoamericanos durante 2024.

## Herramientas y tecnologías

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Metodología

1. **Exploración de datos:** revisión de la estructura, columnas, tipos de datos y registros.
2. **Limpieza y transformación:** estandarización de nombres de columnas, conversión de fechas y formatos numéricos.
3. **Filtrado temporal:** selección de los registros correspondientes a 2024.
4. **Agregación:** cálculo de promedios de las métricas de tráfico por ciudad y año.
5. **Integración:** combinación de los conjuntos de datos mediante una unión INNER, utilizando ciudad y año como claves.
6. **Análisis exploratorio:** elaboración de gráficos para estudiar distribuciones, valores atípicos y posibles relaciones entre las variables.

## Principales hallazgos

- La variable `jams_delay` presenta una distribución sesgada a la derecha, con algunas ciudades que registran retrasos considerablemente superiores al resto.
- Ciudad de México presenta el mayor valor de retraso total promedio agregado entre las ciudades analizadas.
- El PIB per cápita presenta una distribución con mayor concentración de ciudades en rangos intermedios y algunos valores elevados.
- La comparación visual de las variables mostró que sus escalas son muy diferentes, por lo que un gráfico de barras con un mismo eje puede dificultar la interpretación.
- El análisis exploratorio no evidencia una relación clara y directa entre el PIB per cápita y la congestión vehicular.

## Limitaciones del análisis

El estudio comprende una muestra de 15 ciudades durante 2024, por lo que sus resultados no representan necesariamente el comportamiento de todas las ciudades latinoamericanas.

Los resultados describen patrones y posibles asociaciones; no permiten establecer relaciones de causalidad.

## Conclusión

Este proyecto permitió aplicar herramientas de análisis de datos para integrar, limpiar, transformar y explorar información de diferentes fuentes. Los resultados muestran la importancia de considerar tanto el comportamiento de las variables como la calidad de los datos y sus limitaciones al momento de interpretar los hallazgos.

Además, permitió fortalecer habilidades en Python, análisis exploratorio de datos, visualización y comunicación de resultados.
