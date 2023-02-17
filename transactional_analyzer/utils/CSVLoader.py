import csv
from transactional_analyzer.database.MySQLConnector import MySQLConnector
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(
    current_dir, '..', 'database', 'transactional-sample.csv'
)

""" os.path.abspath(__file__) retorna o caminho absoluto para o arquivo em que
o código está sendo executado atualmente. Esse caminho é passado para
os.path.dirname(), que retorna o diretório correspondente a esse caminho
absoluto. Assim podemos garantir que o caminho do arquivo estará correto,
independente do diretório em que o script estiver sendo executado. """


class CSVLoader:
    def __init__(self):
        self.file_path = csv_file_path
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def load_data(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

        with open(self.file_path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(csv_reader)
            for row in csv_reader:
                query = (
                    "INSERT INTO transactionals_data "
                    "(transaction_id, merchant_id, user_id, "
                    "card_number, transaction_date, "
                    "transaction_amount, device_id, has_cbk) "
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
        self.db_cursor.close()


CSVLoader().load_data()
