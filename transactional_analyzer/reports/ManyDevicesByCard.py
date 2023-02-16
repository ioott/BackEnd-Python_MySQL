from database.MySQLConnector import MySQLConnector


class ManyDevicesByCard:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def report(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

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

        self.db_cursor.execute(query)
        results = self.db_cursor.fetchall()

        for (transaction_id, user_id, card_number,
                transaction_amount, device_id, has_cbk) in results:
            print(
                f'Id da transação: {transaction_id}, Id do Usuário: {user_id},'
                f' Cartão: {card_number}, Valor: R$ {transaction_amount}, '
                f'Id do Dispositivo: {device_id}, Houve Chargeback? {has_cbk}'
            )

        self.db_cursor.close()


if __name__ == '__main__':
    ManyDevicesByCard().report()
