from backend.llm import get_llm

llm = get_llm()

def explain_result(hypothesis: str, validation_result: dict) -> str:
    prompt = f"""
You are a senior data analyst.

TASK:
Explain the statistical result below in clear business language.

RULES:
- Do NOT invent numbers
- Base explanation ONLY on the validation result
- Be concise and actionable
- Mention business implications and limitations

HYPOTHESIS:
{hypothesis}

VALIDATION RESULT:
{validation_result}
"""
    return llm(prompt)
