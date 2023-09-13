import mysql.connector
import numbers
# import conexion


connection = None

# TODO
# - Hacer funcion para commit u rollback

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


class Manager:
    def __init__(self):
        #self.database_user = 'Javier'
        self.database_user = 'root'
        # self.database_password = 'I.gt.MPW.2023.U'
        self.database_password = 'andree2332'
        #self.database_password = 'Marco.andres23'
        # self.database_password = '1234'
        # self.database_password = '1234'
        #self.database_host = '192.168.1.150'
        self.database_database = 'mydb'
        self.conexion = get_db_connection(self.database_user, self.database_password, self.database_database)
        self.cursor = self.conexion.cursor()

        # # Connect to the database
        # self.cnx = None
        #
        # # Create a cursor object
        # self.cursor = None

    def close(self):
        # Close the cursor and the connection
        self.cursor.close()
        self.conexion.close()

    def is_empty(self, table_name):
        query = f"SELECT COUNT(*) FROM {table_name};"
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        # self.close()
        return True if row[0][0] == 0 else False

    def delete_id_row(self, table_name, table_data, id):
        query = f"DELETE FROM {table_name} WHERE ({table_data[0]} = {id});"
        self.cursor.execute(query)
        # self.close()
        return self.print_table(table_name)

    def delete_row(self, table_name, table_data, data_list):
        id = self.get_id(table_name, table_data, data_list)
        query = f"DELETE FROM {table_name} WHERE ({table_data[0]} = {id});"
        self.cursor.execute(query)
        # self.close()
        return self.print_table(table_name)

    def update_table_with_id(self, table_name, table_data, column, data, id):
        data = f"'{data}'" if not (isinstance(data, numbers.Number)) else f"{data}"
        query = f"UPDATE {table_name} SET {column} = {data} WHERE ({table_data[0]} = {id})"
        self.cursor.execute(query)
        # self.close()
        return self.print_table(table_name)

    def update_table(self, table_name, table_data, data_list, column, data):
        id = self.get_id(table_name, table_data, data_list)
        data = f"'{data}'" if not (isinstance(data, numbers.Number)) else f"{data}"
        # Execute a INSERT query
        query = f"UPDATE {table_name} SET {column} = {data} WHERE ({table_data[0]} = {id})"
        self.cursor.execute(query)
        # self.close()
        return self.print_table(table_name)

    def auto_id(self, table_name, table_data):
        if not (self.is_empty(table_name)):
            query = f"SELECT {table_data[0]} FROM {table_name} ORDER BY {table_data[0]} DESC;"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            id = rows[0][0]
            # self.close()
            return id + 1
        return 0

    def search_by_id(self, table_name, table_data, id_number):
        query = f"SELECT * FROM {table_name} WHERE {table_data[0]} = {id_number}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        # self.close()
        return rows[0]

    def get_id(self, table_name, table_data, data_list):
        query = f"SELECT {table_data[0]} FROM {table_name} WHERE "
        for i, data in enumerate(table_data[1:]):
            value = data_list[i]
            if not (isinstance(value, numbers.Number)):
                query += f"{data} = '{value}' AND " if i != (len(data_list) - 1) else f"{data} = '{value}';"
            else:
                query += f"{data} = {value} AND " if i != (len(data_list) - 1) else f"{data} = {value};"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        # self.close()
        return rows[0][0]

    def get(self, table_name, table_data, values, data):
        query = f"SELECT {table_data[0]} FROM {table_name} WHERE {data} = '{values}';"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        # self.close()
        return rows[0][0]

    def insert_into_table(self, table_name, table_data, data_list):
        try:
            self.get_id(table_name, table_data, data_list)
            raise Exception('Dato ya existente')
        except:
            id = self.auto_id(table_name, table_data)
            input_data = f"{id}, "
            for i, value in enumerate(data_list):
                if not (isinstance(value, numbers.Number)):
                    input_data += f"'{value}', " if i != (len(data_list) - 1) else f"'{value}'"
                else:
                    input_data += f"{value}, " if i != (len(data_list) - 1) else f"{value}"
            # Execute a INSERT query
            query = f"INSERT INTO {table_name} VALUES ({input_data})"
            self.cursor.execute(query)
            # self.close()
            return self.print_table(table_name)

    def insert_into_table_NID(self, table_name, table_data, data_list):
        try:
            self.get_id(table_name, table_data, data_list)
            raise Exception('Dato ya existente')
        except:
            input_data = f" "
            for i, value in enumerate(data_list):
                if not (isinstance(value, numbers.Number)):
                    input_data += f"'{value}', " if i != (len(data_list) - 1) else f"'{value}'"
                else:
                    input_data += f"{value}, " if i != (len(data_list) - 1) else f"{value}"
            # Execute a INSERT query
            query = f"INSERT INTO {table_name} VALUES ({input_data})"
            self.cursor.execute(query)
            self.close()
            return self.print_table(table_name)

    def print_table(self, table_name):
        # Execute a SELECT query
        query = f"SELECT * FROM {table_name};"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        # self.close()
        return rows

    def iniciar_ses(self, data):
        rol = 'rol'
        usuarios = 'usuarios'
        query = f"SELECT {rol} FROM {usuarios} WHERE nombre =  '{data}';"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        # self.close()
        # -> consulta que nos devuelve un usuario tambien hacer una consulta a la tabla rol
        if rows[0][0] == 'Administrador':
            return 1
        elif rows[0][0] == 'Vendedor':
            return 2
        elif rows[0][0] == 'Bodegero':
            return 3
        elif rows[0][0] == 'Catador':
            return 4

    def iniciar_contra(self, data):
        contrasena = 'contraseña'
        usuarios = 'usuarios'
        query = f"SELECT {contrasena} FROM {usuarios} WHERE nombre =  '{data}';"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        # self.close()
        return rows[0][0]

    def transaction(self, level):
        self.conexion.start_transaction("", level, "")
        self.conexion.autocommit = False

    def commi(self):
        self.conexion.commit()

    def rollB(self):
        self.conexion.rollback()

    def __str__(self):
        return f"Usuario: {self.database_user}\nContrasenia: {self.database_password}" \
               f"\nBase de datos: {self.database_database}"
