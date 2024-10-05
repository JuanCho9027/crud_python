import mysql.connector

# Configuración de la conexión a la base de datos MySQL
def obtener_conexion():
    conn = mysql.connector.connect(
        host="localhost", 
        user="root",
        password="",  
        database="crud"
    )
    return conn