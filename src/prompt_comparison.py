from pathlib import Path


# -----------------------------------
# Load Prompt V1
# -----------------------------------

v1_path = Path("prompts/sql_generation_prompt_v1.txt")

with open(v1_path, "r", encoding="utf-8") as file:
    prompt_v1 = file.read()


# -----------------------------------
# Load Prompt V2
# -----------------------------------

v2_path = Path("prompts/sql_generation_prompt.txt")

with open(v2_path, "r", encoding="utf-8") as file:
    prompt_v2 = file.read()


# -----------------------------------
# Compare prompts
# -----------------------------------

print("\n===================================")
print("PROMPT COMPARISON")
print("===================================")

print("\nPrompt V1")
print("-----------------------------------")
print(prompt_v1)

print("\nPrompt V2")
print("-----------------------------------")
print(prompt_v2)


# -----------------------------------
# Compare prompt characteristics
# -----------------------------------

v1_lines = len(prompt_v1.splitlines())
v2_lines = len(prompt_v2.splitlines())

v1_words = len(prompt_v1.split())
v2_words = len(prompt_v2.split())

print("\n===================================")
print("PROMPT METRICS")
print("===================================")

print(f"V1 Lines: {v1_lines}")
print(f"V2 Lines: {v2_lines}")

print(f"V1 Words: {v1_words}")
print(f"V2 Words: {v2_words}")


# -----------------------------------
# Check important instructions
# -----------------------------------

features = {
    "Role definition": "expert SQL Data Analyst",
    "Database schema": "DATABASE SCHEMA",
    "Table relationships": "TABLE RELATIONSHIPS",
    "Business definition": "BUSINESS DEFINITIONS",
    "JOIN instructions": "Use JOINs",
    "Aggregation instructions": "SUM, COUNT",
    "GROUP BY instructions": "GROUP BY",
    "ORDER BY instructions": "ORDER BY",
    "LIMIT instructions": "LIMIT",
    "Date filters": "date filters",
    "Output constraint": "Return only the SQL query"
}


print("\n===================================")
print("FEATURE COMPARISON")
print("===================================")

for feature, keyword in features.items():

    v1_has_feature = keyword.lower() in prompt_v1.lower()
    v2_has_feature = keyword.lower() in prompt_v2.lower()

    print(f"\n{feature}")
    print(f"V1: {'Yes' if v1_has_feature else 'No'}")
    print(f"V2: {'Yes' if v2_has_feature else 'No'}")