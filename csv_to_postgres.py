import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv("/Users/nash/Project/dbt-project/marriage_data_india.csv")

# Connect to PostgreSQL
conn = psycopg2.connect("dbname=dbt_test user=postgres password=root host=localhost port=5432")
cur = conn.cursor()

# Insert data into the correct table: public.marriage_data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO india_data.marriage_data (Marriage_Type, Age_at_Marriage, Gender, Education_Level, 
                                          Caste_Match, Religion, Parental_Approval, Urban_Rural, 
                                          Dowry_Exchanged, Marital_Satisfaction, Divorce_Status, 
                                          Children_Count, Income_Level, Years_Since_Marriage, 
                                          Spouse_Working, Inter_Caste, Inter_Religion) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['Marriage_Type'], row['Age_at_Marriage'], row['Gender'], row['Education_Level'],
        row['Caste_Match'], row['Religion'], row['Parental_Approval'], row['Urban_Rural'],
        row['Dowry_Exchanged'], row['Marital_Satisfaction'], row['Divorce_Status'],
        row['Children_Count'], row['Income_Level'], row['Years_Since_Marriage'],
        row['Spouse_Working'], row['Inter-Caste'], row['Inter-Religion']
    ))

# Commit and close connection
conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")
