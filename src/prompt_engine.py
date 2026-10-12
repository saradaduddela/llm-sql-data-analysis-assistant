from pathlib import Path


def load_prompt():
    """Load the SQL generation prompt template."""

    prompt_path = Path("prompts/sql_generation_prompt.txt")

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()


def create_prompt(user_question):
    """Insert the user's question into the prompt template."""

    prompt_template = load_prompt()

    prompt = prompt_template.replace(
        "{{user_question}}",
        user_question
    )

    return prompt


# Test the prompt
question = "What are the top 5 products by revenue?"

final_prompt = create_prompt(question)

print("----- GENERATED PROMPT -----")
print(final_prompt)