def generate_insight(question, results):
    """
    Generate a simple business insight from query results.
    """

    if not results:
        return "No data was available to generate an insight."

    question_lower = question.lower()

    # -----------------------------------
    # Top products by revenue
    # -----------------------------------

    if "top 5 products" in question_lower and "revenue" in question_lower:

        top_product = results[0]

        return (
            f"The highest-revenue product is {top_product[0]}, "
            f"with revenue of ₹{top_product[1]:,.2f}."
        )

    # -----------------------------------
    # Total revenue
    # -----------------------------------

    if "total revenue" in question_lower:

        total_revenue = results[0][0]

        return (
            f"The total revenue across all orders is "
            f"₹{total_revenue:,.2f}."
        )

    # -----------------------------------
    # Revenue by region
    # -----------------------------------

    if "revenue by region" in question_lower:

        top_region = results[0]

        return (
            f"The region with the highest revenue is "
            f"{top_region[0]}, generating ₹{top_region[1]:,.2f}."
        )

    # -----------------------------------
    # Top customers
    # -----------------------------------

    if "top customers" in question_lower:

        top_customer = results[0]

        return (
            f"The highest-revenue customer is "
            f"{top_customer[0]}, generating ₹{top_customer[1]:,.2f}."
        )

    return "The query returned results, but no specific insight rule was defined."
# Test
test_results = [
    ("Laptop", 181560000),
    ("Smartphone", 90090000)
]

insight = generate_insight(
    "What are the top 5 products by revenue?",
    test_results
)

print("\nBusiness Insight")
print("----------------")
print(insight)