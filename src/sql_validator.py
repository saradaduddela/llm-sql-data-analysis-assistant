def validate_sql(sql):
    """
    Basic validation of LLM-generated SQL.
    """

    sql = sql.strip()

    # Check that the query starts with SELECT
    if not sql.upper().startswith("SELECT"):
        return False, "Query must start with SELECT."

    # Block potentially dangerous SQL commands
    forbidden_keywords = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE"
    ]

    for keyword in forbidden_keywords:
        if keyword in sql.upper():
            return False, f"Forbidden SQL operation detected: {keyword}"

    return True, "SQL validation successful."


# Test
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

is_valid, message = validate_sql(test_sql)

print(message)