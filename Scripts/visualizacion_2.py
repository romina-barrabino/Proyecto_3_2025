#Libreria
import pyodbc
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

#Cargo las variables desde el archivo .env
load_dotenv()

#Llamo a los parametros desde el archivo .env
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_UID")
password = os.getenv("SQL_PWD")
driver = os.getenv("SQL_DRIVER")

# Conexión a SQL Server
print(" Preparando cadena de conexión...")
conn_str = f'''
    DRIVER={{{driver}}};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    TrustServerCertificate=yes;
'''
conn = None
try:
    print("Intentando conectar a SQL Server...")
    conn = pyodbc.connect(conn_str, timeout=5)
    print("Conexión exitosa.")
    
except pyodbc.Error as e:
    print("Error de conexión:")
    print(e)

if not conn:
    print("El script se detiene porque no se pudo establecer conexión.")
    exit()

#Visualizacion 2 - Analisis de tabla Rotacion

# Leer datos de la tabla Rotacion
print("Leyendo datos de la tabla Rotacion...")
df_rotacion = pd.read_sql("SELECT * FROM Rotacion", conn)
print("Datos cargados:")

# Verificar que cargó bien
print(df_rotacion.head())

#Transformo los datos para la visualizacion (convierte fechas y prepara columnas)
print("Procesando datos de rotación...")
df_rotacion['fecha_de_rotacion'] = pd.to_datetime(df_rotacion['fecha_de_rotacion'])
df_rotacion['año'] = df_rotacion['fecha_de_rotacion'].dt.year
df_rotacion['mes'] = df_rotacion['fecha_de_rotacion'].dt.to_period('M')
print("Procesamiento completado.")

#Comparo por mes el tipo de rotacion de los empleado
print("Generando el grafico")
plt.figure(figsize=(12, 6))
sns.countplot(data=df_rotacion, x='mes', hue='tipo_rotacion')
plt.xticks(rotation=45)
plt.title("Rotaciones mensuales por tipo")
plt.tight_layout()
plt.show()
print("Gráfico mostrado correctamente")

# Cierro la conexión al final
conn.close()