/*##############################################################################
# Created By: Justin Paul
# Source:     https://blogs.oracle.com/OracleWebCenterSuite
#
# NOTE: Please note that these code snippets should be used for development and
#       testing purposes only, as such it is unsupported and should not be used
#       on production environments.
##############################################################################*/
package model;

import javax.ws.rs.core.UriBuilder;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;
import com.sun.jersey.api.client.config.ClientConfig;
import com.sun.jersey.api.client.config.DefaultClientConfig;
import java.io.ByteArrayInputStream;
import java.util.List;
import java.util.ArrayList;
import java.util.ResourceBundle;
import javax.xml.bind.DatatypeConverter;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.xpath.XPathFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

public class ItemsDC {
    private String serviceURL;
    private String userName;
    private String password;
    private String baseFolderID;
    
    public ItemsDC() {
        super();
        ResourceBundle resources = ResourceBundle.getBundle("Model");
        this.serviceURL = resources.getString("ServiceURL");
        this.userName = resources.getString("UserName");
        this.password = resources.getString("Password");
        this.baseFolderID = resources.getString("BaseFolderID");
    }
    
    public List<Item> listItemsInBaseFolder () {
        return listItemsInFolder(baseFolderID);
    }
    
    public List<Item> listItemsInFolder (String folderid) {
        List<Item> items = new ArrayList<Item>();
        
        if (folderid == null || folderid.equals("")) {
            folderid = baseFolderID;
        }
        String sUrl = serviceURL + "/folders/" + folderid + "/items";
        String authString = userName + ":" + password;
        byte[] bAuthString = authString.getBytes();
        String encodedAuthString = "Basic " + DatatypeConverter.printBase64Binary(bAuthString);
        
        ClientConfig config = new DefaultClientConfig();
        Client client = Client.create(config);
        WebResource service = client.resource(UriBuilder.fromUri(sUrl).build());
        ClientResponse response = service.
                                    header("Authorization", encodedAuthString).
                                    header("Accept", "application/xml").
                                    get(ClientResponse.class);

        if (response.getStatus() == ClientResponse.Status.OK.getStatusCode()) {
            byte[] xmlDoc = response.getEntity(String.class).getBytes();
            
            try {
                DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
                DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
                
                Document doc = dBuilder.parse(new ByteArrayInputStream(xmlDoc));
                doc.getDocumentElement().normalize();
                                
                XPathFactory xPathfactory = XPathFactory.newInstance();
                XPath xpath = xPathfactory.newXPath();
                
                Item item = new Item();
                item.setItemType(Type.FOLDER);
                
                XPathExpression expr = xpath.compile("/resource/id");
                item.setID((String) expr.evaluate(doc, XPathConstants.STRING));
                item.setParentID("");
                item.setName("..");
                
                expr = xpath.compile("/resource/parentID");
                item.setID((String) expr.evaluate(doc, XPathConstants.STRING));
                
                expr = xpath.compile("/resource/ownedBy/displayName");
                item.setOwnedBy((String) expr.evaluate(doc, XPathConstants.STRING));
                
                expr = xpath.compile("/resource/createdBy/displayName");
                item.setCreatedBy((String) expr.evaluate(doc, XPathConstants.STRING));
                
                expr = xpath.compile("/resource/modifiedBy/displayName");
                item.setModifiedBy((String) expr.evaluate(doc, XPathConstants.STRING));
                
                expr = xpath.compile("/resource/createdTime");
                item.setCreatedTime((String) expr.evaluate(doc, XPathConstants.STRING));
                
                expr = xpath.compile("/resource/modifiedTime");
                item.setModifiedTime((String) expr.evaluate(doc, XPathConstants.STRING));
                
                expr = xpath.compile("/resource/size");
                item.setSize((Double) expr.evaluate(doc, XPathConstants.NUMBER));
                
                expr = xpath.compile("/resource/childItemsCount");
                item.setChildItemsCount((Double) expr.evaluate(doc, XPathConstants.NUMBER));
                
                if (item.getID() != null && !item.getID().equals(""))
                    items.add(item);
                
                expr = xpath.compile("/resource/items/item");
                NodeList nl = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
                
                for (int i = 1; i < nl.getLength() + 1; i++) {
                    item = new Item();
                    expr = xpath.compile("/resource/items/item[" + i + "]/type");
                    item.setItemType((expr.evaluate(doc, XPathConstants.STRING).equals("folder") ? Type.FOLDER : Type.FILE));
                    expr = xpath.compile("/resource/items/item[" + i + "]/id");
                    item.setID((String)expr.evaluate(doc, XPathConstants.STRING));
                    expr = xpath.compile("/resource/items/item[" + i + "]/parentID");
                    item.setParentID((String)expr.evaluate(doc, XPathConstants.STRING));
                    expr = xpath.compile("/resource/items/item[" + i + "]/name");
                    item.setName((String)expr.evaluate(doc, XPathConstants.STRING));
                    expr = xpath.compile("/resource/items/item[" + i + "]/ownedBy/displayName");
                    item.setOwnedBy((String)expr.evaluate(doc, XPathConstants.STRING));
                    expr = xpath.compile("/resource/items/item[" + i + "]/createdBy/displayName");
                    item.setCreatedBy((String)expr.evaluate(doc, XPathConstants.STRING));
                    expr = xpath.compile("/resource/items/item[" + i + "]/modifiedBy/displayName");
                    item.setModifiedBy((String)expr.evaluate(doc, XPathConstants.STRING));
                    expr = xpath.compile("/resource/items/item[" + i + "]/createdTime");
                    item.setCreatedTime((String)expr.evaluate(doc, XPathConstants.STRING));
                    expr = xpath.compile("/resource/items/item[" + i + "]/modifiedTime");
                    item.setModifiedTime((String)expr.evaluate(doc, XPathConstants.STRING));
                    expr = xpath.compile("/resource/items/item[" + i + "]/size");
                    item.setSize((Double)expr.evaluate(doc, XPathConstants.NUMBER));
                    expr = xpath.compile("/resource/items/item[" + i + "]/childItemsCount");
                    item.setChildItemsCount((item.getItemType() == Type.FOLDER) ? (Double)expr.evaluate(doc, XPathConstants.NUMBER) : 0);
                    items.add(item);
                }
            } catch(Exception e) {
                System.out.println(e.toString());
            }
        }
        
        return items;
    }
    
    public static void main(String[] args) {
        ItemsDC it = new ItemsDC();
        it.listItemsInBaseFolder();
    }
}
