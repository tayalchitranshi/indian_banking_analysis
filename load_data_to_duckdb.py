import duckdb

# Connect to DuckDB database
conn = duckdb.connect('indian_banking.duckdb')

print("Loading data into DuckDB...")

# Create table from CSV
conn.execute("""
    CREATE OR REPLACE TABLE customers AS 
    SELECT * FROM read_csv_auto('indian_customers_data.csv')
""")

# Verify data loaded
count = conn.execute("SELECT COUNT(*) FROM customers").fetchone()[0]
print(f"✓ Successfully loaded {count:,} customer records!")

# Show table structure
print("\nTable Structure:")
print(conn.execute("DESCRIBE customers").fetchdf())

# Show sample data
print("\nSample Records:")
print(conn.execute("SELECT * FROM customers LIMIT 3").fetchdf())

print("\n" + "="*80)
print("Database ready! You can now run SQL queries.")
print("="*80)

conn.close()
