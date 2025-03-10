-- models/marriage_data_analysis.sql
{{
  config(
    materialized='table'
  )
}}

SELECT 
  *
  -- Add any transformations here
FROM {{ source('india_data', 'marriage_data') }}