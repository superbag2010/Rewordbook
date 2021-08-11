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
    if os.path.exists(outputUrl):

        # bakcup origin file
        copyfile(outputUrl, outputBackbupUrl)

        # make word to add to book
        with open(outputUrl, 'r', newline='', encoding='UTF-8') as f:
            newRecs = mkAddedRecsFromList(csv.reader(f), rawSearchHistory)
        with open(outputUrl, 'r', newline='', encoding='UTF-8') as f:
            memorizedRecs, notMemorizedRecs = mkMemorizedRecsFromList(csv.reader(f))

        # add to output file
        with open(outputUrl, 'w', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(constants.FIELDS)
            
            writer.writerows(newRecs)
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


def toGspread(rawSearchHistory):
    a=1


def mkAddedRecsFromList(reader, rawSearchHistory):
    newRecs = []
    for recToCheck in rawSearchHistory:
        # create searched word field
        searchedWord = recToCheck[0].split("'")
        if len(searchedWord) > 1:
            isNewWord = True
            for existedRec in reader:
                # if word is new, need to add
                if searchedWord[1] == existedRec[1]:
                    isNewWord = False
                    break
                
            if isNewWord == True:
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
                newRecs.append(newRecord)
        # if searched word doesn't exist, skip
        else:
            continue

    return newRecs


def mkMemorizedRecsFromList(reader):
    notMemorizedRecs = []
    deletedRecs = []
    memorizedRecs = []
    onceMemorizedRecs = []

    for rec in reader:
        # duplication check
        isExist = False
        if rec[0] == constants.NOT_MEMORIZED_SYMBOL:
            for addedRec in notMemorizedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                notMemorizedRecs.append(rec)
        elif rec[0] == constants.DELETED_SYMBOL:
            for addedRec in deletedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                deletedRecs.append(rec)
        elif rec[0] == constants.MEMORIZED_SYMBOL:
            for addedRec in memorizedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                memorizedRecs.append(rec)
        elif rec[0] == constants.ONCE_MEMORIZED_SYMBOL:
            for addedRec in onceMemorizedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                onceMemorizedRecs.append(rec)

    return notMemorizedRecs, deletedRecs, memorizedRecs, onceMemorizedRecs

def mkNewRecsFromDate(reader, rawSearchHistory):
    newRecs = []
    next(reader)
    lastSearchedDate = next(reader)[3]

    for recToCheck in rawSearchHistory:

        newSearchedDate = datetime.datetime.fromtimestamp(recToCheck['time_usec'] / 1e6).strftime('%Y-%m-%d %H:%M')

        if newSearchedDate > lastSearchedDate:
            if constants.DIC_HOME_URL_NAVER in recToCheck['url']:
                newRecord = [None]*4

                newRecord[0] = constants.NOT_MEMORIZED_SYMBOL

                # searched word field
                newSearchedWord = recToCheck['title'].split("'")
                if len(newSearchedWord) > 1:
                    newRecord[1] = newSearchedWord[1]
                else:
                    continue

                # url field
                newRecord[2] = recToCheck['url']

                # date field : convert epoch timestamp to readable date
                newRecord[3] = newSearchedDate

                # duplication check
                isExist = False
                for rec in newRecs:
                    if rec[1] == newSearchedWord[1]:
                        isExist = True
                        break

                if isExist == False:
                    newRecs.append(newRecord)
        # if old date, break
        else:
            break

    return newRecs