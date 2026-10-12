import json
import csv

from mock_llm import generate_sql
from sql_validator import validate_sql
from query_executor import execute_sql


# -----------------------------------
# 1. Load test questions
# -----------------------------------

with open("evaluation/test_questions.json", "r", encoding="utf-8") as file:
    test_questions = json.load(file)


# -----------------------------------
# 2. Prepare evaluation results
# -----------------------------------

results = []


# -----------------------------------
# 3. Test each business question
# -----------------------------------

for test in test_questions:

    question = test["question"]

    print("\n-----------------------------------")
    print("Question:", question)

    # Generate SQL
    generated_sql = generate_sql(question)

    if generated_sql is None:

        print("SQL Generation: FAILED")

        results.append({
            "question": question,
            "sql_generated": "No",
            "sql_valid": "No",
            "execution_success": "No",
            "status": "FAIL"
        })

        continue

    print("SQL Generation: SUCCESS")

    # Validate SQL
    is_valid, validation_message = validate_sql(generated_sql)

    print("SQL Validation:", validation_message)

    if not is_valid:

        results.append({
            "question": question,
            "sql_generated": "Yes",
            "sql_valid": "No",
            "execution_success": "No",
            "status": "FAIL"
        })

        continue

    # Execute SQL
    query_results = execute_sql(generated_sql)

    if query_results is not None:

        print("SQL Execution: SUCCESS")

        results.append({
            "question": question,
            "sql_generated": "Yes",
            "sql_valid": "Yes",
            "execution_success": "Yes",
            "status": "PASS"
        })

    else:

        print("SQL Execution: FAILED")

        results.append({
            "question": question,
            "sql_generated": "Yes",
            "sql_valid": "Yes",
            "execution_success": "No",
            "status": "FAIL"
        })


# -----------------------------------
# 4. Save evaluation results
# -----------------------------------

with open(
    "evaluation/evaluation_results.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "question",
        "sql_generated",
        "sql_valid",
        "execution_success",
        "status"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)


# -----------------------------------
# 5. Evaluation summary
# -----------------------------------

total = len(results)
passed = sum(1 for result in results if result["status"] == "PASS")

print("\n===================================")
print("EVALUATION SUMMARY")
print("===================================")

print(f"Total Questions: {total}")
print(f"Passed: {passed}")
print(f"Failed: {total - passed}")

if total > 0:
    accuracy = (passed / total) * 100
    print(f"Evaluation Pass Rate: {accuracy:.2f}%")

print("\nResults saved to:")
print("evaluation/evaluation_results.csv")