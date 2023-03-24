import mysql.connector
import numbers


class Manager:
    def __init__(self):
        self.database_user = 'root'
        # self.database_password = 'I.gt.MPW.2023.U'
        #self.database_password = 'andree2332'
        self.database_password = 'Marco.andres23'
        self.database_host = '127.0.0.1'
        self.database_database = 'mydb'

        # Connect to the database
        self.cnx = None

        # Create a cursor object
        self.cursor = None

    def set_database_user(self, value):
        self.database_user = value

    def set_database_password(self, value):
        self.database_password = value

    def set_database_host(self, value):
        self.database_host = value

    def set_database_database(self, value):
        self.database_database = value

    def connect(self):
        # Connect to the database
        self.cnx = mysql.connector.connect(user=self.database_user, password=self.database_password,
                                           host=self.database_host, database=self.database_database)

        # Create a cursor object
        self.cursor = self.cnx.cursor()

    def close(self):
        # Close the cursor and the connection
        self.cursor.close()
        self.cnx.close()

    def is_empty(self, table_name):
        self.connect()

        query = f"SELECT COUNT(*) FROM {table_name};"
        self.cursor.execute(query)

        row = self.cursor.fetchall()

        self.close()

        return True if row[0][0] == 0 else False

    def delete_id_row(self, table_name, table_data, id):
        self.connect()

        query = f"DELETE FROM {table_name} WHERE ({table_data[0]} = {id});"
        self.cursor.execute(query)

        self.cnx.commit()

        self.close()

        return self.print_table(table_name)

    def delete_row(self, table_name, table_data, data_list):
        id = self.get_id(table_name, table_data, data_list)

        self.connect()

        query = f"DELETE FROM {table_name} WHERE ({table_data[0]} = {id});"

        self.cursor.execute(query)

        self.cnx.commit()

        self.close()

        return self.print_table(table_name)

    def update_table(self, table_name, table_data, data_list, column, data):
        id = self.get_id(table_name, table_data, data_list)

        self.connect()

        data = f"'{data}'" if not (isinstance(data, numbers.Number)) else f"{data}"

        # Execute a INSERT query
        query = f"UPDATE {table_name} SET {column} = {data} WHERE ({table_data[0]} = {id})"

        self.cursor.execute(query)

        self.cnx.commit()

        self.close()
        return self.print_table(table_name)

    def auto_id(self, table_name, table_data):
        if not (self.is_empty(table_name)):
            self.connect()

            query = f"SELECT {table_data[0]} FROM {table_name} ORDER BY {table_data[0]} DESC;"
            self.cursor.execute(query)

            rows = self.cursor.fetchall()

            id = rows[0][0]

            self.close()

            return id + 1

        return 0

    def search_by_id(self, table_name, table_data, id_number):
        self.connect()

        query = f"SELECT * FROM {table_name} WHERE {table_data[0]} = {id_number}"

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        self.close()

        return rows[0]

    def get_id(self, table_name, table_data, data_list):
        self.connect()

        query = f"SELECT {table_data[0]} FROM {table_name} WHERE "

        for i, data in enumerate(table_data[1:]):
            value = data_list[i]

            if not (isinstance(value, numbers.Number)):
                query += f"{data} = '{value}' AND " if i != (len(data_list) - 1) else f"{data} = '{value}';"

            else:
                query += f"{data} = {value} AND " if i != (len(data_list) - 1) else f"{data} = {value};"

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        self.close()

        return rows[0][0]

    def insert_into_table(self, table_name, table_data, data_list):
        try:
            self.get_id(table_name, table_data, data_list)

            raise Exception('Dato ya existente')

        except:
            id = self.auto_id(table_name, table_data)

            self.connect()

            input_data = f"{id}, "

            for i, value in enumerate(data_list):
                if not (isinstance(value, numbers.Number)):
                    input_data += f"'{value}', " if i != (len(data_list) - 1) else f"'{value}'"

                else:
                    input_data += f"{value}, " if i != (len(data_list) - 1) else f"{value}"

            # Execute a INSERT query

            query = f"INSERT INTO {table_name} VALUES ({input_data})"
            print(query)
            self.cursor.execute(query)

            self.cnx.commit()

            self.close()
            return self.print_table(table_name)

    def print_table(self, table_name):
        self.connect()

        # Execute a SELECT query
        query = f"SELECT * FROM {table_name};"

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        self.close()

        return rows

    def iniciar_ses(self, data):
        self.connect()
        rol = 'rol'
        usuarios = 'usuarios'
        query = f"SELECT {rol} FROM {usuarios} WHERE nombre =  '{data}';"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.close()
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
        self.connect()
        contrasena = 'contraseña'
        usuarios = 'usuarios'
        query = f"SELECT {contrasena} FROM {usuarios} WHERE nombre =  '{data}';"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.close()
        return rows[0][0]



    def __str__(self):
        return f"Usuario: {self.database_user}\nContrasenia: {self.database_password}" \
               f"\nHost: {self.database_host}\nBase de datos: {self.database_database}"
