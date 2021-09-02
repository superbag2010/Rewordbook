import fetch
import extract
import userConfig
import constants

import os
import csv
from datetime import date
from shutil import copyfile

'''
In this module, make rewordbook as userConfig.py
'''

# get search history data
rawHistory = fetch.getFromGoogleAccountHistoryFile(userConfig.GOOGLE_ACCOUNT_HISTORY_URL)

# url of rewordbook(output file)
rewordbookUrl = os.path.join(userConfig.OUTPUT_PATH, userConfig.REWORDBOOK_FILENAME + '.' + userConfig.REWORDBOOK_FORMAT)

# if already rewordbook file exist
if os.path.exists(rewordbookUrl):
    # if backup setting is on,
    if userConfig.DO_BACKUP:
        # do backup
        backupFileUrl = os.path.join(userConfig.BACKUP_PATH, userConfig.REWORDBOOK_FILENAME + str(date.today()) + '.' + userConfig.REWORDBOOK_FORMAT)
        copyfile(rewordbookUrl, backupFileUrl)

    # extract new word search record(comparing search date).
    with open(rewordbookUrl, 'r', newline='', encoding='UTF-8') as rewordbook:
        newWordRecs = extract.getNewRecsCompDate(csv.reader(rewordbook), rawHistory)
    
    # extract word search record as word status(memorized, not memorized, etc.)
    with open(rewordbookUrl, 'r', newline='', encoding='UTF-8') as rewordbook:
        notMemorizedWordRecs, excludedWordRecs, memorizedWordRecs, onceMemorizedWordRecs = extract.getRecsAsMemorizedSymbol(csv.reader(rewordbook))
    
    # make rewordbook
    with open(rewordbookUrl, 'w', newline='', encoding='UTF-8') as rewordbook:
        writer = csv.writer(rewordbook)
        writer.writerow(constants.FIELDS)
        writer.writerows(newWordRecs)
        writer.writerows(notMemorizedWordRecs)
        writer.writerows(excludedWordRecs)
        writer.writerows(memorizedWordRecs)
        writer.writerows(onceMemorizedWordRecs)
    

# if rewordbook file doesn't exist
else:
    # extract all search word
    wordRecs = extract.getRecs(rawHistory)

    # make rewordbook
    with open(rewordbookUrl, 'w', newline='', encoding='UTF-8') as rewordbook:
        writer = csv.writer(rewordbook)
        writer.writerow(constants.FIELDS)
        writer.writerows(wordRecs)