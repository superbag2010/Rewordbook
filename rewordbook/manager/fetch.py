import os
import sqlite3

class Fetcher:
    """
    """

    def __init__(self) -> None:
        pass

    def getSearchHitory(self, browser):
        if browser == "chrome":
            data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
            files = os.listdir(data_path)
            history_db = os.path.join(data_path, 'history')

            c = sqlite3.connect(history_db)
            cursor = c.cursor()
            select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
            cursor.execute(select_statement)
            results = cursor.fetchall()
