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
binder.putLocal("IdcService", "FLD_UNFILE")

# Unfile one or more items from the Folders hierarchy
# You can move multiple items as item1, item2, item3, ..., item[n]

# Item1 - File
binder.putLocal("item3", "fFileGUID:8F9E18BB9D8609A0E07F391C8A3737F4")
# binder.putLocal("item3", "path:/Enterprise Libraries/My Library/Folder4/file1.txt")

# Item2 - File
# binder.putLocal("item4", "fFileGUID:8F9E18BB9D8609A0E07F391C8A3737F4")
binder.putLocal("item4", "path:/Enterprise Libraries/My Library/Folder4/file2.txt")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
