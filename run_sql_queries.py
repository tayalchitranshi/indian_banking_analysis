import duckdb
import pandas as pd

# Connect to the database
conn = duckdb.connect('indian_banking.duckdb')

print("="*80)
print("SQL Query Practice Environment")
print("="*80)

# Example queries to get you started
queries = {
    "1. Total Customers by Bank": """
        SELECT bank_name, COUNT(*) as customer_count
        FROM customers
        GROUP BY bank_name
    """,
    
    "2. Gender Distribution": """
        SELECT gender, COUNT(*) as count, 
               ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
        FROM customers
        GROUP BY gender
    """,
    
    "3. Top 10 Occupations": """
        SELECT occupation, COUNT(*) as customer_count
        FROM customers
        GROUP BY occupation
        ORDER BY customer_count DESC
        LIMIT 10
    """,
    
    "4. Average Balance by Account Type": """
        SELECT account_type, 
               ROUND(AVG(account_balance), 2) as avg_balance,
               COUNT(*) as customer_count
        FROM customers
        GROUP BY account_type
        ORDER BY avg_balance DESC
    """,
    
    "5. High Income Customers (>10 Lakhs)": """
        SELECT title, full_name, occupation, annual_income, bank_name
        FROM customers
        WHERE annual_income > 1000000
        ORDER BY annual_income DESC
        LIMIT 10
    """
}

# Run example queries
for title, query in queries.items():
    print(f"\n{title}")
    print("-" * 80)
    result = conn.execute(query).fetchdf()
    print(result.to_string(index=False))
    print()

print("="*80)
print("Now try your own queries!")
print("="*80)

# Interactive query mode
print("\nEnter your SQL query (or 'exit' to quit):")
print("Example: SELECT * FROM customers WHERE occupation = 'Doctor' LIMIT 5")

while True:
    print("\n" + ">"*3 + " ", end="")
    user_query = input().strip()
    
    if user_query.lower() in ['exit', 'quit', 'q']:
        print("Goodbye!")
        break
    
    if not user_query:
        continue
    
    try:
        result = conn.execute(user_query).fetchdf()
        print("\nResult:")
        print(result.to_string(index=False))
        print(f"\nRows returned: {len(result)}")
    except Exception as e:
        print(f"Error: {e}")

conn.close()
