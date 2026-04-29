from app.backend.db import DB

class DBPUFunctions:
    def __init__(self, db_:DB):
        self.db = db_

    def get_printer_usage(self):
        query = """
                SELECT pu.usage_id, \
                       p.printer_name, \
                       p.printer_location, \
                       pu.pages_printed, \
                       pu.job_status, \
                       pu.print_time
                FROM PrinterUsage pu
                         JOIN Printer p ON pu.printer_id = p.printer_id
                ORDER BY pu.print_time DESC \
                """
        params = ()
        return self.db.execute_command(query, params)

    def get_printer_usage_summary(self):
        query = """
                SELECT p.printer_name, \
                       COUNT(pu.usage_id)                 AS total_jobs, \
                       COALESCE(SUM(pu.pages_printed), 0) AS total_pages
                FROM Printer p
                         LEFT JOIN PrinterUsage pu ON p.printer_id = pu.printer_id
                GROUP BY p.printer_id, p.printer_name
                ORDER BY total_pages DESC \
                """
        params = ()
        return self.db.execute_command(query, params)