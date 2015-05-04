   CREATE
    INDEX dev1_ocs.classcats_idx
       ON dev1_ocs.classificationcategories(categoryselectionrule)
INDEXTYPE
       IS ctxsys.ctxrule;

   CREATE
       OR
  REPLACE
 FUNCTION dev1_ocs.categorizeDocument(
 		     ddocname IN VARCHAR2,
 		     activeindex IN VARCHAR2)
   RETURN VARCHAR2
       IS
       		b_docfulltext	BLOB;
         	c_document    	CLOB;
			i_dest_offset   INTEGER := 1;
			i_src_offset    INTEGER := 1;
			i_lang_context  INTEGER := dbms_lob.default_lang_ctx;
			i_warning     	INTEGER;
			v_catgegories	VARCHAR2(200) := '';
    BEGIN
    	 	dbms_lob.createtemporary(c_document, true);
    	 	  EXECUTE
    	 	IMMEDIATE 'select ddocname, DDOCFULLTEXT from IDCCOLL2 where ddocname = '000823''
    	 	     INTO b_docfulltext;
    	 	dbms_lob.converttoclob(c_document,
                          		   b_docfulltext,
                          		   dbms_lob.lobmaxsize,
                          		   i_dest_offset,
                          		   i_src_offset,
                          		   dbms_lob.default_csid,
                          		   i_lang_context,
                          		   i_warning);
            FOR cat IN (SELECT categoryid FROM classificationcategories WHERE MATCHES(categoryselectionrule, c_document) > 0)
            LOOP
            	v_catgegories := v_catgegories || cat.categoryid || ',';
            END LOOP;
            dbms_lob.freetemporary(c_document);
            v_catgegories := TRIM(TRAILING ',' FROM v_catgegories);
            RETURN v_catgegories;
EXCEPTION
		 	WHEN OTHERS
		 	THEN RETURN '';
      END;

/
