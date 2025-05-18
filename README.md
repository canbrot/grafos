# Análisis de Redes de Cómics Marvel

Este proyecto contiene scripts de Python para analizar y visualizar redes de relaciones entre cómics de Marvel, utilizando la biblioteca `networkx` para la manipulación de grafos y otras bibliotecas para el análisis y visualización de datos. Los datos de los cómics se gestionan mediante una base de datos MySQL.

## Estructura del Proyecto

* **`data/`**:  Este directorio contiene la base de datos `marvel_comics` (MySQL) que almacena la información detallada sobre los cómics.
* **`scripts/`**:  Este directorio contiene los scripts de Python para el análisis y visualización de los datos.

## Descripción de los Scripts

1.  **`louvain.py`**:
    * Este script implementa el algoritmo de Louvain para la detección de comunidades en una red simplificada de cómics.
    * Crea un grafo no dirigido y visualiza las comunidades detectadas mediante colores.
    * Útil para identificar grupos de cómics estrechamente relacionados.

    ```python
    import networkx as nx
    import community.community_louvain as community_louvain
    import matplotlib.pyplot as plt
    import random

    # ... (código del script louvain.py)
    ```

2.  **`primer_grafo.py`**:
    * Crea un grafo dirigido que representa la secuencia narrativa de los cómics.
    * Asigna ratings a los nodos (cómics) y los utiliza para determinar el tamaño y color de los nodos en la visualización.
    * Permite visualizar la importancia y la conexión entre los cómics basada en sus ratings.

    ```python
    import networkx as nx
    import matplotlib.pyplot as plt

    # ... (código del script primer_grafo.py)
    ```

3.  **`segundo_grafo.py`**:
    * Genera un grafo no dirigido que muestra las relaciones entre cómics, escritores y dibujantes.
    * Utiliza colores para diferenciar entre tipos de nodos (cómics, escritores, dibujantes) y tamaños para reflejar los ratings de los cómics.
    * Proporciona una visión general de la colaboración en la creación de los cómics.

    ```python
    import networkx as nx
    import matplotlib.pyplot as plt

    # ... (código del script segundo_grafo.py)
    ```

4.  **`analisis.py`**:
    * Calcula varias métricas de centralidad en el grafo dirigido de cómics, incluyendo:
        * Centralidad de grado (in-degree y out-degree)
        * Centralidad de intermediación (betweenness)
        * Centralidad de cercanía (closeness)
        * Centralidad de eigenvector
        * PageRank
    * Analiza la relación entre los ratings de los cómics y su centralidad.

    ```python
    import networkx as nx

    # ... (código del script analisis.py)
    ```

5.  **`filtracion.py`**:
    * Este script se conecta a la base de datos MySQL `marvel_comics`.
    * Ejecuta una consulta SQL para filtrar cómics basados en criterios específicos (por ejemplo, aquellos que contienen "thanos" en el título y publicados entre 2000 y 2014).
    * Muestra los datos filtrados, lo que permite extraer información relevante de la base de datos.

    ```python
    import pandas as pd
    import mysql.connector

    # ... (código del script filtracion.py)
    ```

## Requisitos

* Python 3.x
* Bibliotecas de Python: `networkx`, `matplotlib`, `community` (para el algoritmo de Louvain), `pandas`, `mysql-connector-python`
* MySQL Server con la base de datos `marvel_comics`

## Uso

1.  Asegúrate de tener instalado Python y las bibliotecas necesarias.
2.  Configura la conexión a la base de datos MySQL en `filtracion.py` con tus credenciales.
3.  Ejecuta los scripts de Python para generar los grafos, realizar los análisis y filtrar los datos de los cómics.
