import os
from backend.llm import get_llm

def generate_hypotheses(summary_text: str) -> str:
    llm = get_llm()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(base_dir,"tools", "prompts", "hypothesis.txt")

    with open(prompt_path, "r", encoding="utf-8") as f:
        template = f.read()

    prompt = template.format(summary=summary_text)
    return llm(prompt)


def explain_result(hypothesis: str, result: dict) -> str:
    llm = get_llm()

    prompt = f"""
You are a senior data analyst.

Hypothesis tested:
{hypothesis}

Statistical result:
{result}

Explain clearly:
- Is the hypothesis supported?
- Why does this matter in business terms?
- What are the limitations of this analysis?

Rules:
- Do NOT invent data
- Do NOT assume causation
"""

    return llm(prompt)
