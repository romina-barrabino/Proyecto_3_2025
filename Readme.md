# Aplicaciones a instalar: 
SQL Microsoft Server (creo en ella una base de datos que llamo "Empleados")
Visual Studio
Git (desde https://git-scm.com/downloads/win)

# Instalaciones requeridas:
pandas (pip install pandas)
seaborn (pip install seaborn)
pyodc (pip install pyodbc)
scikit-learn (pip install scikit-learn)

# Estructura creada en SQL:
Empleados
|_ tabla
    |_ informacion
    |_ encuesta
    |_ rotacion

# Detalle de la estructura en SQL:
.) Empleados= Base de datos.
.) Informacion= Tabla creada manualmente en SQL con los datos principales de los empleados.
.) Encuesta= Tabla creada manualmente en SQL con los resultados de las encuestas realizados por los empleados.
.) Rotacion= Tabla creada manualmente en SQL con los estados de rotacion de cada empleado.

# Estructura creada en Visual Studio:
Proyecto_3_2025
|_ Imagenes
|_ Scripts
    |_carga_datos_informacion
|   |_carga_datos_encuesta
|   |_carga_datos_rotacion
|   |_creacion_tabla_encuesta
|   |_creacion_tabla_informacion
|   |_creacion_tabla_rotacion
|   |_predicciones_de_rotacion
|   |_visualizacion_1
|   |_visualizacion_2
|_ encuesta_de_satisfacción
|_ Readme.md
|_ .env
|_ .gitignore

# Detalle de la estructura en Visual Studio:
.) Protecto_3_2025= Carpeta creada manualmente en la computadora.
.) Imagenes= Compuesta por diversas capturas de pantalla de los procesos realizados.
.) encuesta_de_satisfaccion= Encuesta realizada (sin resultados). 
.) .env= Posee los datos para la conexion con SQL y con la API.
.) .gitignore= Posee el nombre de los archivos que no deberan visualizarse en el Github.

# Instalaciones y/o scripts para la terminal de Visual Studio: 
a) Instalacion de dotenv: pip install python-dotenv
b) Evitar la visualizacion de la carpeta .env en GitHub: git rm --cached .env
c) Verificacion de la instalacion de git: git --version

# Conexion entre Visual Studio y un repositorio en GitHub que llamare "Proyecto_2_2025"
git init
git add .
git commit -m "Iniciando proyecto en GitHub"