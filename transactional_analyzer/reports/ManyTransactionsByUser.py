from database.MySQLConnector import MySQLConnector
from utils.export_csv import export_csv


class ManyTransactionsByUser:
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
            "SELECT user_id, COUNT(*) AS total_transactions, "
            "SUM(transaction_amount) AS total_amount "
            "FROM transactionals_data "
            "WHERE has_cbk = 'TRUE' "
            "GROUP BY user_id "
            "HAVING total_transactions > 10 "
            "ORDER BY total_amount DESC"
        )

    db_cursor.execute(query)
    return db_cursor.fetchall()


def print_report(report):
    print('\n >>> O relatório foi salvo na pasta "exported_reports" <<<\n')

    for user_id, total_transactions, total_amount in report:
        print(
            f'Id da transação: {user_id}, '
            f'Total de Transações: {total_transactions}, '
            f'Valor Total: R$ {total_amount}'
        )

    print('\n >>> O relatório foi salvo na pasta "exported_reports" <<<\n')


def save_report(report):
    filepath = 'exported_reports/ManyTransactionsByUser.csv'
    export_csv(filepath, report)


if __name__ == '__main__':
    ManyTransactionsByUser().report()
