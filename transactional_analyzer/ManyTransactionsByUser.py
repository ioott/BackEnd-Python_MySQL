from transactional_analyzer.database.MySQLConnector import MySQLConnector


class ManyTransactionsByUser:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def report(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

        query = (
            "SELECT user_id, COUNT(*) AS total_transactions, "
            "SUM(transaction_amount) AS total_amount "
            "FROM transactionals_data "
            "WHERE has_cbk = 'TRUE' "
            "GROUP BY user_id "
            "HAVING total_transactions > 10 "
            "ORDER BY total_amount DESC"
        )

        self.db_cursor.execute(query)
        results = self.db_cursor.fetchall()
        # retorna uma lista de tuplas

        self.db_cursor.close()
        return results
