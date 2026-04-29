from app.backend.db import DB

class DBPrinterFunctions:
    def __init__(self, db_:DB):
        self.db = db_

    def get_printers(self):
        query = """
        SELECT
            printer_id,
            printer_name,
            printer_location,
            printer_model,
            curr_status,
            toner_level,
            paper_level,
            last_maintenance
        FROM Printer
        ORDER BY printer_name ASC
        """
        params = ()
        return self.db.execute_command(query, params)

    def get_printers_needing_attention_count(self):
        query = """
        SELECT COUNT(*)
        FROM Printer
        WHERE toner_level <= 20
        OR paper_level <= 20
        OR curr_status IN ('Offline', 'Maintenance')
        """
        params = ()
        result = self.db.execute_command(query, params)
        return result[0][0] if result else 0