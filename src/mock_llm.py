def generate_sql(user_question):
    """
    Simulates an LLM generating SQL from a business question.
    """

    question = user_question.lower()

    # Question 1: Top 5 products by revenue
    if "top 5 products" in question and "revenue" in question:

        return """
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

    # Question 2: Revenue by region
    elif "revenue by region" in question:

        return """
        SELECT
            c.region,
            SUM(o.quantity * p.unit_price) AS revenue
        FROM orders o
        JOIN customers c
            ON o.customer_id = c.customer_id
        JOIN products p
            ON o.product_id = p.product_id
        GROUP BY c.region
        ORDER BY revenue DESC;
        """

    # Question 3: Total revenue
    elif "total revenue" in question:

        return """
        SELECT
            SUM(o.quantity * p.unit_price) AS total_revenue
        FROM orders o
        JOIN products p
            ON o.product_id = p.product_id;
        """

    # Question 4: Top customers
    elif "top customers" in question:

        return """
        SELECT
            c.customer_name,
            SUM(o.quantity * p.unit_price) AS revenue
        FROM orders o
        JOIN customers c
            ON o.customer_id = c.customer_id
        JOIN products p
            ON o.product_id = p.product_id
        GROUP BY c.customer_name
        ORDER BY revenue DESC
        LIMIT 5;
        """

    # If question is not supported
    else:
        return None