
import streamlit as st
import sys
from pathlib import Path

# Allow Python to find modules inside src/
PROJECT_DIR = Path(__file__).resolve().parent
SRC_DIR = PROJECT_DIR / "src"

sys.path.insert(0, str(SRC_DIR))

from mock_llm import generate_sql
from sql_validator import validate_sql
from query_executor import execute_sql
from analyzer import generate_insight

# -----------------------------------
# Page configuration
# -----------------------------------

st.set_page_config(
    page_title="SQL Data Analysis Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 SQL & Data Analysis Assistant")
st.write(
    "Ask a business question and explore your sales database."
)

st.info(
    "This version uses a Mock LLM. "
    "It supports a limited set of predefined question patterns."
)

# -----------------------------------
# User question
# -----------------------------------

question = st.text_area(
    "Enter your business question",
    placeholder="Example: What are the top 5 products by revenue?"
)

if st.button("Analyze", type="primary"):

    if not question.strip():
        st.warning("Please enter a business question.")

    else:
        with st.spinner("Analyzing your question..."):

            sql = generate_sql(question)

            if sql is None:
                st.error(
                    "The Mock LLM doesn't support this question yet. "
                    "Try one of the suggested questions below."
                )

            else:
                st.subheader("Generated SQL")
                st.code(sql, language="sql")

                is_valid, message = validate_sql(sql)

                if not is_valid:
                    st.error(f"SQL validation failed: {message}")

                else:
                    st.success(message)

                    results = execute_sql(sql)

                    if results is None:
                        st.error("SQL execution failed.")

                    elif not results:
                        st.warning("The query returned no results.")

                    else:
                        st.subheader("Query Results")

                        # Identify column names
                        question_lower = question.lower()

                        if "top 5 products" in question_lower and "revenue" in question_lower:
                            columns = ["Product", "Revenue (₹)"]
                        elif "total revenue" in question_lower:
                            columns = ["Total Revenue (₹)"]
                        elif "revenue by region" in question_lower:
                            columns = ["Region", "Revenue (₹)"]
                        elif "top customers" in question_lower:
                            columns = ["Customer", "Revenue (₹)"]
                        else:
                            columns = [
                                f"Column {i + 1}"
                                for i in range(len(results[0]))
                            ]

                        import pandas as pd
                        df = pd.DataFrame(results, columns=columns)

                        for column in df.columns:
                            if "revenue" in column.lower():
                                df[column] = df[column].apply(
                                    lambda value: f"₹{value:,.2f}"
                                    if value is not None else "N/A"
                                )

                        st.dataframe(
                            df,
                            use_container_width=True,
                            hide_index=True
                        )

                        st.subheader("Key Takeaway")

                        if "top 5 products" in question_lower and "revenue" in question_lower:
                            st.metric(
                                label="Top Revenue Product",
                                value=str(results[0][0])
                            )
                        elif "total revenue" in question_lower:
                            st.metric(
                                label="Total Revenue",
                                value=f"₹{results[0][0]:,.2f}"
                                if results[0][0] is not None else "₹0.00"
                            )

                        insight = generate_insight(
                            question,
                            results
                        )

                        st.subheader("Business Insight")
                        st.write(insight)

                       

# -----------------------------------
# Example questions
# -----------------------------------

st.divider()
st.subheader("Try these example questions")

st.markdown("""
- What are the top 5 products by revenue?
- What is the total revenue?
- What is the revenue by region?
- What are the top customers?
""")