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
binder.putLocal("IdcService", "FLD_MOVE")

# 1 to overwrite, 0 to leave
binder.putLocal("overwrite", "1")

# Use any one of the identified for destination folder
binder.putLocal("destination", "fFolderGUID:D638FE6CBE83C59B488AF5DDC70AD77F")
# binder.putLocal("destination", "path:/Enterprise Libraries/My Library/Folder1/Destination")

# You can move multiple items as item1, item2, item3, ..., item[n]
# Item1 - Folder
binder.putLocal("item1", "fFolderGUID:9386AC92919EF4A8C022D3EA47E63B52")
# binder.putLocal("item1", "path:/Enterprise Libraries/My Library/Folder2")

# Item2 - Folder
# binder.putLocal("item2", "fFolderGUID:9386AC92919EF4A8C022D3EA47E63B76")
binder.putLocal("item2", "path:/Enterprise Libraries/My Library/Folder3")

# Item3 - File
binder.putLocal("item3", "fFileGUID:F868B260B75DED9CD7A37F0A1CD703BD")
# binder.putLocal("item3", "path:/Enterprise Libraries/My Library/Folder4/file1.txt")

# Item4 - File
# binder.putLocal("item4", "fFileGUID:8F9E18BB9D8609A0E07F391C8A3737F4")
binder.putLocal("item4", "path:/Enterprise Libraries/My Library/Folder4/file2.txt")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
