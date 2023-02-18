from database.MySQLConnector import MySQLConnector
from utils.export_csv import export_csv


class ManyDevicesByCard:
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
            "SELECT card_number "
            "FROM transactionals_data "
            "WHERE has_cbk = 'TRUE' "
            "GROUP BY card_number "
            "HAVING COUNT(DISTINCT device_id) > 1"
        )
    query = (
        "SELECT transaction_id, user_id, card_number, "
        "transaction_amount, device_id, has_cbk "
        "FROM transactionals_data "
        f"WHERE card_number IN ({sub_query}) "
        "ORDER BY card_number"
    )

    db_cursor.execute(query)
    return db_cursor.fetchall()


def print_report(report):
    print('\n >>> Este relatório mostra as transações que tiveram chargeback')
    print('e foram feitas usando um mesmo cartão em mais de um dispositivo \n')
    print('>>> Foi salvo na pasta "exported_reports"\n')

    for (transaction_id, user_id, card_number,
            transaction_amount, device_id, has_cbk) in report:
        print(
            f'Id da transação: {transaction_id}, Id do Usuário: {user_id},'
            f' Cartão: {card_number}, Valor: R$ {transaction_amount}, '
            f'Id do Dispositivo: {device_id}, Houve Chargeback? {has_cbk}'
        )

    print('\n >>> Este relatório mostra as transações que tiveram chargeback')
    print('e foram feitas usando um mesmo cartão em mais de um dispositivo \n')
    print('>>> Foi salvo na pasta "exported_reports"\n')


def save_report(report):
    filepath = 'exported_reports/ManyDevicesByCard.csv'
    export_csv(filepath, report)


if __name__ == '__main__':
    ManyDevicesByCard().report()
