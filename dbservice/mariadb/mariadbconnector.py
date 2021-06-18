# Module Imports
import mariadb
from os import getenv
import sys


# Connect to MariaDB Platform

class MariadbConnector:
    def __init__(self):
        self.hostname = getenv('HOSTNAME')
        self.user = getenv('MARIADB_USER')
        self.pwd = getenv('MARIADB_PWD')
        self.db = getenv('MARIADB_DB')


        self.connection = mariadb.connect(
            user=self.user,
            password=self.pwd,
            host=self.hostname,
            port=3303,  # your port number
            database=self.db,  # your database name
            autocommit=True

        )

    def execute(self, statement):
        cursor = self.connection.cursor()
        cursor.execute(statement)
        return cursor


    def commit(self):
        self.connection.commit()
        return
    def close(self):
        self.connection.close()
        return





