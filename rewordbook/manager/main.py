import fetch
import constants
import export

# get searched history data
rawSearchHistory = fetch.getSearchHitoryFromLocal(constants.CHROME)

# output to csv file
history = export.toCSV(rawSearchHistory)