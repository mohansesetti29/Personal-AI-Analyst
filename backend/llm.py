import os
from groq import Groq

class GroqLLM:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.1-8b-instant"

    def __call__(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a professional data analyst."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=512,
        )
        return response.choices[0].message.content


def get_llm():
    return GroqLLM()
