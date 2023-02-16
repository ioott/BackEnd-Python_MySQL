from database.MySQLConnector import MySQLConnector


class ShortTime:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def report(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

        query = (
            "SELECT t1.transaction_id, t1.merchant_id, t1.user_id, "
            "t1.card_number, t1.transaction_date, t1.transaction_amount, "
            "t1.device_id, t1.has_cbk "
            "FROM transactionals_data AS t1 "
            "JOIN transactionals_data AS t2 "
            "ON t1.user_id = t2.user_id "
            "WHERE t1.has_cbk = 'TRUE' "
            "AND t1.transaction_date <> t2.transaction_date "
            "AND TIMEDIFF(t1.transaction_date, "
            "t2.transaction_date) <= '00:05:00' "
            "ORDER BY t1.transaction_date "
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
