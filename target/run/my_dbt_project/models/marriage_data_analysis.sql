
  
    

  create  table "dbt_test"."india_data"."marriage_data_analysis__dbt_tmp"
  
  
    as
  
  (
    -- models/marriage_data_analysis.sql


SELECT 
  *
  -- Add any transformations here
FROM "dbt_test"."india_data"."marriage_data"
  );
  