################################################################################
# Created By: Justin Paul
# Source:     https://blogs.oracle.com/OracleWebCenterSuite
#
# NOTE: Please note that these code snippets should be used for development and
#       testing purposes only, as such it is unsupported and should not be used
#       on production environments.
################################################################################

from oracle.stellent.ridc import IdcClientManager
from oracle.stellent.ridc import IdcContext

manager = IdcClientManager ()
client = manager.createClient ("idc://127.0.0.1:4444")
userContext = IdcContext ("weblogic")
# client = manager.createClient ("http://127.0.0.1:16200/cs/idcplg")
# userContext = IdcContext ("<user>", "<password>")

binder = client.createBinder ()
binder.putLocal("IdcService", "FLD_BROWSE")

# Specify one of the following
# binder.putLocal("item", "[path:<path>|fFolderGUID:<GUID>]")
# binder.putLocal("items", "[path:<path>|fFolderGUID:<GUID>], ...")
# binder.putLocal("path", "<path>")
binder.putLocal("fFolderGUID", "AF9D359824F9B32515C166EEF2D9A5FE")

# Specifies the Folders Application of the location to which the user is browsing
# binder.putLocal("fldapp", "framework")

# Performs the service in a combined pagination mode, default is 0
binder.putLocal("doCombinedBrowse", "1")

# Lists folders before files in the combined pagination mode, default is 1
binder.putLocal("foldersFirst", "1")

# The number of folders to return, default is 50
binder.putLocal("folderCount", "50")

# The row number at which to start returning data and is used for pagination, default is 0
binder.putLocal("folderStartRow", "0")

# The number of files to return, default is 50
binder.putLocal("fileCount", "50")

# The row number at which to start returning data and is used for pagination, default is 0
binder.putLocal("fileStartRow", "0")

# The number of items (folders plus files) to return, default is 100
binder.putLocal("combinedCount", "100")

# The row number at which to start returning data and is used for pagination, default is 0
binder.putLocal("combinedStartRow", "0")

# Returns target folder's information for all shortcuts retrieved in the ChildTargetFolders ResultSet, default is 0
binder.putLocal("doRetrieveTargetInfo", "0")

# Adds a fIsFavorite field in the ResultSet to indicate if the folder or file is favorite
# (if it has a shortcut in the Favorites folder), default is 0
binder.putLocal("doMarkFavorites", "0")

# Adds a URL field in the files ResultSet that is the absolute Web location of the document, default is 0
binder.putLocal("doRetrieveDocumentURL", "0")

# Post processes the results to return only unique links, default is 0
binder.putLocal("doRetrieveUniqueLinks", "0")

# The comma-delinated list of filter parameters for the browse
# For example, foldersFilterParams=fIsContribution&fIsContribution=1 will return folders with fIsContribution=1
# binder.putLocal("foldersFilterParams", "")

# Standard query for filtering out the folders
# For example, foldersFilterQuery=fFolderName<substring>`test`
# binder.putLocal("foldersFilterQuery", "")

# Standard query for filtering out the files
# For example, filesFilterQuery=fFileName<substring>`test`
# binder.putLocal("filesFilterQuery", "")

# Field name from the FolderFolders table on which to sort the records
# binder.putLocal("foldersSortField", "")

# Specify Asc or Desc for an ascending or descending sort
# binder.putLocal("foldersSortOrder", "")

# The comma-delinated list of filter parameters on the browse
# For example, filesFilterParams=fOwner&fOwner=sysadmin will return folders with fOwner=sysadmin
# binder.putLocal("filesFilterParams", "")

# If set to Folders, this filters results to only include folders that are favorites
# If set to Files, this filters only files that are favorites
# If set to 1, this filters both folders and files that are favorites
# By default, this filters none
# binder.putLocal("filterFavorites", "1")

# If set to Folders, this filters results to only include folders that are followed
# If set to Files, this filters only files that are followed
# If set to 1, this filters both folders and files that are followed
# By default, it filters none
# binder.putLocal("filterFollows", "1")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
print responseBinder

# Print Local data
localData = responseBinder.getLocalData ()
for key in localData:
    print key + ": " + localData.get(key)

# Get current folder information
fInfo = responseBinder.getResultSet("FolderInfo")
fFields = fInfo.getFields()
fRows = fInfo.getRows()
for fChild in fRows:
    for fField in fFields:
        print fField.getName() + ": " + fChild.get(fField.getName())

# Loop through the child folders
fChildFolders = responseBinder.getResultSet("ChildFolders")
fFields = fChildFolders.getFields()
fRows = fChildFolders.getRows()
for fChild in fRows:
    for fField in fFields:
        print fField.getName() + ": " + fChild.get(fField.getName())
    
# Loop through the child files
fChildFiles = responseBinder.getResultSet("ChildFiles")
fFields = fChildFiles.getFields()
fRows = fChildFiles.getRows()
for fChild in fRows:
    for fField in fFields:
        print fField.getName() + ": " + fChild.get(fField.getName())
