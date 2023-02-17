from database.MySQLConnector import MySQLConnector
from utils.export_csv import export_csv


class UnusualHours:
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
    query = (
            "SELECT * "
            "FROM transactionals_data "
            "WHERE has_cbk = 'TRUE' "
            "AND (HOUR(transaction_date) < 6) "
            "ORDER BY transaction_amount DESC "
        )

    db_cursor.execute(query)
    return db_cursor.fetchall()


def print_report(report):
    print('\n >>> O relatório foi salvo na pasta "exported_reports" <<<\n')

    for (transaction_id, merchant_id, user_id,
            card_number, transaction_date, transaction_amount,
            device_id, has_cbk) in report:
        print(
            f'Id da transação: {transaction_id}, '
            f'Id do Vendedor: {merchant_id}, Id do Usuário: {user_id}, '
            f'Cartão: {card_number}, Data: {transaction_date}, '
            f'Valor: R$ {transaction_amount}, '
            f'Id do Dispositivo: {device_id}, Houve Chargeback? {has_cbk}'
        )

    print('\n >>> O relatório foi salvo na pasta "exported_reports" <<<\n')


def save_report(report):
    filepath = 'exported_reports/UnusualHours.csv'
    export_csv(filepath, report)


if __name__ == '__main__':
    UnusualHours().report()
