import json
import os
import datetime
import csv
from shutil import copyfile

import constants
import export

processedSearchHistory = []
fields = ['memorized', 'word', 'url','date']
outputUrl = constants.OUTPUT_URL + "." + constants.OUTPUT_FORMAT_CSV
outputBackbupUrl = constants.OUTPUT_BACKUP_URL + "." + constants.OUTPUT_FORMAT_CSV

json_open = open(constants.GOOGLE_ACCOUNT_HISTORY_PATH, 'r')
json_load = json.load(json_open)['Browser History']

# if already output file exist
if os.path.exists(outputUrl):
    # add only 'NOT_MEMORIZED_SYMBOL' and new search record
    # bakcup origin file
    copyfile(outputUrl, outputBackbupUrl)

    # make word to add to book
    with open(outputUrl, 'r', newline='', encoding='UTF-8') as f:
        newRecs = export.mkNewRecsFromDate(csv.reader(f), json_load)
    with open(outputUrl, 'r', newline='', encoding='UTF-8') as f:
        notMemorizedRecs, deletedRecs, memorizedRecs, onceMemorizedRecs = export.mkMemorizedRecsFromList(csv.reader(f))

    # add to output file
    with open(outputUrl, 'w', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        
        writer.writerows(newRecs)
        writer.writerows(notMemorizedRecs)
        writer.writerows(deletedRecs)
        writer.writerows(memorizedRecs)
        writer.writerows(onceMemorizedRecs)

else:
    for rec in json_load:
        if constants.DIC_HOME_URL_NAVER in rec['url']:
            recTmp = [None]*4
            recTmp[0] = constants.NOT_MEMORIZED_SYMBOL

            # create searched word field
            searchedWord = rec['title'].split("'")
            if len(searchedWord) > 1:
                recTmp[1] = searchedWord[1]
            else:
                continue

            # url field
            recTmp[2] = rec['url']

            # date field : convert epoch timestamp to readable date('%Y-%m-%dT%H:%M:%S.%f', '2013-02-07T17:30:03.083988')
            recTmp[3] = datetime.datetime.fromtimestamp(rec['time_usec'] / 1e6).strftime('%Y-%m-%d %H:%M')

            # duplication check
            isExist = False
            for rec in processedSearchHistory:
                if rec[1] == recTmp[1]:
                    isExist = True
                    break

            if isExist == False:
                processedSearchHistory.append(recTmp)

    # output
    with open(outputUrl, 'w', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(processedSearchHistory)