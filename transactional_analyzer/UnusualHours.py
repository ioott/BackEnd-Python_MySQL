from transactional_analyzer.database.MySQLConnector import MySQLConnector


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
        # retorna uma lista de tuplas

        self.db_cursor.close()

        return results
