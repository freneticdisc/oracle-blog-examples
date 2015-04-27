/*##############################################################################
# Created By: Justin Paul
# Source:     https://blogs.oracle.com/OracleWebCenterSuite
#
# NOTE: Please note that these code snippets should be used for development and
#       testing purposes only, as such it is unsupported and should not be used
#       on production environments.
##############################################################################*/
package model;

public class Item {
    private Type ItemType;
    private String ID;
    private String ParentID;
    private String Name;
    private String OwnedBy;
    private String CreatedBy;
    private String ModifiedBy;
    private String CreatedTime;
    private String ModifiedTime;
    private Double Size;
    private Double ChildItemsCount;

    public Item() {
        super();
    }

    public Item(Type ItemType,
                String ID,
                String Name,
                String OwnedBy,
                String CreatedBy,
                String ModifiedBy,
                String CreatedTime,
                String ModifiedTime,
                Double Size,
                Double ChildItemsCount) {
        super();
        this.ItemType = ItemType;
        this.ID = ID;
        this.Name = Name;
        this.OwnedBy = OwnedBy;
        this.CreatedBy = CreatedBy;
        this.ModifiedBy = ModifiedBy;
        this.CreatedTime = CreatedTime;
        this.ModifiedTime = ModifiedTime;
        this.Size = Size;
        this.ChildItemsCount = ChildItemsCount;
    }

    public void setItemType(Type ItemType) {
        this.ItemType = ItemType;
    }

    public Type getItemType() {
        return ItemType;
    }

    public void setID(String ID) {
        this.ID = ID;
    }

    public String getID() {
        return ID;
    }
    
    public void setParentID(String ParentID) {
        this.ParentID = ParentID;
    }

    public String getParentID() {
        return ParentID;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public String getName() {
        return Name;
    }

    public void setOwnedBy(String OwnedBy) {
        this.OwnedBy = OwnedBy;
    }

    public String getOwnedBy() {
        return OwnedBy;
    }

    public void setCreatedBy(String CreatedBy) {
        this.CreatedBy = CreatedBy;
    }

    public String getCreatedBy() {
        return CreatedBy;
    }

    public void setModifiedBy(String ModifiedBy) {
        this.ModifiedBy = ModifiedBy;
    }

    public String getModifiedBy() {
        return ModifiedBy;
    }

    public void setCreatedTime(String CreatedTime) {
        this.CreatedTime = CreatedTime;
    }

    public String getCreatedTime() {
        return CreatedTime;
    }

    public void setModifiedTime(String ModifiedTime) {
        this.ModifiedTime = ModifiedTime;
    }

    public String getModifiedTime() {
        return ModifiedTime;
    }

    public void setSize(Double Size) {
        this.Size = Size;
    }

    public Double getSize() {
        return Size;
    }

    public void setChildItemsCount(Double ChildItemsCount) {
        this.ChildItemsCount = ChildItemsCount;
    }

    public Double getChildItemsCount() {
        return ChildItemsCount;
    }
    
    public boolean isFile() {
        return (this.ItemType == Type.FILE) ? true : false;
    }
    
    public boolean isFolder() {
        return (this.ItemType == Type.FOLDER) ? true : false;
    }
}
