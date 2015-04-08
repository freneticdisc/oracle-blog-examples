/*##############################################################################
# Created By: Justin Paul
# Source:     https://blogs.oracle.com/OracleWebCenterSuite
#
# NOTE: Please note that these code snippets should be used for development and
#       testing purposes only, as such it is unsupported and should not be used
#       on production environments.
##############################################################################*/

package com.oracle.justin.wcc;

import oracle.stellent.ridc.IdcClientManager;
import oracle.stellent.ridc.IdcClient;
import oracle.stellent.ridc.IdcContext;
import oracle.stellent.ridc.model.TransferFile;
import oracle.stellent.ridc.IdcClientConfig;
import oracle.stellent.ridc.protocol.Protocol;
import oracle.stellent.ridc.protocol.Connection;
import oracle.stellent.ridc.model.DataBinder;
import oracle.stellent.ridc.protocol.ServiceResponse;
import oracle.stellent.ridc.IdcClientException;
import oracle.sql.BLOB;

import java.io.ByteArrayInputStream;
import java.io.File;

public class CheckinFileIntoContentServer {
	private static IdcClientManager manager;
	private static IdcClient<IdcClientConfig, Protocol, Connection> client;
	
	public static void main(String[] args) {
		checkinFile("/Users/JustinPaul/Downloads/activation.jar");
	}
	
	// This method will take the file path and checkin the file
	public static String checkinFile(String fPath) {
		String dDocName = "";
		try {
			manager = new IdcClientManager();
			client = (IdcClient<IdcClientConfig, Protocol, Connection>) manager.createClient("idc://10.0.0.5:4444");
			
			IdcContext userContext = new IdcContext("sysadmin");
			DataBinder binder = client.createBinder();
			binder.putLocal("IdcService", "CHECKIN_NEW");
			binder.putLocal("dDocTitle", "Test File - ABC000001");
			binder.putLocal("dDocType", "Document");
			binder.putLocal("dSecurityGroup", "Public");
			binder.putLocal("dDocAccount", "");
			binder.addFile("primaryFile", new TransferFile(new File(fPath)));
			ServiceResponse response = client.sendRequest(userContext, binder);
			DataBinder responsebinder = response.getResponseAsBinder();
			dDocName = responsebinder.getLocal("dDocName");
			client = null;
			manager = null;
		} catch (Exception e) {
			// Nothing to do
			dDocName = e.getLocalizedMessage();
		}
		
		return dDocName;
	}
	
	// This method will take a BLOB field and checkin
	public static String checkinBlob(BLOB bFile, String filename) {
		String dDocName = "";
		try {
			manager = new IdcClientManager();
			client = (IdcClient<IdcClientConfig, Protocol, Connection>) manager.createClient("idc://10.0.0.5:4444");
			
			// Read the BLOB and create a Input Stream
			// Make sure that the files are small as we are using in memory
			byte[] filearray = bFile.getBytes(1, (int) bFile.length());
			ByteArrayInputStream stream = new ByteArrayInputStream(filearray);
			
			IdcContext userContext = new IdcContext("sysadmin");
			DataBinder binder = client.createBinder();
			binder.putLocal("IdcService", "CHECKIN_NEW");
			binder.putLocal("dDocTitle", "Test File - ABC000002");
			binder.putLocal("dDocType", "Document");
			binder.putLocal("dSecurityGroup", "Public");
			binder.putLocal("dDocAccount", "");
			binder.addFile("primaryFile", new TransferFile(stream, filename, bFile.length()));
			ServiceResponse response = client.sendRequest(userContext, binder);
			DataBinder responsebinder = response.getResponseAsBinder();
			dDocName = responsebinder.getLocal("dDocName");
			client = null;
			manager = null;
		} catch (Exception e) {
			// Nothing to do
			dDocName = e.getLocalizedMessage();
		}
		
		return dDocName;
	}
}
