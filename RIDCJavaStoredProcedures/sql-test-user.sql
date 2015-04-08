  CREATE
      OR
 REPLACE
FUNCTION test.checkinFile(fPath IN VARCHAR2)
  RETURN VARCHAR2
      AS LANGUAGE JAVA
    NAME 'com.oracle.justin.wcc.CheckinFileIntoContentServer.checkinFile(java.lang.String) return java.lang.String';
    
  CREATE
      OR
 REPLACE
FUNCTION test.checkinBlob(bFile IN BLOB, filename IN VARCHAR2)
  RETURN VARCHAR2
      AS LANGUAGE JAVA
    NAME 'com.oracle.justin.wcc.CheckinFileIntoContentServer.checkinBlob(oracle.sql.BLOB, java.lang.String) return java.lang.String';
    
CREATE TABLE TEST.blob_table (
  fileid INTEGER NOT NULL,
  filename VARCHAR2(255) NOT NULL,
  filedata BLOB
);

/
