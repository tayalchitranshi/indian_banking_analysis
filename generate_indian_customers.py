import random
import string
from datetime import datetime, timedelta

# Indian first names
first_names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Arnav", "Ayaan", "Krishna", "Ishaan",
    "Shaurya", "Atharv", "Advik", "Pranav", "Reyansh", "Aadhya", "Ananya", "Pari", "Anika", "Ira",
    "Diya", "Navya", "Saanvi", "Myra", "Sara", "Priya", "Kavya", "Riya", "Anvi", "Kiara",
    "Rajesh", "Suresh", "Ramesh", "Mahesh", "Dinesh", "Amit", "Rohit", "Vikas", "Ajay", "Vijay",
    "Sunita", "Geeta", "Meera", "Pooja", "Neha", "Sneha", "Anjali", "Preeti", "Kavita", "Rekha",
    "Aryan", "Kabir", "Rohan", "Karan", "Varun", "Nikhil", "Rahul", "Siddharth", "Harsh", "Yash",
    "Shreya", "Tanvi", "Ishita", "Nisha", "Simran", "Tanya", "Divya", "Sakshi", "Kritika", "Megha"
]

last_names = [
    "Sharma", "Verma", "Patel", "Kumar", "Singh", "Gupta", "Reddy", "Rao", "Nair", "Iyer",
    "Joshi", "Desai", "Mehta", "Shah", "Agarwal", "Bansal", "Malhotra", "Kapoor", "Chopra", "Bhatia",
    "Pandey", "Mishra", "Tiwari", "Dubey", "Jain", "Saxena", "Sinha", "Yadav", "Chauhan", "Rajput",
    "Pillai", "Menon", "Krishnan", "Naidu", "Chowdhury", "Das", "Bose", "Ghosh", "Mukherjee", "Sen"
]

# Bank details
banks = [
    {"bank_id": "SBI001", "bank_name": "State Bank of India"},
    {"bank_id": "CBI001", "bank_name": "Central Bank of India"}
]

def generate_account_number():
    """Generate a random 12-digit account number"""
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

def generate_customer_id():
    """Generate a customer ID in format CUST followed by 8 digits"""
    return f"CUST{random.randint(10000000, 99999999)}"

def generate_email(first_name, last_name):
    """Generate email address"""
    domains = ["gmail.com", "yahoo.com", "outlook.com", "rediffmail.com", "hotmail.com"]
    return f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 999)}@{random.choice(domains)}"

def generate_phone():
    """Generate Indian phone number"""
    return f"+91{random.randint(7000000000, 9999999999)}"

def generate_date_of_birth():
    """Generate date of birth between 1960 and 2005"""
    start_date = datetime(1960, 1, 1)
    end_date = datetime(2005, 12, 31)
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

def generate_address():
    """Generate Indian address"""
    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"]
    states = ["Maharashtra", "Delhi", "Karnataka", "Telangana", "Tamil Nadu", "West Bengal", "Maharashtra", "Gujarat", "Rajasthan", "Uttar Pradesh"]
    street_num = random.randint(1, 999)
    sector = random.randint(1, 50)
    city_idx = random.randint(0, len(cities) - 1)
    pincode = random.randint(100000, 999999)
    return f"{street_num}, Sector {sector}, {cities[city_idx]}, {states[city_idx]} - {pincode}"

def generate_customers(num_records=100000):
    """Generate customer records"""
    print(f"Generating {num_records} customer records...")
    
    customers = []
    used_customer_ids = set()
    used_account_numbers = set()
    
    for i in range(num_records):
        if (i + 1) % 10000 == 0:
            print(f"Generated {i + 1} records...")
        
        # Generate unique customer ID
        while True:
            customer_id = generate_customer_id()
            if customer_id not in used_customer_ids:
                used_customer_ids.add(customer_id)
                break
        
        # Generate unique account number
        while True:
            account_number = generate_account_number()
            if account_number not in used_account_numbers:
                used_account_numbers.add(account_number)
                break
        
        # Random bank
        bank = random.choice(banks)
        
        # Random name
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"
        
        customer = {
            "customer_id": customer_id,
            "bank_id": bank["bank_id"],
            "bank_name": bank["bank_name"],
            "account_number": account_number,
            "full_name": full_name,
            "email": generate_email(first_name, last_name),
            "phone": generate_phone(),
            "date_of_birth": generate_date_of_birth(),
            "address": generate_address(),
            "account_balance": round(random.uniform(1000, 5000000), 2),
            "account_type": random.choice(["Savings", "Current", "Salary"]),
            "account_status": random.choice(["Active", "Active", "Active", "Inactive"]),  # 75% active
            "created_date": (datetime.now() - timedelta(days=random.randint(1, 3650))).strftime('%Y-%m-%d')
        }
        
        customers.append(customer)
    
    return customers

if __name__ == "__main__":
    # Generate 1 lakh (100,000) records
    customers = generate_customers(100000)
    
    # Save to CSV
    import csv
    
    output_file = "indian_customers_data.csv"
    print(f"\nSaving to {output_file}...")
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        if customers:
            writer = csv.DictWriter(f, fieldnames=customers[0].keys())
            writer.writeheader()
            writer.writerows(customers)
    
    print(f"Successfully created {output_file} with {len(customers)} records!")
    print(f"\nSample record:")
    print(customers[0])
