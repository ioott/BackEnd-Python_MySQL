from transactional_analyzer.database.MySQLConnector import MySQLConnector


class ShortTime:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def report(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

        query = (
            "(SELECT t1.transaction_id, t1.merchant_id, t1.user_id, "
            "t1.card_number, t1.transaction_date, t1.transaction_amount, "
            "t1.device_id, t1.has_cbk) "
            "FROM transactionals_data AS t1 "
            "JOIN transactionals_data AS t2 "
            "WHERE has_cbk = 'TRUE' "
            "ON t1.user_id = t2.user_id "
            "AND t1.transaction_date != t2.transaction_date "
            "(AND TIMEDIFF(t1.transaction_date, "
            "t2.transaction_date) <= '00:05:00) "
            "ORDER BY t1.transaction_date "
        )

        self.db_cursor.execute(query)
        results = self.db_cursor.fetchall()
        # retorna uma lista de tuplas

        self.db_cursor.close()
        return results
