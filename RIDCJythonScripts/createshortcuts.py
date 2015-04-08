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

# Create shortcut for a folder
# The user must have logged in at least once to have the profile folder created
username="weblogic"
binder = client.createBinder ()
binder.putLocal("IdcService", "FLD_CREATE_FOLDER")
binder.putLocal("fParentGUID", "5517F2B282C5KJB40E5574E4D5AU7Y9A")  # This is the GUID of the parent folder
binder.putLocal("fTargetGUID", "5517F2B282C574B40E5574E4D5AF1C9A")  # This is the GUID of original folder
binder.putLocal("fFolderName", "My Shortcut to Folder1")
binder.putLocal("fFolderType", "soft")
userContext = IdcContext (username)

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()

# Create shortcut for a file
# The user must have logged in at least once to have the profile folder created
username="weblogic"
binder = client.createBinder ()
binder.putLocal("IdcService", "FLD_CREATE_FILE")
binder.putLocal("fParentGUID", "5517F2B282C5KJB40E5574E4D5AU7Y9A")  # This is the GUID of the parent folder
binder.putLocal("fFileName", "My Shortcut to dDocName - 000421")
binder.putLocal("dDocName", "000421")
binder.putLocal("fFileType", "soft")
userContext = IdcContext (username)

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
