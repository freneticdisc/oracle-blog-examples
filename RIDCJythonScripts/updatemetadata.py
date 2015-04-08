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

# Delete all revisions
binder = client.createBinder ()
binder.putLocal("IdcService", "UPDATE_DOCINFO")

binder.putLocal("dID", "221")
binder.putLocal("dDocName", "000220")
binder.putLocal("dSecurityGroup", "Public")
binder.putLocal("dDocAccount", "")
binder.putLocal("SkipIndexingForUpdate", "false")

# Custom Metadata here
binder.putLocal("xComments", "This is an update")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
