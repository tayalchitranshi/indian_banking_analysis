import duckdb

conn = duckdb.connect('indian_banking.duckdb')

# Write your SQL query here
query = """
    SELECT bank_name, COUNT(*) as customer_count
    FROM customers
    GROUP BY bank_name
"""

result = conn.execute(query).fetchdf()
print(result)

conn.close()
