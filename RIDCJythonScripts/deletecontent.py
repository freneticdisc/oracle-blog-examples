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
binder.putLocal("IdcService", "DELETE_DOC")

binder.putLocal("dID", "463")
binder.putLocal("dDocName", "ABC000001")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()

# Delete a single revision
binder = client.createBinder ()
binder.putLocal("IdcService", "DELETE_REV")

binder.putLocal("dID", "422")
binder.putLocal("dDocName", "000421")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
