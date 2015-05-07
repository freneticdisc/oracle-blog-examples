DECLARE
		v_cats VARCHAR2(200) := '';
		v_indx VARCHAR2(8)	  := 'IDCCOLL2';
 CURSOR content_released_today
     IS
        SELECT did,
        	   ddocname
          FROM revisions
         WHERE TRUNC(dreleasedate) = TRUNC(SYSDATE);
  BEGIN
  		 	  FOR content IN content_released_today
  		     LOOP
  		     	  v_cats := dev1_ocs.categorizeDocument(content.ddocname, v_indx);
  		     	      IF NVL(v_cats, 'NULL') <> 'NULL'
  		     	    THEN
  		     	  		 UPDATE dev1_ocs.docmeta
  		     	     		SET xclassificationcategory = v_cats
  		     	   		  WHERE did = content.did;
  		     	  		 UPDATE dev1_ocs.revisions
  		     	     		SET dreleasestate = 'U'
  		     	   		  WHERE did = content.did;
  		     	  END IF;
  		 END LOOP;
  		   COMMIT;
    END;