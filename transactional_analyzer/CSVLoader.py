import csv
from transactional_analyzer.database.MySQLConnector import MySQLConnector

file_path = "transactional_analyzer/database/transactional-sample.csv"
mysql = MySQLConnector()


class CSVLoader:
    def __init__(self):
        self.file_path = file_path
        self.mysql = mysql
        self.conn = None
        self.db_cursor = None

    def load_data(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

        with open(self.file_path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csv_reader:
                query = (
                    "INSERT INTO transactionals_data "
                    "(transaction_id, merchant_id, user_id, "
                    "card_number, transaction_date, transaction_amount, "
                    "device_id, has_cbk) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                )
                self.db_cursor.execute(
                    query,
                    (
                      row[0],
                      row[1],
                      row[2],
                      row[3],
                      row[4],
                      row[5],
                      row[6],
                      row[7]
                    )
                )

        self.conn.commit()
        self.cursor.close()


CSVLoader().load_data()
