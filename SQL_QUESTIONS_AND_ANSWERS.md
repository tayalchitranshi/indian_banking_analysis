# SQL Questions and Answers - Indian Banking Dataset

## Database: indian_banking.duckdb
## Table: customers (100,000 records)

---

## 📘 BASIC LEVEL QUESTIONS (1-15)

### Question 1: How many total customers are in the database?
**Difficulty:** ⭐

**Query:**
```sql
SELECT COUNT(*) as total_customers
FROM customers;
```

**Expected Output:** 100,000 customers

---

### Question 2: List all unique bank names in the database.
**Difficulty:** ⭐

**Query:**
```sql
SELECT DISTINCT bank_name
FROM customers;
```

**Expected Output:** State Bank of India, Central Bank of India

---

### Question 3: How many customers does each bank have?
**Difficulty:** ⭐

**Query:**
```sql
SELECT bank_name, COUNT(*) as customer_count
FROM customers
GROUP BY bank_name;
```

---

### Question 4: What are the different account types available?
**Difficulty:** ⭐

**Query:**
```sql
SELECT DISTINCT account_type, COUNT(*) as count
FROM customers
GROUP BY account_type
ORDER BY count DESC;
```

---

### Question 5: How many male and female customers are there?
**Difficulty:** ⭐

**Query:**
```sql
SELECT gender, COUNT(*) as count
FROM customers
GROUP BY gender;
```

---

### Question 6: List the first 10 customers with their names and email addresses.
**Difficulty:** ⭐

**Query:**
```sql
SELECT customer_id, full_name, email, phone
FROM customers
LIMIT 10;
```

---

### Question 7: How many customers have an Active account status?
**Difficulty:** ⭐

**Query:**
```sql
SELECT account_status, COUNT(*) as count
FROM customers
GROUP BY account_status;
```

---

### Question 8: Find all customers who are Doctors.
**Difficulty:** ⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation, annual_income
FROM customers
WHERE occupation = 'Doctor'
LIMIT 20;
```

---

### Question 9: What is the highest account balance in the database?
**Difficulty:** ⭐

**Query:**
```sql
SELECT MAX(account_balance) as highest_balance
FROM customers;
```

---

### Question 10: List all unique occupations in alphabetical order.
**Difficulty:** ⭐

**Query:**
```sql
SELECT DISTINCT occupation
FROM customers
ORDER BY occupation;
```

---

### Question 11: How many customers have a Savings account?
**Difficulty:** ⭐

**Query:**
```sql
SELECT COUNT(*) as savings_customers
FROM customers
WHERE account_type = 'Savings';
```

---

### Question 12: Find customers with account balance greater than 10 lakhs.
**Difficulty:** ⭐

**Query:**
```sql
SELECT full_name, account_balance, occupation
FROM customers
WHERE account_balance > 1000000
ORDER BY account_balance DESC
LIMIT 10;
```

---

### Question 13: What are the different primary sources of funds?
**Difficulty:** ⭐

**Query:**
```sql
SELECT DISTINCT primary_source_of_funds, COUNT(*) as count
FROM customers
GROUP BY primary_source_of_funds
ORDER BY count DESC;
```

---

### Question 14: List customers from State Bank of India only.
**Difficulty:** ⭐

**Query:**
```sql
SELECT customer_id, full_name, bank_name
FROM customers
WHERE bank_name = 'State Bank of India'
LIMIT 10;
```

---

### Question 15: What is the average account balance across all customers?
**Difficulty:** ⭐

**Query:**
```sql
SELECT ROUND(AVG(account_balance), 2) as avg_balance
FROM customers;
```

---

## 📗 INTERMEDIATE LEVEL QUESTIONS (16-40)

### Question 16: What is the average annual income by gender?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT gender, 
       ROUND(AVG(annual_income), 2) as avg_income,
       COUNT(*) as customer_count
FROM customers
GROUP BY gender;
```

---

### Question 17: Find the top 10 highest-paid occupations by average income.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT occupation, 
       ROUND(AVG(annual_income), 2) as avg_income,
       COUNT(*) as count
FROM customers
GROUP BY occupation
ORDER BY avg_income DESC
LIMIT 10;
```

---

### Question 18: What is the average account balance for each account type?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT account_type,
       COUNT(*) as customers,
       ROUND(AVG(account_balance), 2) as avg_balance,
       ROUND(MIN(account_balance), 2) as min_balance,
       ROUND(MAX(account_balance), 2) as max_balance
FROM customers
GROUP BY account_type;
```

---

### Question 19: How many customers are there in each occupation category?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT occupation, COUNT(*) as customer_count
FROM customers
GROUP BY occupation
ORDER BY customer_count DESC;
```

---

### Question 20: Find customers with credit score above 800.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, credit_score, occupation, annual_income
FROM customers
WHERE credit_score > 800
ORDER BY credit_score DESC;
```

---

### Question 21: What is the total deposit amount in each bank?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT bank_name, 
       COUNT(*) as customers,
       ROUND(SUM(account_balance), 2) as total_deposits
FROM customers
GROUP BY bank_name;
```

---

### Question 22: Find all customers who are Students or Retired.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT full_name, occupation, annual_income, account_balance
FROM customers
WHERE occupation IN ('Student', 'Retired')
ORDER BY occupation, annual_income DESC;
```

---

### Question 23: What percentage of customers have Active vs Inactive accounts?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT account_status,
       COUNT(*) as count,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
FROM customers
GROUP BY account_status;
```

---

### Question 24: Find the average credit score by account type.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT account_type,
       ROUND(AVG(credit_score), 2) as avg_credit_score,
       COUNT(*) as customers
FROM customers
GROUP BY account_type
ORDER BY avg_credit_score DESC;
```

---

### Question 25: List customers with annual income between 5 lakhs and 10 lakhs.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT full_name, occupation, annual_income, bank_name
FROM customers
WHERE annual_income BETWEEN 500000 AND 1000000
ORDER BY annual_income DESC
LIMIT 20;
```

---

### Question 26: How many customers have each title (Mr., Mrs., Ms., Dr., Er.)?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT title, COUNT(*) as count
FROM customers
GROUP BY title
ORDER BY count DESC;
```

---

### Question 27: Find customers whose primary source of funds is Business Income.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT full_name, occupation, annual_income, primary_source_of_funds
FROM customers
WHERE primary_source_of_funds = 'Business Income'
ORDER BY annual_income DESC
LIMIT 15;
```

---

### Question 28: What is the average number of transactions per month by account type?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT account_type,
       ROUND(AVG(transactions_per_month), 2) as avg_transactions,
       COUNT(*) as customers
FROM customers
GROUP BY account_type;
```

---

### Question 29: Find customers with zero annual income.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT full_name, occupation, primary_source_of_funds, account_balance
FROM customers
WHERE annual_income = 0
LIMIT 20;
```

---

### Question 30: What is the average account balance by gender and account type?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT gender, account_type,
       COUNT(*) as customers,
       ROUND(AVG(account_balance), 2) as avg_balance
FROM customers
GROUP BY gender, account_type
ORDER BY gender, avg_balance DESC;
```

---

### Question 31: Find the youngest and oldest customers in the database.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT 'Youngest' as category, full_name, date_of_birth, occupation
FROM customers
ORDER BY date_of_birth DESC
LIMIT 1

UNION ALL

SELECT 'Oldest' as category, full_name, date_of_birth, occupation
FROM customers
ORDER BY date_of_birth ASC
LIMIT 1;
```

---

### Question 32: How many customers have a middle name?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT 
    COUNT(CASE WHEN middle_name != '' THEN 1 END) as with_middle_name,
    COUNT(CASE WHEN middle_name = '' THEN 1 END) as without_middle_name
FROM customers;
```

---

### Question 33: Find customers with account balance less than their annual income.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT full_name, occupation, annual_income, account_balance
FROM customers
WHERE account_balance < annual_income
ORDER BY annual_income DESC
LIMIT 20;
```

---

### Question 34: What is the distribution of customers by primary source of funds?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT primary_source_of_funds,
       COUNT(*) as count,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
FROM customers
GROUP BY primary_source_of_funds
ORDER BY count DESC;
```

---

### Question 35: Find all Software Engineers with their average income.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT COUNT(*) as total_engineers,
       ROUND(AVG(annual_income), 2) as avg_income,
       ROUND(AVG(account_balance), 2) as avg_balance,
       ROUND(AVG(credit_score), 2) as avg_credit_score
FROM customers
WHERE occupation = 'Software Engineer';
```

---

### Question 36: List customers who had transactions in the last 30 days.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT full_name, last_transaction_date, account_status, transactions_per_month
FROM customers
WHERE last_transaction_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
ORDER BY last_transaction_date DESC
LIMIT 20;
```

---

### Question 37: Find the total number of customers by account creation year.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT YEAR(created_date) as year,
       COUNT(*) as customers_joined
FROM customers
GROUP BY year
ORDER BY year DESC;
```

---

### Question 38: What is the average credit score by income bracket?
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT 
    CASE 
        WHEN annual_income < 300000 THEN 'Below 3 Lakhs'
        WHEN annual_income BETWEEN 300000 AND 1000000 THEN '3-10 Lakhs'
        WHEN annual_income > 1000000 THEN 'Above 10 Lakhs'
    END as income_bracket,
    COUNT(*) as customers,
    ROUND(AVG(credit_score), 2) as avg_credit_score
FROM customers
GROUP BY income_bracket
ORDER BY avg_credit_score DESC;
```

---

### Question 39: Find customers with more than 100 transactions per month.
**Difficulty:** ⭐⭐

**Query:**
```sql
SELECT full_name, occupation, transactions_per_month, account_type
FROM customers
WHERE transactions_per_month > 100
ORDER BY transactions_per_month DESC
LIMIT 20;
```

---

### Question 40: What is the gender distribution within each occupation (top 10 occupations)?
**Difficulty:** ⭐⭐

**Query:**
```sql
WITH top_occupations AS (
    SELECT occupation
    FROM customers
    GROUP BY occupation
    ORDER BY COUNT(*) DESC
    LIMIT 10
)
SELECT o.occupation, c.gender, COUNT(*) as count
FROM customers c
JOIN top_occupations o ON c.occupation = o.occupation
GROUP BY o.occupation, c.gender
ORDER BY o.occupation, count DESC;
```

---

## 📕 ADVANCED LEVEL QUESTIONS (41-60)

### Question 41: Find customers whose account balance is more than 3 times their annual income.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation,
       annual_income, account_balance,
       ROUND(account_balance / NULLIF(annual_income, 0), 2) as balance_to_income_ratio
FROM customers
WHERE account_balance > (annual_income * 3)
ORDER BY balance_to_income_ratio DESC
LIMIT 20;
```

---

### Question 42: Calculate the customer lifetime value (CLV) for top 50 customers.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation,
       account_balance,
       annual_income,
       DATEDIFF(CURRENT_DATE, created_date) as account_age_days,
       ROUND(account_balance + (annual_income * DATEDIFF(CURRENT_DATE, created_date) / 365.0), 2) as estimated_clv
FROM customers
WHERE account_status = 'Active'
ORDER BY estimated_clv DESC
LIMIT 50;
```

---

### Question 43: Find the income gap between male and female customers by occupation.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT occupation,
       COUNT(*) as total_customers,
       ROUND(AVG(CASE WHEN gender = 'Male' THEN annual_income END), 2) as male_avg_income,
       ROUND(AVG(CASE WHEN gender = 'Female' THEN annual_income END), 2) as female_avg_income,
       ROUND(AVG(CASE WHEN gender = 'Male' THEN annual_income END) - 
             AVG(CASE WHEN gender = 'Female' THEN annual_income END), 2) as income_gap
FROM customers
GROUP BY occupation
HAVING COUNT(CASE WHEN gender = 'Male' THEN 1 END) > 50 
   AND COUNT(CASE WHEN gender = 'Female' THEN 1 END) > 50
ORDER BY ABS(income_gap) DESC
LIMIT 15;
```

---

### Question 44: Identify high-risk customers (low credit score but high balance).
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation,
       credit_score, account_balance, annual_income,
       primary_source_of_funds,
       CASE 
           WHEN credit_score < 400 THEN 'Very High Risk'
           WHEN credit_score BETWEEN 400 AND 500 THEN 'High Risk'
           ELSE 'Moderate Risk'
       END as risk_level
FROM customers
WHERE credit_score < 500 AND account_balance > 500000
ORDER BY account_balance DESC, credit_score ASC
LIMIT 30;
```

---

### Question 45: Find customers who are potential candidates for account upgrade (Savings to Current).
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation,
       account_type, account_balance, transactions_per_month,
       annual_income
FROM customers
WHERE account_type = 'Savings'
  AND (account_balance > 1000000 OR transactions_per_month > 80)
  AND account_status = 'Active'
ORDER BY account_balance DESC, transactions_per_month DESC
LIMIT 50;
```

---

### Question 46: Calculate the average account balance by age group and gender.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT 
    CASE 
        WHEN YEAR(CURRENT_DATE) - YEAR(date_of_birth) < 25 THEN 'Under 25'
        WHEN YEAR(CURRENT_DATE) - YEAR(date_of_birth) BETWEEN 25 AND 35 THEN '25-35'
        WHEN YEAR(CURRENT_DATE) - YEAR(date_of_birth) BETWEEN 36 AND 50 THEN '36-50'
        WHEN YEAR(CURRENT_DATE) - YEAR(date_of_birth) BETWEEN 51 AND 65 THEN '51-65'
        ELSE 'Above 65'
    END as age_group,
    gender,
    COUNT(*) as customers,
    ROUND(AVG(account_balance), 2) as avg_balance,
    ROUND(AVG(annual_income), 2) as avg_income
FROM customers
GROUP BY age_group, gender
ORDER BY age_group, gender;
```

---

### Question 47: Find inactive accounts with high balances for recovery campaigns.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, phone, email,
       account_balance, last_transaction_date,
       DATEDIFF(CURRENT_DATE, last_transaction_date) as days_inactive,
       occupation, annual_income
FROM customers
WHERE account_status = 'Inactive'
  AND account_balance > 100000
  AND DATEDIFF(CURRENT_DATE, last_transaction_date) > 90
ORDER BY account_balance DESC
LIMIT 100;
```

---

### Question 48: Compare bank performance across multiple metrics.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT bank_name,
       COUNT(*) as total_customers,
       ROUND(AVG(account_balance), 2) as avg_balance,
       ROUND(SUM(account_balance), 2) as total_deposits,
       ROUND(AVG(annual_income), 2) as avg_customer_income,
       ROUND(AVG(credit_score), 2) as avg_credit_score,
       ROUND(COUNT(CASE WHEN account_status = 'Active' THEN 1 END) * 100.0 / COUNT(*), 2) as active_percentage,
       ROUND(AVG(transactions_per_month), 2) as avg_monthly_transactions
FROM customers
GROUP BY bank_name;
```

---

### Question 49: Identify customers with unusual balance-to-income ratios.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
WITH balance_ratios AS (
    SELECT customer_id, full_name, occupation,
           annual_income, account_balance,
           CASE 
               WHEN annual_income > 0 THEN account_balance / annual_income
               ELSE NULL
           END as balance_ratio
    FROM customers
    WHERE annual_income > 0
)
SELECT customer_id, full_name, occupation,
       annual_income, account_balance,
       ROUND(balance_ratio, 2) as balance_to_income_ratio
FROM balance_ratios
WHERE balance_ratio > 5 OR balance_ratio < 0.1
ORDER BY balance_ratio DESC
LIMIT 30;
```

---

### Question 50: Find the most profitable customer segments.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT occupation,
       COUNT(*) as customer_count,
       ROUND(AVG(account_balance), 2) as avg_balance,
       ROUND(SUM(account_balance), 2) as total_balance,
       ROUND(AVG(transactions_per_month), 2) as avg_transactions,
       ROUND(AVG(annual_income), 2) as avg_income
FROM customers
WHERE account_status = 'Active'
GROUP BY occupation
HAVING customer_count > 100
ORDER BY total_balance DESC
LIMIT 15;
```

---

### Question 51: Analyze transaction activity patterns by account type and status.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT account_type, account_status,
       COUNT(*) as customers,
       ROUND(AVG(transactions_per_month), 2) as avg_transactions,
       ROUND(MIN(transactions_per_month), 2) as min_transactions,
       ROUND(MAX(transactions_per_month), 2) as max_transactions,
       ROUND(AVG(account_balance), 2) as avg_balance
FROM customers
GROUP BY account_type, account_status
ORDER BY account_type, account_status;
```

---

### Question 52: Find customers who might be good candidates for premium banking services.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation,
       annual_income, account_balance, credit_score,
       transactions_per_month, account_type
FROM customers
WHERE annual_income > 2000000
  AND account_balance > 2000000
  AND credit_score > 700
  AND account_status = 'Active'
ORDER BY (annual_income + account_balance) DESC
LIMIT 50;
```

---

### Question 53: Calculate customer retention rate by account creation year.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT YEAR(created_date) as year,
       COUNT(*) as total_accounts,
       COUNT(CASE WHEN account_status = 'Active' THEN 1 END) as active_accounts,
       ROUND(COUNT(CASE WHEN account_status = 'Active' THEN 1 END) * 100.0 / COUNT(*), 2) as retention_rate
FROM customers
GROUP BY year
ORDER BY year DESC;
```

---

### Question 54: Find occupation pairs where income differs significantly.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
WITH occupation_income AS (
    SELECT occupation, AVG(annual_income) as avg_income
    FROM customers
    GROUP BY occupation
    HAVING COUNT(*) > 100
)
SELECT o1.occupation as occupation_1,
       ROUND(o1.avg_income, 2) as income_1,
       o2.occupation as occupation_2,
       ROUND(o2.avg_income, 2) as income_2,
       ROUND(ABS(o1.avg_income - o2.avg_income), 2) as income_difference
FROM occupation_income o1
CROSS JOIN occupation_income o2
WHERE o1.occupation < o2.occupation
ORDER BY income_difference DESC
LIMIT 10;
```

---

### Question 55: Identify customers with declining transaction activity.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation,
       transactions_per_month,
       last_transaction_date,
       DATEDIFF(CURRENT_DATE, last_transaction_date) as days_since_last_transaction,
       account_balance
FROM customers
WHERE account_status = 'Active'
  AND transactions_per_month < 20
  AND DATEDIFF(CURRENT_DATE, last_transaction_date) > 30
ORDER BY account_balance DESC
LIMIT 50;
```

---

### Question 56: Calculate the distribution of wealth across different demographics.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT 
    CASE 
        WHEN account_balance < 100000 THEN 'Low (<1L)'
        WHEN account_balance BETWEEN 100000 AND 500000 THEN 'Medium (1-5L)'
        WHEN account_balance BETWEEN 500001 AND 2000000 THEN 'High (5-20L)'
        ELSE 'Very High (>20L)'
    END as wealth_category,
    gender,
    COUNT(*) as customers,
    ROUND(AVG(annual_income), 2) as avg_income,
    ROUND(AVG(credit_score), 2) as avg_credit_score
FROM customers
GROUP BY wealth_category, gender
ORDER BY wealth_category, gender;
```

---

### Question 57: Find customers with mismatched occupation and income levels.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
WITH occupation_avg AS (
    SELECT occupation, AVG(annual_income) as avg_occupation_income
    FROM customers
    GROUP BY occupation
)
SELECT c.customer_id, c.full_name, c.occupation,
       c.annual_income,
       ROUND(oa.avg_occupation_income, 2) as expected_income,
       ROUND(c.annual_income - oa.avg_occupation_income, 2) as income_deviation
FROM customers c
JOIN occupation_avg oa ON c.occupation = oa.occupation
WHERE ABS(c.annual_income - oa.avg_occupation_income) > 500000
ORDER BY ABS(income_deviation) DESC
LIMIT 30;
```

---

### Question 58: Analyze credit score distribution by primary source of funds.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT primary_source_of_funds,
       COUNT(*) as customers,
       ROUND(AVG(credit_score), 2) as avg_credit_score,
       ROUND(MIN(credit_score), 2) as min_credit_score,
       ROUND(MAX(credit_score), 2) as max_credit_score,
       COUNT(CASE WHEN credit_score < 500 THEN 1 END) as poor_credit_count,
       COUNT(CASE WHEN credit_score >= 750 THEN 1 END) as excellent_credit_count
FROM customers
GROUP BY primary_source_of_funds
ORDER BY avg_credit_score DESC;
```

---

### Question 59: Find the top 20 customers by total banking value (balance + annual income).
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation, gender,
       account_balance, annual_income, credit_score,
       (account_balance + annual_income) as total_value,
       bank_name
FROM customers
ORDER BY total_value DESC
LIMIT 20;
```

---

### Question 60: Create a customer segmentation based on RFM-like analysis.
**Difficulty:** ⭐⭐⭐

**Query:**
```sql
SELECT 
    CASE 
        WHEN DATEDIFF(CURRENT_DATE, last_transaction_date) <= 30 THEN 'Recent'
        WHEN DATEDIFF(CURRENT_DATE, last_transaction_date) <= 90 THEN 'Moderate'
        ELSE 'Dormant'
    END as recency,
    CASE 
        WHEN transactions_per_month >= 80 THEN 'High Frequency'
        WHEN transactions_per_month >= 40 THEN 'Medium Frequency'
        ELSE 'Low Frequency'
    END as frequency,
    CASE 
        WHEN account_balance >= 1000000 THEN 'High Value'
        WHEN account_balance >= 300000 THEN 'Medium Value'
        ELSE 'Low Value'
    END as monetary,
    COUNT(*) as customer_count,
    ROUND(AVG(account_balance), 2) as avg_balance
FROM customers
WHERE account_status = 'Active'
GROUP BY recency, frequency, monetary
ORDER BY customer_count DESC;
```

---

## 🎯 BONUS CHALLENGE QUESTIONS

### Bonus 1: Find customers who are outliers in their occupation group.
**Difficulty:** ⭐⭐⭐⭐

**Query:**
```sql
WITH occupation_stats AS (
    SELECT occupation,
           AVG(annual_income) as avg_income,
           STDDEV(annual_income) as stddev_income
    FROM customers
    GROUP BY occupation
    HAVING COUNT(*) > 50
)
SELECT c.customer_id, c.full_name, c.occupation,
       c.annual_income,
       ROUND(os.avg_income, 2) as occupation_avg,
       ROUND((c.annual_income - os.avg_income) / NULLIF(os.stddev_income, 0), 2) as z_score
FROM customers c
JOIN occupation_stats os ON c.occupation = os.occupation
WHERE ABS((c.annual_income - os.avg_income) / NULLIF(os.stddev_income, 0)) > 2
ORDER BY ABS(z_score) DESC
LIMIT 30;
```

---

### Bonus 2: Calculate customer churn probability score.
**Difficulty:** ⭐⭐⭐⭐

**Query:**
```sql
SELECT customer_id, full_name, occupation,
       account_balance, transactions_per_month,
       DATEDIFF(CURRENT_DATE, last_transaction_date) as days_inactive,
       credit_score,
       CASE 
           WHEN account_status = 'Inactive' THEN 100
           WHEN DATEDIFF(CURRENT_DATE, last_transaction_date) > 180 THEN 90
           WHEN DATEDIFF(CURRENT_DATE, last_transaction_date) > 90 THEN 70
           WHEN transactions_per_month < 10 THEN 50
           WHEN credit_score < 400 THEN 40
           ELSE 10
       END as churn_risk_score
FROM customers
ORDER BY churn_risk_score DESC, account_balance DESC
LIMIT 100;
```

---

## 📊 Summary Statistics

**Total Questions:** 62
- Basic: 15 questions (⭐)
- Intermediate: 25 questions (⭐⭐)
- Advanced: 20 questions (⭐⭐⭐)
- Bonus Challenge: 2 questions (⭐⭐⭐⭐)

**Topics Covered:**
- Basic SELECT, WHERE, GROUP BY
- Aggregations (COUNT, AVG, SUM, MIN, MAX)
- JOINs and Subqueries
- CASE statements and conditional logic
- Window functions
- CTEs (Common Table Expressions)
- Date functions
- Statistical analysis
- Customer segmentation
- Risk assessment
- Business intelligence queries

---

**Happy Learning! 🚀**
