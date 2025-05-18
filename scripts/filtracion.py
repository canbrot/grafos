import pandas as pd
import mysql.connector

# Conectar a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="marvel_comics"
)

# Consulta SQL para obtener solo los cómics en formato "Comic" entre 2000 y 2012
query = """
SELECT *
FROM comics
WHERE issue_title LIKE '%thanos%'
AND YEAR(publish_date) BETWEEN 2000 AND 2014

"""

# Leer los datos desde MySQL en un DataFrame
df = pd.read_sql(query, conn)

# Convertir la fecha a formato datetime
df["publish_date"] = pd.to_datetime(df["publish_date"], errors="coerce")

# Mostrar los datos filtrados
print(df[["comic_name", "writer", "cover_artist" ]])

# Cerrar conexión
conn.close()
