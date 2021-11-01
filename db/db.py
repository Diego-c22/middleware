"""Manage Data base connection"""

import pymysql
from pymysql.err import OperationalError
from common.config import DATABASES


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
        )

    def select_detail(self, table, param, id):
        sql = f"SELECT * FROM {table} where {param}={id}"

        try:
            self.cursor.execute(sql)
            item = self.cursor.fetchone()
            print(item)
            return item
        except:
            print("error en ")

    def select_all(self, table):
        sql = f"SELECT * FROM {table}"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        print(items)
        return items


print(Attempt.attempt)
