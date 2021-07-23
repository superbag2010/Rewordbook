import os
from datetime import date

# browser
CHROME="chrome"

# url of browser history
HISTORY_PATH_CHROME=os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
HISTORY_FILE_CHROME='history'

# url of output
#OUTPUT_URL=os.path.expanduser('~')+r"\Desktop\rewordbook.csv"
OUTPUT_URL=r"D:\Googleドライブ\日本語\rewordbook.csv"

# output format
FIELDS=['word', 'memorized', 'url', 'date', 'count']

# sql
GET_HISTORY_SQL_CHROME="SELECT DISTINCT urls.title, urls.url, urls.last_visit_time, urls.visit_count FROM urls, visits WHERE urls.id = visits.url and urls.url LIKE ('%ja.dict.naver.com%');"

# etc
EPOCH_START_HOUR_CHROME=1601
EPOCH_START_MINUTE_CHROME=1
EPOCH_START_SECOND_CHROME=1