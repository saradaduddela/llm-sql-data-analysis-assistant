import sqlite3

DB_PATH = "data/sales_database.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

query = """
SELECT
    p.product_name,
    SUM(o.quantity * p.unit_price) AS revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 5;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\nTop 5 Products by Revenue")
print("--------------------------")

for product, revenue in results:
    print(f"{product}: ₹{revenue:,.2f}")

conn.close()