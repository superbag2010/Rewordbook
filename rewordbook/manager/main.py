import fetch
import constants
import csv
import re
import datetime
import os

# featured history data
history=[]

# get history data
fetcher = fetch.Fetcher()
historyOrigin = fetcher.getSearchHitory(constants.CHROME)

# if already output file exist
if os.path.isfile(constants.OUTPUT_URL):
    # add to output file
    with open(constants.OUTPUT_URL, 'a+', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        reader = csv.reader(f)
        
        for recToCheck in historyOrigin:

            # create searched word field
            searchedWord = recToCheck[0].split("'")
            if len(searchedWord) > 1:
                isNewWord = True
                for recExist in reader:
                    # if word is new and not memorized, need to add
                    if searchedWord[1] is recExist[2]:
                        isNewWord = False
                        break
                
                if isNewWord is True:
                    recToAdd = [None]*5
                    recToAdd[0] = searchedWord[1]      
                    recToAdd[1] = constants.NOT_MEMORIZED_SYMBOL

                    # url field
                    recToAdd[2] = recToCheck[1]

                    # date field : convert epoch timestamp to readable date
                    epoch_start = datetime.datetime(constants.EPOCH_START_HOUR_CHROME, constants.EPOCH_START_MINUTE_CHROME, constants.EPOCH_START_SECOND_CHROME)
                    delta = epoch_start + datetime.timedelta(microseconds=int(recToCheck[2]))
                    recToAdd[3] = delta

                    # searched count field
                    recToAdd[4] = recToCheck[3]
                    writer.writerow(recToAdd)
            # if searched word does't exist, skip
            else:
                continue

# if already output file doens't exist
else:
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

    # output
    with open(constants.OUTPUT_URL, 'w', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(constants.FIELDS)
        writer.writerows(history)