import json

def getFromGoogleAccountHistoryFile(historyJsoneUrl):
    json_open = open(historyJsoneUrl, 'r')
    json_load = json.load(json_open)['Browser History']
    return json_load