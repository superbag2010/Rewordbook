import os
from datetime import date

### excuting in new window environment, need to set following constans
OUTPUT_URL=r"D:\Googleドライブ\日本語\rewordbook"

# browser
CHROME="chrome"

# url of browser history
HISTORY_PATH_CHROME=os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
HISTORY_FILE_CHROME='history'

# url of output
#OUTPUT_URL=os.path.expanduser('~')+r"\Desktop\rewordbook.csv"
OUTPUT_BACKUP_URL=OUTPUT_URL + str(date.today())

# output format
FIELDS=['memorized', 'word', 'url', 'date', 'count']

# sql
GET_HISTORY_SQL_CHROME="SELECT DISTINCT urls.title, urls.url, urls.last_visit_time, urls.visit_count FROM urls, visits WHERE urls.id = visits.url and urls.url LIKE ('%ja.dict.naver.com%') ORDER BY urls.last_visit_time DESC;"

# output format
OUTPUT_FORMAT_CSV='csv'

# etc
EPOCH_START_HOUR_CHROME=1601
EPOCH_START_MINUTE_CHROME=1
EPOCH_START_SECOND_CHROME=1
NOT_MEMORIZED_SYMBOL='X'

# symbol
MEMORIZED_SYMBOL='O'
MEMORIZED_SYMBOL_TMP=''