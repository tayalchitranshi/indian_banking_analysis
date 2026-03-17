import duckdb

conn = duckdb.connect('indian_banking.duckdb')

print("="*80)
print("SQL Query Examples - Indian Banking Data")
print("="*80)

queries = {
    "1. Total Customers by Bank": """
        SELECT bank_name, COUNT(*) as customer_count
        FROM customers
        GROUP BY bank_name
    """,
    
    "2. Top 5 Occupations": """
        SELECT occupation, COUNT(*) as count
        FROM customers
        GROUP BY occupation
        ORDER BY count DESC
        LIMIT 5
    """,
    
    "3. Average Income by Gender": """
        SELECT gender, 
               ROUND(AVG(annual_income), 2) as avg_income,
               COUNT(*) as count
        FROM customers
        GROUP BY gender
    """
}

for title, query in queries.items():
    print(f"\n{title}")
    print("-" * 80)
    result = conn.execute(query).fetchdf()
    print(result.to_string(index=False))

conn.close()
