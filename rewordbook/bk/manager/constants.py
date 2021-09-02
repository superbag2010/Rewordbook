import os
from datetime import date

### excuting in new window environment, need to set following constans
OUTPUT_URL="/Users/choeseungho/Desktop/google_drive/ja_dic/rewordbook"
OUTPUT_URL_FOR_WINODW=r"C:\Users\JEANSUBIANO\Desktop\WebCrawler\Result"

# browser
CHROME="chrome"

# url of browser history
HISTORY_PATH_CHROME=os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
HISTORY_FILE_CHROME='history'
GOOGLE_ACCOUNT_HISTORY_PATH="/Users/choeseungho/Desktop/google_drive/ja_dic/raw/BrowserHistory.json"

# url of output
#OUTPUT_URL=os.path.expanduser('~')+r"\Desktop\rewordbook.csv"
OUTPUT_BACKUP_URL=OUTPUT_URL + str(date.today())

# output format
FIELDS=['memorized', 'word', 'url','date', 'count']

# sql
GET_HISTORY_SQL_CHROME="SELECT DISTINCT urls.title, urls.url, urls.last_visit_time, urls.visit_count FROM urls, visits WHERE urls.id = visits.url and urls.url LIKE ('%ja.dict.naver.com%') ORDER BY urls.last_visit_time DESC;"

# output format
OUTPUT_FORMAT_CSV='csv'

# etc
EPOCH_START_HOUR_CHROME=1601
EPOCH_START_MINUTE_CHROME=1
EPOCH_START_SECOND_CHROME=1
NOT_MEMORIZED_SYMBOL='x'
DIC_HOME_URL_NAVER="https://ja.dict.naver.com"

# symbol
MEMORIZED_SYMBOL='o'
DELETED_SYMBOL='-'
ONCE_MEMORIZED_SYMBOL='1'