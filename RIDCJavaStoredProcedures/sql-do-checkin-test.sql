CREATE OR REPLACE DIRECTORY TEMP_DIR AS '/tmp/';
DECLARE
  vblob BLOB;
  filename  VARCHAR2(200);
  lbloblen  INTEGER;
  lfile  UTL_FILE.FILE_TYPE;
  lbuffer  RAW(32767);
  lamount  BINARY_INTEGER := 32767;
  lpos INTEGER := 1;
BEGIN
  -- Save the file to a temporary location
  -- and checkin the file
  SELECT filename,
         filedata
    INTO filename,
         vblob
    FROM blob_table
   WHERE fileid = 1;
   
  lbloblen := DBMS_LOB.getlength(vblob);
  lfile := UTL_FILE.FOPEN('TEMP_DIR', 'file1.txt', 'w', 32767);
  WHILE lpos < lbloblen LOOP
    DBMS_LOB.READ(vblob, lamount, lpos, lbuffer);
    UTL_FILE.PUT_RAW(lfile, lbuffer, TRUE);
    lpos := lpos + lamount;
  END LOOP;
  UTL_FILE.FCLOSE(lfile);
  DBMS_OUTPUT.PUT_LINE ('dDocname: ' || CHECKINFILE('/tmp/' || filename));
  
  -- IN MEMORY file checkin
  SELECT filename,
         filedata
    INTO filename,
         vblob
    FROM blob_table
   WHERE fileid = 2;
   DBMS_OUTPUT.PUT_LINE ('dDocname: ' || CHECKINBLOB(vblob, filename));
EXCEPTION
  WHEN OTHERS THEN
    IF UTL_FILE.IS_OPEN(lfile) THEN
      UTL_FILE.FCLOSE(lfile);
    END IF;
END;
