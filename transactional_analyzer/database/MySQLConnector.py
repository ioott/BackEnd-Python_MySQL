from decouple import config
import mysql.connector


class MySQLConnector:
    def __init__(self):
        self.host = config('DB_HOST')
        self.user = config('DB_USER')
        self.password = config('DB_PASSWORD')
        self.database = config('DB_NAME')
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def connect(self):
        host = config("DB_HOST")
        user = config("DB_USER")
        password = config("DB_PASSWORD")
        database = config("DB_NAME")
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def close(self):
        self.connection.close()
