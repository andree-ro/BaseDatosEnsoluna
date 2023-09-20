import mysql.connector
# import threading

connection = None

# Función para obtener una conexión a la base de datos

def get_db_connection(user, password, database):
    try:
        global connection
        if connection is None:
            connection = mysql.connector.connect(
                host="127.0.0.1", user=user, password=password, database=database, port=3306
            )
            print("Conexion creada por primera vez:", database)
        else:
            print("Reutilizando conexion")
        return connection
    except mysql.connector.Error as e:
        print("Error de conexión:", e)
        return None
