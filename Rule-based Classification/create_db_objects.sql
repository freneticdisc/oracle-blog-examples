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
            b_docfulltext   BLOB;
            c_document      CLOB;
            i_dest_offset   INTEGER := 1;
            i_src_offset    INTEGER := 1;
            i_lang_context  INTEGER := dbms_lob.default_lang_ctx;
            i_warning       INTEGER;
            v_categories    VARCHAR2(200) := '';
            v_query         VARCHAR2(100) := 'SELECT ';
    BEGIN
                IF (INSTR(activeindex, 'IDCCOLL') = 1)
              THEN
                   v_query := v_query || 'ddocfulltext';
             ELSIF (INSTR(activeindex, 'IDCTEXT') = 1)
              THEN
                   v_query := v_query || 'otscontent';
              ELSE
                   v_query := v_query || '''X''';
            END IF;

            v_query := v_query || '  FROM ' || activeindex;
            v_query := v_query || ' WHERE ddocname = :1';
            dbms_lob.createtemporary(c_document, true);
              EXECUTE
            IMMEDIATE v_query
                 INTO b_docfulltext
                USING ddocname;
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
                v_categories := v_categories || cat.categoryid || ', ';
            END LOOP;
            dbms_lob.freetemporary(c_document);
            v_categories := TRIM(TRAILING ' ' FROM v_categories);
            v_categories := TRIM(TRAILING ',' FROM v_categories);
            RETURN v_categories;
EXCEPTION
            WHEN OTHERS
            THEN RETURN '';
      END;

/
