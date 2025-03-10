-- models/marriage_stats.sql


SELECT 
  Religion,
  Urban_Rural,
  Marriage_Type,
  Years_Since_Marriage,
  COUNT(*) AS marriages_count,
  AVG(Age_at_Marriage) AS avg_age_at_marriage,
  SUM(CASE WHEN Dowry_Exchanged = 'Yes' THEN 1 ELSE 0 END) AS dowry_count,
  SUM(CASE WHEN Divorce_Status = 'Yes' THEN 1 ELSE 0 END) AS divorce_count,
  AVG(Children_Count) AS avg_children,
  SUM(CASE WHEN Marital_Satisfaction = 'High' THEN 1 ELSE 0 END) AS high_satisfaction_count,
  SUM(CASE WHEN Caste_Match = 'Yes' THEN 1 ELSE 0 END) AS caste_match_count,
  SUM(CASE WHEN Inter_Caste = 'Yes' THEN 1 ELSE 0 END) AS inter_caste_count,
  SUM(CASE WHEN Inter_Religion = 'Yes' THEN 1 ELSE 0 END) AS inter_religion_count
FROM "dbt_test"."india_data"."marriage_data_analysis"
GROUP BY 
  Religion,
  Urban_Rural,
  Marriage_Type,
  Years_Since_Marriage