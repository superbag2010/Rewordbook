import datetime
import userConfig
import constants

'''
comparing search date,
get new record from chorme search history of naver dictionary
'''
def getNewRecsCompDate(csvReader, rawSearchHistory):
    # records added to rewordbook
    newRecs = []

    # skip field row
    next(csvReader)

    # get latest date in old rewordbook
    oldLatestSearchedDate = next(csvReader)[3]
    
    for rawRec in rawSearchHistory:
        # get searched date each search record
        searchedDate = datetime.datetime.fromtimestamp(rawRec['time_usec'] / 1e6).strftime('%Y-%m-%d %H:%M')

        # if searched date is more recent than record in old rewordbook
        if searchedDate > oldLatestSearchedDate:
            # if 'url of searched record' contain dictionary home url
            if userConfig.DIC_HOME_URL_NAVER in rawRec['url']:
                # make record to add to new rewordbook
                newRec = [None]*4
                # column1. memorized
                newRec[0] = userConfig.NOT_MEMORIZED_WORD_SYMBOL

                # column2. searched word column
                rawNewSearchedWordSplitedByApostrophe = rawRec['title'].split("'")
                # if not (len>1), searched word is blanck in naver dictionary
                if len(rawNewSearchedWordSplitedByApostrophe) > 1:
                    newRec[1] = rawNewSearchedWordSplitedByApostrophe[1]
                else:
                    continue

                # column3. url
                newRec[2] = rawRec['url']
                # column4. date(convert epoch timestamp to readable date)
                newRec[3] = searchedDate

                # do duplication check before add to rewordbook
                isExist = False
                for addedRec in newRecs:
                    if addedRec[1] == newRec[1]:
                        isExist = True
                        break
                # if not duplicate, add
                if isExist == False:
                    newRecs.append(newRec)
        
        # if aleary exist in rewordbook, skip
        else:
            break
    
    return newRecs


'''
aling words in old rewordbook as symbol
'''
def getRecsAsMemorizedSymbol(csvReader):
    notMemorizedRecs = []
    excludedRecs = []
    memorizedRecs = []
    onceMemorizedRecs = []

    # skip field row
    next(csvReader)

    for rec in csvReader:
        # add to each symboled list after duplication check
        isExist = False
        # make list of not memorized words
        if rec[0] == userConfig.NOT_MEMORIZED_WORD_SYMBOL:
            for addedRec in notMemorizedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                notMemorizedRecs.append(rec)
        # make list of excluded words
        elif rec[0] == userConfig.EXCLUDED_WORD_SYMBOL:
            for addedRec in excludedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                excludedRecs.append(rec)
        # make list of memorized words
        elif rec[0] == userConfig.MEMORIZED_WORD_SYMBOL:
            for addedRec in memorizedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                memorizedRecs.append(rec)
        # make list of once memorized words
        elif rec[0] == userConfig.ONCE_MEMORIZED_WORD_SYMBOL:
            for addedRec in onceMemorizedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                onceMemorizedRecs.append(rec)
        # if other symbols add to not memorized list
        else:
            for addedRec in notMemorizedRecs:
                if addedRec[1] == rec[1]:
                    isExist = True
                    break
            if isExist == False:
                notMemorizedRecs.append(rec)

    return notMemorizedRecs, excludedRecs, memorizedRecs, onceMemorizedRecs

'''
get records added to initial rewordbook
'''
def getRecs(rawSearchHistory):
    recsToAdd = []
    for rawRec in rawSearchHistory:
        if userConfig.DIC_HOME_URL_NAVER in rawRec['url']:
            recToAdd = [None]*4
            # column1. memorized
            recToAdd[0] = userConfig.NOT_MEMORIZED_WORD_SYMBOL

            # column2. searched word column
            rawNewSearchedWordSplitedByApostrophe = rawRec['title'].split("'")
            # if not (len>1), searched word is blanck in naver dictionary
            if len(rawNewSearchedWordSplitedByApostrophe) > 1:
                recToAdd[1] = rawNewSearchedWordSplitedByApostrophe[1]
            else:
                continue
            # column3. url
            recToAdd[2] = rawRec['url']
            # column4. date:convert epoch timestamp to readable date('%Y-%m-%dT%H:%M:%S.%f', '2013-02-07T17:30:03.083988')
            recToAdd[3] = datetime.datetime.fromtimestamp(rawRec['time_usec'] / 1e6).strftime('%Y-%m-%d %H:%M')

            # duplication check
            isExist = False
            for addedRec in recsToAdd: 
                if addedRec[1] == recToAdd[1]:
                    isExist = True
                    break
            # if no duplicate, add
            if isExist == False:
                recsToAdd.append(recToAdd)

    return recsToAdd