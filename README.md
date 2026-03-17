# Indian Banking Customer Analysis

Analyzed 100K customer records from State Bank of India and Central Bank of India using three different approaches — SQL, Python, and Power BI. The idea was to explore the same dataset from different angles and show how each tool brings something different to the table.

## Dataset

`customers_100k.csv` — 100,000 rows with 24 columns including customer details, bank info, account balance, credit score, income, occupation, transaction history, etc.

## Three Approaches

### 1. SQL Analysis (`customer_analysis.ipynb`)
Used DuckDB to write raw SQL queries. Covers demographics, balance segmentation, transaction patterns, credit scores, income breakdown, risk assessment, and bank-level comparisons. Good for quick data exploration and getting exact numbers.

### 2. Python Analysis (`python_analysis.ipynb`)
Same analysis but using pandas, matplotlib, and seaborn. Added visualizations like heatmaps, scatter plots, histograms, and correlation matrices. The charts make patterns easier to spot — especially the risk concentration in the balance vs credit heatmap.

### 3. Power BI Dashboard
Interactive dashboard with filters and drill-downs. Useful for non-technical stakeholders who want to explore the data themselves without writing code. *(Dashboard file in the repo)*

## Some key findings

- 84% of customers have balance above 2 lakhs
- ~41% have poor credit scores (below 550), which is a big risk area
- Around 15K accounts haven't had a transaction in over a year
- Business owners earn the most on average (~52L/year)
- Both banks have very similar customer profiles across most metrics
- No real correlation between account balance and transaction frequency

## How to run

```
pip install duckdb pandas matplotlib seaborn jupyter
```

For SQL analysis:
```python
import duckdb
conn = duckdb.connect('indian_banking.duckdb')
conn.execute("CREATE TABLE customers AS SELECT * FROM read_csv_auto('customers_100k.csv')")
```

Then open either notebook:
```
jupyter notebook customer_analysis.ipynb
jupyter notebook python_analysis.ipynb
```

## Built with

SQL (DuckDB) | Python (Pandas, Matplotlib, Seaborn) | Power BI | Jupyter Notebook
