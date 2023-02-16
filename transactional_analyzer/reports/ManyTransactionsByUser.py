from database.MySQLConnector import MySQLConnector


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

        for user_id, total_transactions, total_amount in results:
            print(
                f'Id da transação: {user_id}, '
                f'Total de Transações: {total_transactions}, '
                f'Valor Total: R$ {total_amount}'
            )

        self.db_cursor.close()


if __name__ == '__main__':
    ManyTransactionsByUser().report()
