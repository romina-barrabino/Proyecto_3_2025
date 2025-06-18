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

#Visualizacion 1 - Analisis de tabla Encuesta

# Leer datos de la tabla Encuesta
print("Leyendo datos de la tabla Encuesta...")
df = pd.read_sql("SELECT * FROM Encuesta", conn)
print("Datos cargados:")

# Verificar que cargó bien
print(df.head())

#Transformo los datos para la visualizacion (de ancho a largo)
df_long = df.melt(
    id_vars=['id_encuesta', 'id_empleado', 'fecha'],
    var_name='pregunta',
    value_name='puntuacion'
)

#Comparo los resultados de la encuesta por empleado
print("Generando el gráfico")
sns.set_theme(style="darkgrid")
plt.figure(figsize=(14, 6))
sns.lineplot(data=df_long, x='pregunta', y='puntuacion', hue='id_empleado', marker="o")
plt.title("Respuestas de empleados por pregunta")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Gráfico mostrado correctamente")

# Cierro la conexión al final
conn.close()