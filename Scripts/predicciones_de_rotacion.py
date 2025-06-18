#Predecir cada cuanto tiempo se renueva el personal (rotacion)

#Librerias
import pyodbc
import os
import pandas as pd ##Prediccion: Importancia de variables
import numpy as np
from sklearn.model_selection import train_test_split ##Dividir datos de entrenamiento y prueba
from sklearn.linear_model import LinearRegression ##Elegir un modelo
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report ##Predicción y evaluación
from sklearn.metrics import mean_absolute_error, r2_score ##Prediccion
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

#Seleccionar y usar columnas de la tabla Rotacion
query = '''
SELECT id_empleado, tipo_rotacion, fecha_de_rotacion, motivo
FROM dbo.Rotacion
ORDER BY id_empleado, fecha_de_rotacion
'''
df = pd.read_sql(query, conn)

#Verificar si el tipo de dato es correcto
df['fecha_de_rotacion'] = pd.to_datetime(df['fecha_de_rotacion'])

#Calcular días hasta la próxima rotación (por empleado)
df['dias_hasta_proxima_rotacion'] = df.groupby('id_empleado')['fecha_de_rotacion'].shift(-1) - df['fecha_de_rotacion']
df['dias_hasta_proxima_rotacion'] = df['dias_hasta_proxima_rotacion'].dt.days

#Eliminar filas donde no se puede saber la próxima rotación
df = df.dropna(subset=['dias_hasta_proxima_rotacion'])

#Verificacion
print(df.head())

# Codificamos variables
df = pd.get_dummies(df, columns=['tipo_rotacion', 'motivo'], drop_first=True)

#Convertir la columna fecha_de_rotacion por una variable numérica
df['año'] = df['fecha_de_rotacion'].dt.year
df['mes'] = df['fecha_de_rotacion'].dt.month
df['dia'] = df['fecha_de_rotacion'].dt.day

#Detalle de variables
X = df.drop(columns=['id_empleado', 'fecha_de_rotacion', 'dias_hasta_proxima_rotacion'])
y = df['dias_hasta_proxima_rotacion']

#Dividir datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Elegir un modelo
model = LinearRegression()
model.fit(X_train, y_train)

#Predicción y evaluación
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# Cierro la conexión
conn.close()