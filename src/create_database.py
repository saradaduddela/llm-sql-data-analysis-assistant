import sqlite3
import random
from datetime import datetime, timedelta

DB_PATH = "data/sales_database.db"

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# -------------------------
# Create Customers table
# -------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    region TEXT,
    city TEXT,
    customer_segment TEXT
)
""")

# -------------------------
# Create Products table
# -------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    unit_price REAL
)
""")

# -------------------------
# Create Orders table
# -------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    order_date DATE,
    quantity INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
""")

# -------------------------
# Insert Customers
# -------------------------

regions = ["North", "South", "East", "West"]

cities = [
    "Delhi",
    "Hyderabad",
    "Kolkata",
    "Mumbai",
    "Bangalore",
    "Chennai"
]

segments = [
    "Consumer",
    "Corporate",
    "Small Business"
]

for i in range(1, 101):

    cursor.execute("""
        INSERT INTO customers
        VALUES (?, ?, ?, ?, ?)
    """, (
        i,
        f"Customer {i}",
        random.choice(regions),
        random.choice(cities),
        random.choice(segments)
    ))

# -------------------------
# Insert Products
# -------------------------

products = [
    (1, "Laptop", "Electronics", 60000),
    (2, "Smartphone", "Electronics", 30000),
    (3, "Tablet", "Electronics", 20000),
    (4, "Headphones", "Accessories", 3000),
    (5, "Keyboard", "Accessories", 1500),
    (6, "Office Chair", "Furniture", 12000),
    (7, "Desk", "Furniture", 18000),
    (8, "Monitor", "Electronics", 15000),
    (9, "Mouse", "Accessories", 1000),
    (10, "Printer", "Office Equipment", 10000)
]

cursor.executemany("""
    INSERT INTO products
    VALUES (?, ?, ?, ?)
""", products)

# -------------------------
# Insert Orders
# -------------------------

start_date = datetime(2024, 1, 1)

for order_id in range(1, 10001):

    customer_id = random.randint(1, 100)
    product_id = random.randint(1, 10)

    random_days = random.randint(0, 730)

    order_date = start_date + timedelta(days=random_days)

    quantity = random.randint(1, 5)

    cursor.execute("""
        INSERT INTO orders
        VALUES (?, ?, ?, ?, ?)
    """, (
        order_id,
        customer_id,
        product_id,
        order_date.strftime("%Y-%m-%d"),
        quantity
    ))

# Save changes
conn.commit()

# Close database
conn.close()

print("Database created successfully!")