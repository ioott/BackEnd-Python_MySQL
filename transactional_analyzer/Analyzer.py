from database.MySQLConnector import MySQLConnector
from reports import (
    HigherAmount,
    UnusualHours,
    ShortTime,
    ManyDevicesByCard,
    ManyTransactionsByUser
)


class Analyzer:
    def __init__(self):
        self.mysql = MySQLConnector()
        self.conn = self.mysql.connection
        self.db_cursor = self.conn.cursor()

    def make_all_reports(self) -> str:
        all_reports = []
        all_reports.extend(HigherAmount.make_report(self.db_cursor))
        all_reports.extend(UnusualHours.make_report(self.db_cursor))
        all_reports.extend(ShortTime.make_report(self.db_cursor))
        all_reports.extend(ManyDevicesByCard.make_report(self.db_cursor))
        all_reports.extend(ManyTransactionsByUser.make_report(self.db_cursor))
        return all_reports

    def user_analyzer(user_id):
        analyzer = Analyzer()
        all_reports = analyzer.make_all_reports()
        for transaction in all_reports:
            if user_id in transaction:
                is_suspect = True
                break
            else:
                is_suspect = False

        if is_suspect:
            print('\n Usuário suspeito \n')
        else:
            print('\n Nenhum registro encontrado \n')
