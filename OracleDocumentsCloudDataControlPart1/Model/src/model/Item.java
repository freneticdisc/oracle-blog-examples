package model;

public class Item {
    private Type ItemType;
    private String ID;
    private String Name;
    private String OwnedBy;
    private String CreatedBy;
    private String ModifiedBy;
    private String CreatedTime;
    private String ModifiedTime;
    private long Size;
    private long ChildItemsCount;


    public Item(Type ItemType,
                String ID,
                String Name,
                String OwnedBy,
                String CreatedBy,
                String ModifiedBy,
                String CreatedTime,
                String ModifiedTime,
                long Size,
                long ChildItemsCount) {
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

    public void setSize(long Size) {
        this.Size = Size;
    }

    public long getSize() {
        return Size;
    }

    public void setChildItemsCount(long ChildItemsCount) {
        this.ChildItemsCount = ChildItemsCount;
    }

    public long getChildItemsCount() {
        return ChildItemsCount;
    }
}
