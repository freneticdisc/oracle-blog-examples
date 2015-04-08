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
binder.putLocal("IdcService", "FLD_PROPAGATE")

# Set to 1 to propagate metadata to documents pointed to by soft links
binder.putLocal("propagateThroughSoftLinks", "1")

binder.putLocal("fFolderGUID", "D7B0D24CEE5C70CB3B8AD13809DD2505")

# You can propagate multiple metadata, just repeat the 2 lines below
# Set to 1 to propagate the specified field
binder.putLocal("dSecurityGroup:isSelected", "1")
binder.putLocal("dSecurityGroup", "Public")

binder.putLocal("dDocAccount:isSelected", "1")
binder.putLocal("dDocAccount", "abc")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
