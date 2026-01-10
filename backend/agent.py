import json
from backend.llm import get_llm

llm = get_llm()

def generate_hypotheses(summary_text: str):
    prompt = f"""
You are a senior data analyst.

TASK:
Generate EXACTLY 3 testable hypotheses in STRICT JSON format.

RULES (MANDATORY):
- Use ONLY column names exactly as provided
- Do NOT paraphrase column names
- Do NOT add explanations
- Output VALID JSON only

Each hypothesis must include:
- hypothesis (string)
- columns (array of column names)
- type (one of: numeric_vs_numeric, binary_vs_numeric, binary_vs_binary)

FORMAT:
[
  {{
    "hypothesis": "avg_order_value is positively correlated with total_spend",
    "columns": ["avg_order_value", "total_spend"],
    "type": "numeric_vs_numeric"
  }}
]

DATASET SUMMARY:
{summary_text}
"""

    response = llm(prompt)

    try:
        return json.loads(response)
    except Exception:
        raise ValueError("LLM did not return valid JSON")
