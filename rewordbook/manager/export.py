import os
import csv

import constants
import datetime
from shutil import copyfile

def toCSV(rawSearchHistory):

    processedSearchHistory = []
    outputUrl = constants.OUTPUT_URL + "." + constants.OUTPUT_FORMAT_CSV
    outputBackbupUrl = constants.OUTPUT_BACKUP_URL + "." + constants.OUTPUT_FORMAT_CSV

    # if already output file exist
    if os.path.isfile(outputUrl):

        # bakcup origin file
        copyfile(outputUrl, outputBackbupUrl)

        # not memorized word
        memorizedRecs = []
        notMemorizedRecs = []
        allWordInBook = []
        with open(outputUrl, 'r', newline='', encoding='UTF-8') as f:
            reader = csv.reader(f)
            for rec in reader:
                allWordInBook.append(rec[1])
                if rec[0] == constants.NOT_MEMORIZED_SYMBOL:
                    notMemorizedRecs.append(rec)
                elif rec[0] == constants.MEMORIZED_SYMBOL_TMP:
                    rec[0] = constants.MEMORIZED_SYMBOL
                    memorizedRecs.append(rec)

        # add to output file
        with open(outputUrl, 'w', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(constants.FIELDS)
            
            for recToCheck in rawSearchHistory:
                # create searched word field
                searchedWord = recToCheck[0].split("'")
                if len(searchedWord) > 1:
                    isNewWord = True
                    for existedRec in allWordInBook:
                        # if word is new, need to add
                        if searchedWord[1] == existedRec:
                            isNewWord = False
                            break
                    if isNewWord is True:
                        newRecord = [None]*5
                        newRecord[0] = constants.NOT_MEMORIZED_SYMBOL

                        newRecord[1] = searchedWord[1]                    

                        # url field
                        newRecord[2] = recToCheck[1]

                        # date field : convert epoch timestamp to readable date
                        epoch_start = datetime.datetime(constants.EPOCH_START_HOUR_CHROME, constants.EPOCH_START_MINUTE_CHROME, constants.EPOCH_START_SECOND_CHROME)
                        delta = epoch_start + datetime.timedelta(microseconds=int(recToCheck[2]))
                        newRecord[3] = delta

                        # searched count field
                        newRecord[4] = recToCheck[3]
                        writer.writerow(newRecord)
                # if searched word doesn't exist, skip
                else:
                    continue

            writer.writerows(notMemorizedRecs)
            writer.writerows(memorizedRecs)

    # if already output file doens't exist
    else:
        for rec in rawSearchHistory:
            recTmp = [None]*5
            recTmp[0] = constants.NOT_MEMORIZED_SYMBOL

            # create searched word field
            searchedWord = rec[0].split("'")
            if len(searchedWord) > 1:
                recTmp[1] = searchedWord[1]
            else:
                continue

            # url field
            recTmp[2] = rec[1]

            # date field : convert epoch timestamp to readable date
            epoch_start = datetime.datetime(constants.EPOCH_START_HOUR_CHROME, constants.EPOCH_START_MINUTE_CHROME, constants.EPOCH_START_SECOND_CHROME)
            delta = epoch_start + datetime.timedelta(microseconds=int(rec[2]))
            recTmp[3] = delta

            # searched count field
            recTmp[4] = rec[3]
            processedSearchHistory.append(recTmp)

        # output
        with open(outputUrl, 'w', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(constants.FIELDS)
            writer.writerows(processedSearchHistory)
    
    return processedSearchHistory