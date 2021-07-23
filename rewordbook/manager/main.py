import fetch
import constants
import csv
import re
import datetime

fetcher = fetch.Fetcher()
historyOrigin = fetcher.getSearchHitory(constants.CHROME)
history=[]
for rec in historyOrigin:
    recTmp = [None]*5

    # create searched word field
    searchedWord = rec[0].split("'")
    if len(searchedWord) > 1:
        recTmp[0] = searchedWord[1]
    else:
        continue
    
    recTmp[1] = 'X'

    # url field
    recTmp[2] = rec[1]

    # date field : convert epoch timestamp to readable date
    epoch_start = datetime.datetime(constants.EPOCH_START_HOUR_CHROME, constants.EPOCH_START_MINUTE_CHROME, constants.EPOCH_START_SECOND_CHROME)
    delta = epoch_start + datetime.timedelta(microseconds=int(rec[2]))
    recTmp[3] = delta

    # searched count field
    recTmp[4] = rec[3]
    history.append(recTmp)

## output
with open(constants.OUTPUT_URL, 'w', newline='', encoding='UTF-8') as f:
    write = csv.writer(f)
    write.writerow(constants.FIELDS)
    write.writerows(history)