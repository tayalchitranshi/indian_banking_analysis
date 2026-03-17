import duckdb

# Connect to DuckDB (creates file if it doesn't exist)
con = duckdb.connect('data.duckdb')

# Read the Parquet file and create a table
con.execute("""
    CREATE TABLE customers AS 
    SELECT * FROM read_parquet('part-00000-11a5ea31-a538-4940-a136-ae015132082d-c000.snappy.parquet')
""")

# Verify the data was loaded
result = con.execute("SELECT COUNT(*) as row_count FROM customers").fetchone()
print(f"Successfully loaded {result[0]} rows into DuckDB")

# Show table schema
print("\nTable schema:")
con.execute("DESCRIBE customers").show()

# Show sample data
print("\nSample data (first 5 rows):")
con.execute("SELECT * FROM customers LIMIT 5").show()

# Close connection
con.close()

print("\nDuckDB database created: data.duckdb")
