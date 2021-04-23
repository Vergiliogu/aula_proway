import MySQLdb
from typing import List

DB = ""
HOST = "localhost"
USER = "root"
PASSWORD = ""
PORT = 3306


class DataBase:

    def create_connection_and_cursor(self, db_name: str = "") -> None:
        self.conn = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, db=db_name)
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

    def conn_and_cursor_exist(self):
        try:
            self.conn
            self.cursor
            return True
        except AttributeError:
            return False

    def is_database_selected(self):
        try:
            self.cursor.execute("insert into teste values ('teste')")
        except Exception:
            return False

    def change_current_database(self, new_database_name: str) -> None:
        self.conn.select_db(new_database_name)

    def insert_data(self, table_to_insert: str, data: List[str, float, int]) -> bool:
        if not self.conn_and_cursor_exist():
            raise Exception("Connetion or cursor is not defined!")
        if not self.is_database_selected():
            raise Exception("Database is not selected!")
        if not isinstance(data, list):
            raise TypeError("Data is not a list!")

        converted_to_sql_data = [f"'{value}'" if isinstance(value, str) and value.upper() not in "DEFAULT NULL"
                                 else str(value) for value in data]
        string_values = ",".join(converted_to_sql_data)
        sql = f"""INSERT INTO {table_to_insert} VALUES ({string_values})"""

        try:
            affected_rows = self.cursor.execute(sql)
            if affected_rows > 0:
                return True
        except:
            pass

        return False


tt = DataBase()
tt.create_connection_and_cursor()
# tt.change_current_database("teste123")
tt.insert_data("abc", [1, "Gustavo", "2021-10-12", "default"])
