import psycopg2

# Database connection details
DB_NAME = "dbt_test"  # Ensure this is correct
DB_USER = "postgres"  # Replace with your PostgreSQL username
DB_PASSWORD = "root"  # Replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

SCHEMA_NAME = "india_data"  # Name of the schema

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    print("Connected to the database successfully!")

    # Step 1: Create the schema if it doesn't exist
    create_schema_query = f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME};"
    cur.execute(create_schema_query)
    conn.commit()
    print(f"Schema '{SCHEMA_NAME}' has been created successfully!")

    # Step 2: Create the table inside the new schema
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.marriage_data (
        ID SERIAL PRIMARY KEY,
        Marriage_Type TEXT,
        Age_at_Marriage INT,
        Gender TEXT,
        Education_Level TEXT,
        Caste_Match TEXT,
        Religion TEXT,
        Parental_Approval TEXT,
        Urban_Rural TEXT,
        Dowry_Exchanged TEXT,
        Marital_Satisfaction TEXT,
        Divorce_Status TEXT,
        Children_Count INT,
        Income_Level TEXT,
        Years_Since_Marriage INT,
        Spouse_Working TEXT,
        Inter_Caste TEXT,
        Inter_Religion TEXT
    );
    """
    
    # Execute the query
    cur.execute(create_table_query)
    conn.commit()

    print(f"Table 'marriage_data' has been created inside schema '{SCHEMA_NAME}' successfully!")

    # Close connection
    cur.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")
