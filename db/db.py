"""Manage Data base connection"""
import pymysql
from pymysql.err import OperationalError
from common.config import DATABASES
from utilities.json_serializer import decimal_json_array


class Attempt:
    attempt = 0

    def increment(self):
        self.attempt += 1

    def reset(self):
        self.attempt = 0


class DataBase:
    """Create connection to db"""

    def __init__(self):
        print("i am in constructor")
        self.try_connection()

    def try_connection(self):
        print("i am in try connection")
        flag_conn = True
        while flag_conn:
            try:
                self.fill_connection()
                print("im in while try")
                self.cursor = self.connection.cursor()
                flag_conn = False
                print("Connected on attmpt: " + str(Attempt.attempt))

            except:
                print("Error on attmpt: " + str(Attempt.attempt))
                Attempt.attempt += 1
                print(Attempt.attempt)
                if Attempt.attempt > 3:
                    Attempt.attempt = 0
                    flag_conn = False
                    raise OperationalError

    def fill_connection(self):
        """Fill the database config"""
        print("im in fill conection")
        databases = ["default", "replica1", "replica2", "replica3"]
        self.connection = pymysql.connect(
            host=DATABASES[databases[Attempt.attempt]]["host"],
            db=DATABASES[databases[Attempt.attempt]]["db"],
            user=DATABASES[databases[Attempt.attempt]]["user"],
            password=DATABASES[databases[Attempt.attempt]]["password"],
            cursorclass=pymysql.cursors.DictCursor
        )

    def select_detail(self, table, param, id):
        sql = f'SELECT * FROM {table} where {param}="{id}"'
        print(sql)

        try:
            self.cursor.execute(sql)
            item = self.cursor.fetchone()
            print(item)
            return item
        except:
            print("error en ")

        self.connection.close()

    def select_all(self, table):
        sql = f"SELECT * FROM {table}"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        items = decimal_json_array(items)
        self.connection.close()
        return items

    def insert_element(self, table, **kwargs):
        print("im in create")
        keys = kwargs.keys()
        values = kwargs.values()
        fields = ""
        data = ""
        for key in keys:
            fields += f"{key},"

        for value in values:
            data += f'"{value}",'

        fields = fields[:-1]
        data = data[:-1]
        sql = f"INSERT INTO {table}({fields}) VALUES({data})"

        print(sql)
        try:
            self.cursor.execute(sql)

            id = self.cursor.lastrowid
            self.cursor.execute(
                f'SELECT * FROM {table} WHERE Id{table[:-1].title()}={id}')
            item = self.cursor.fetchone()
            self.connection.commit()

            print(item)
            return item
        except Exception as e:
            print(e)

        self.connection.close()

    def update_element(self, table, field, id, **kwargs):
        print("im in create")
        items = kwargs.items()
        fields = ""
        for key, value in items:
            if value:
                fields += f'{key}="{value}",'

        fields = fields[:-1]
        sql = f"UPDATE {table} SET {fields} WHERE {field}={id}"

        print(sql)
        try:
            self.cursor.execute(sql)
            self.cursor.execute(f'SELECT * FROM {table} WHERE {field}={id}')
            self.connection.commit()
            item = self.cursor.fetchone()
            print(item)
            return item
        except Exception as e:
            print(e)

        self.connection.close()

    def delete_element(self, table, param, id):
        sql = f'DELETE FROM {table} WHERE {param}="{id}"'
        print(sql)

        try:
            self.cursor.execute(sql)
            item = self.cursor.fetchone()
            print(item)
            self.connection.commit()
            return item
        except:
            print("error en ")

        self.connection.close()
