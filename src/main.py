from prompt_engine import create_prompt
from sql_validator import validate_sql
from query_executor import execute_sql
from mock_llm import generate_sql 
from analyzer import generate_insight
# -----------------------------------
# 1. Get user's business question
# -----------------------------------

user_question = input("\nEnter your business question: ")

print("\nProcessing your question...")


# -----------------------------------
# 2. Create structured prompt
# -----------------------------------

prompt = create_prompt(user_question)

print("\n----- STRUCTURED PROMPT CREATED -----")
print(prompt)


# -----------------------------------
# 3. Simulate LLM-generated SQL
# -----------------------------------

# For now, we are manually providing the SQL.
# Later, the LLM will generate this automatically.

generated_sql = generate_sql(user_question)

print("\n----- GENERATED SQL -----")

if generated_sql:
    print(generated_sql)
else:
    print("Mock LLM could not generate SQL for this question.")
    exit()



print("\n----- GENERATED SQL -----")
print(generated_sql)


# -----------------------------------
# 4. Validate SQL
# -----------------------------------

is_valid, validation_message = validate_sql(generated_sql)

print("\n----- SQL VALIDATION -----")
print(validation_message)

if not is_valid:

    print("SQL execution stopped because validation failed.")

else:

    # -----------------------------------
    # 5. Execute SQL
    # -----------------------------------

    results = execute_sql(generated_sql)

    print("\n----- QUERY RESULTS -----")

    if results:

        for row in results:
            print(row)

        # -----------------------------------
        # 6. Generate Business Insight
        # -----------------------------------

        insight = generate_insight(
            user_question,
            results
        )

        print("\n----- BUSINESS INSIGHT -----")
        print(insight)

    else:

        print("No results found.")
