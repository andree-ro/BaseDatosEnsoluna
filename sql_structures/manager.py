import mysql.connector
import numbers


class Manager:
    def __init__(self):
        # self.database_dir = "user='root', password='I.gt.MPW.2023.U', host='127.0.0.1', database='mydb'"
        self.database_dir = "user='root', password='andree2332', host='127.0.0.1', database='mydb'"

        # Connect to the database
        self.cnx = None

        # Create a cursor object
        self.cursor = None

    def connect(self):
        # Connect to the database
        self.cnx = mysql.connector.connect(user='root', password='andree2332',
                                           host='127.0.0.1', database='mydb')

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
        if not(self.is_empty(table_name)):
            self.connect()

            query = f"SELECT {table_data[0]} FROM {table_name} ORDER BY {table_data[0]} DESC;"
            self.cursor.execute(query)

            rows = self.cursor.fetchall()

            id = rows[0][0]

            self.close()

            return id+1

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

            if not(isinstance(value, numbers.Number)):
                query += f"{data} = '{value}' AND " if i != (len(data_list)-1) else f"{data} = '{value}';"

            else:
                query += f"{data} = {value} AND " if i != (len(data_list)-1) else f"{data} = {value};"

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        self.close()

        return rows[0][0]

    def insert_into_table(self, table_name, table_data, data_list):
        id = self.auto_id(table_name, table_data)

        self.connect()

        input_data = f"{id}, "

        for i, value in enumerate(data_list):
            if not(isinstance(value, numbers.Number)):
                input_data += f"'{value}', " if i != (len(data_list)-1) else f"'{value}'"

            else:
                input_data += f"{value}, " if i != (len(data_list)-1) else f"{value}"

        print(input_data)

        # Execute a INSERT query
        query = f"INSERT INTO {table_name} VALUES ({input_data})"

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
