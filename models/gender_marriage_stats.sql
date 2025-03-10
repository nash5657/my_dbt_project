-- models/gender_marriage_stats.sql
{{
  config(
    materialized='table'
  )
}}

SELECT 
  Gender,
  Education_Level,
  Income_Level,
  AVG(Age_at_Marriage) AS avg_age_at_marriage,
  COUNT(*) AS count,
  AVG(Years_Since_Marriage) AS avg_marriage_duration,
  SUM(CASE WHEN Spouse_Working = 'Yes' THEN 1 ELSE 0 END) AS working_spouse_count,
  SUM(CASE WHEN Marital_Satisfaction = 'High' THEN 1 ELSE 0 END) AS high_satisfaction_count,
  SUM(CASE WHEN Divorce_Status = 'Yes' THEN 1 ELSE 0 END) AS divorce_count,
  AVG(Children_Count) AS avg_children_count,
  SUM(CASE WHEN Inter_Caste = 'Yes' THEN 1 ELSE 0 END) AS inter_caste_count,
  SUM(CASE WHEN Dowry_Exchanged = 'Yes' THEN 1 ELSE 0 END) AS dowry_count
FROM {{ ref('marriage_data_analysis') }}
GROUP BY 
  Gender,
  Education_Level,
  Income_Level