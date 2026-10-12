import sqlite3


DB_PATH = "data/sales_database.db"


def execute_sql(sql):
    """
    Execute validated SQL against the SQLite database.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    try:
        cursor.execute(sql)

        results = cursor.fetchall()

        return results

    except sqlite3.Error as error:

        print("SQL execution error:", error)

        return None

    finally:

        conn.close()


# Test query

test_sql = """
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


results = execute_sql(test_sql)

print("\nQuery Results")
print("-------------")

for row in results:
    print(row)