from database.MySQLConnector import MySQLConnector
from utils.export_csv import export_csv


class HigherAmount:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def report(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

        results = make_report(self.db_cursor)
        save_report(results)
        print_report(results)

        self.db_cursor.close()
        return results


def make_report(db_cursor):
    sub_query = (
            "SELECT transaction_amount FROM transactionals_data "
            "WHERE has_cbk = 'TRUE' AND transaction_amount > 1000"
        )

    query = (
        "SELECT transaction_id, user_id, transaction_amount, has_cbk "
        "FROM transactionals_data "
        f"WHERE transaction_amount IN ({sub_query}) "
        "ORDER BY transaction_amount DESC"
    )

    db_cursor.execute(query)
    return db_cursor.fetchall()


def print_report(report):
    print('\n >>> O relatório foi salvo na pasta "exported_reports" <<<\n')

    for transaction_id, user_id, transaction_amount, has_cbk in report:
        print(
            f'Id da transação: {transaction_id}, Id do Usuário: {user_id},'
            f' Valor: R$ {transaction_amount}, Houve Chargeback? {has_cbk}'
        )

    print('\n >>> O relatório foi salvo na pasta "exported_reports" <<<\n')


def save_report(report):
    filepath = 'exported_reports/HigherAmountReport.csv'
    export_csv(filepath, report)


if __name__ == '__main__':
    HigherAmount().report()
