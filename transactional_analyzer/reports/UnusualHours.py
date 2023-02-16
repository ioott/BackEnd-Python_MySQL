from database.MySQLConnector import MySQLConnector


class UnusualHours:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def report(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

        query = (
            "SELECT * "
            "FROM transactionals_data "
            "WHERE has_cbk = 'TRUE' "
            "AND (HOUR(transaction_date) < 6) "
            "ORDER BY transaction_amount DESC "
        )

        self.db_cursor.execute(query)
        results = self.db_cursor.fetchall()

        for (transaction_id, merchant_id, user_id,
                card_number, transaction_date, transaction_amount,
                device_id, has_cbk) in results:
            print(
                f'Id da transação: {transaction_id}, '
                f'Id do Vendedor: {merchant_id}, Id do Usuário: {user_id}, '
                f'Cartão: {card_number}, Data: {transaction_date}, '
                f'Valor: R$ {transaction_amount}, '
                f'Id do Dispositivo: {device_id}, Houve Chargeback? {has_cbk}'
            )

        self.db_cursor.close()
