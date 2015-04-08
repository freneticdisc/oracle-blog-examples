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
from oracle.stellent.ridc.model import TransferFile
from java.io import File

manager = IdcClientManager ()
client = manager.createClient ("idc://127.0.0.1:4444")
userContext = IdcContext ("weblogic")
# client = manager.createClient ("http://127.0.0.1:16200/cs/idcplg")
# userContext = IdcContext ("<user>", "<password>")

# Checkin a new file
binder = client.createBinder ()
binder.putLocal("IdcService", "CHECKIN_NEW")

# Comment the line below if you do not want to put the file in a folder
# Meatadata defaults are copied from the folder except SecurityGroup and Account
binder.putLocal("fParentGUID", "D638FE6CBE83C59B488AF5DDC70AD77F")

binder.putLocal("dDocName", "ABC000001")
binder.putLocal("dDocTitle", "Test File - ABC000001")
binder.putLocal("dDocType", "Document")
binder.putLocal("dSecurityGroup", "Public")
binder.putLocal("dDocAccount", "")
binder.addFile("primaryFile", TransferFile(File("abc.txt")))

# Custom Metadata here
binder.putLocal("xComments", "This is new content - revision 1")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
localData = responseBinder.getLocalData ()
dDocName = localData.get ("dDocName")
dID = localData.get ("dID")

# Checkin a new revision
# Need to checkout first
binder = client.createBinder ()
binder.putLocal("IdcService", "CHECKOUT")
binder.putLocal("dID", dID)
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()

binder = client.createBinder ()
binder.putLocal("IdcService", "CHECKIN_SEL")

binder.putLocal("dID", dID)
binder.putLocal("dDocName", dDocName)
binder.putLocal("dDocTitle", "Test File 2 - ABC000001")
binder.putLocal("dSecurityGroup", "Public")
binder.putLocal("dDocAccount", "")
binder.putLocal("doFileCopy", "1")
binder.addFile("primaryFile", TransferFile(File("createnewfolderandsubfolders.py")))

# Custom Metadata here
binder.putLocal("xComments", "This is a new revision - revision 2")

# get the response
response = client.sendRequest (userContext, binder)
responseBinder = response.getResponseAsBinder ()
