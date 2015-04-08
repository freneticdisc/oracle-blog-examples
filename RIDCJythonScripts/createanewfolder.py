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
binder.putLocal("IdcService", "FLD_CREATE_FOLDER")
binder.putLocal("fParentGUID", "3A26D8CE011B9C8BE6B9CB1F32BD52FD")  # This is the GUID of the parent folder
binder.putLocal("fFolderName", "Folder1")
binder.putLocal("fFolderType", "owner")
binder.putLocal("fApplication", "framework")
binder.putLocal("fInhibitPropagation", "0")
binder.putLocal("fPromptForMetadata", "1")
binder.putLocal("fSecurityGroup", "Public")
binder.putLocal("fDocAccount", "")

# List the default metadata for this folder here
binder.putLocal("xComments", "This is a new folder")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
localData = responseBinder.getLocalData ()
fFolderGUID = localData.get ("fFolderGUID")
print fFolderGUID
