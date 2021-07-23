import os
import sqlite3
import constants

class Fetcher:
    """
    """

    def __init__(self) -> None:
        pass

    def getSearchHitory(self, browser):
        if browser == constants.CHROME:
            # set history file path
            data_path = constants.HISTORY_PATH_CHROME
            files = os.listdir(data_path)
            history_db = os.path.join(data_path, constants.HISTORY_FILE_CHROME)

            c = sqlite3.connect(history_db)
            cursor = c.cursor()
            select_statement = constants.GET_HISTORY_SQL_CHROME
            cursor.execute(select_statement)
            results = cursor.fetchall()
            return results