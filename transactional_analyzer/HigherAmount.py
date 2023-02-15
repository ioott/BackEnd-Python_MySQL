from transactional_analyzer.database.MySQLConnector import MySQLConnector


class HigherAmount:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = None
        self.db_cursor = None

    def execute_query(self):
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

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

        self.db_cursor.execute(query)
        results = self.db_cursor.fetchall()
        # retorna uma lista de tuplas

        self.db_cursor.close()
        return results
