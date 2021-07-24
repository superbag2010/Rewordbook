import fetch
import constants
import export

# get searched history data
rawSearchHistory = fetch.getSearchHitoryFromLocal(constants.CHROME)

# output to csv file
export.toCSV(rawSearchHistory)